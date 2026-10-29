
from pathlib import Path
import pandas as pd

# ============================================================
# 1. CONFIGURATION
# ============================================================

PROJECT_ROOT = Path(__file__).resolve().parents[2]

RAW_DIR = PROJECT_ROOT / "02_Data" / "Raw"

REPORT_DIR = (
    PROJECT_ROOT
    / "02_Data"
    / "Documentation"
    / "relationship_reports"
)

REPORT_DIR.mkdir(parents=True, exist_ok=True)


# ============================================================
# 2. LOAD REQUIRED DATASETS
# ============================================================

print("Loading datasets...")

customers = pd.read_csv(
    RAW_DIR / "olist_customers_dataset.csv"
)

orders = pd.read_csv(
    RAW_DIR / "olist_orders_dataset.csv"
)

order_items = pd.read_csv(
    RAW_DIR / "olist_order_items_dataset.csv"
)

payments = pd.read_csv(
    RAW_DIR / "olist_order_payments_dataset.csv"
)

reviews = pd.read_csv(
    RAW_DIR / "olist_order_reviews_dataset.csv"
)

products = pd.read_csv(
    RAW_DIR / "olist_products_dataset.csv"
)

sellers = pd.read_csv(
    RAW_DIR / "olist_sellers_dataset.csv"
)

translation = pd.read_csv(
    RAW_DIR / "product_category_name_translation.csv"
)


# ============================================================
# 3. CHECK KEY UNIQUENESS AND DUPLICATES
# ============================================================

print("\nChecking key uniqueness...")

key_checks = []


def check_key(df, table_name, key_columns):
    # Count the total number of rows in current table and save that number
    total_rows = len(df)

    # Looks at the key column and count how many rows are exact duplicates of another row.
    duplicate_rows = int(
        df.duplicated(subset=key_columns).sum()
    )

    # Looks at the key columns and count how many rows are completely missing theri ID (blank or "Nan").
    missing_key_rows = int(
        df[key_columns].isna().any(axis=1).sum()
    )

    # Takes all the information we just calculated and packages it into a mini-dictionary, then drops it into the key_checks list we've created above
    key_checks.append({
        "table_name": table_name,
        "key_columns": ", ".join(key_columns),
        "total_rows": total_rows,
        "duplicate_key_rows": duplicate_rows,
        "missing_key_rows": missing_key_rows,
        "unique_key": (
            duplicate_rows == 0
            and missing_key_rows == 0
        )
    })


check_key(customers, "customers", ["customer_id"])
check_key(orders, "orders", ["order_id"])

check_key(order_items,"order_items",["order_id", "order_item_id"])

check_key(products, "products", ["product_id"])
check_key(sellers, "sellers", ["seller_id"])

check_key(payments, "payments", ["order_id", "payment_sequential"])
check_key(reviews, "reviews", ["review_id"])
check_key(translation,"category_translation",["product_category_name"])


# takes the complete list and turns it into a neat, organized data table
key_report = pd.DataFrame(key_checks)

# saves this new report table as a CSV file into a specific folder, index = False --> just tells it not to save the meaningless row numbers
key_report.to_csv(
    REPORT_DIR / "key_validation.csv",
    index=False
)

print(key_report.to_string(index=False))


# ============================================================
# 4. CHECK FOREIGN KEY RELATIONSHIPS
# ============================================================

print("\nChecking table relationships...")

# this creates an empty python list which will store the results of every relationship check in the list.
relationship_checks = []

# parent table contains the original or referenced IDs. Child table contains IDs that refer to the parent table.
def check_relationship(
    child_df,
    child_table,
    child_column,
    parent_df,
    parent_table,
    parent_column
):
    # Get non-null IDs from the child table. The missing value is excluded because this step checks whether, non-null foreign key values match a parent ID
    child_values = child_df[child_column].dropna()
    
    # Take the parent's table ID column, remove missing IDs and convert the remaining values into a python set. 
    # A set stores unique values and is efficient for checking whether an ID exists in the parent table
    parent_values = set(parent_df[parent_column].dropna())

    # It checks whether each child ID exist in the parent IDs and reverses the result (~). 
    # The True value identifies an ID that does not exist in the parent table.
    unmatched_mask = ~child_values.isin(parent_values)
    
    # Count the number of True values in the pandas dataframe. True counts as 1 and False counts as 0 in pandas.
    unmatched_count = int(unmatched_mask.sum())

    relationship_checks.append({
        "child_table": child_table,
        "child_column": child_column,
        "parent_table": parent_table,
        "parent_column": parent_column,
        "child_non_null_rows": len(child_values),
        "unmatched_rows": unmatched_count,
        "unmatched_percentage": round(
            unmatched_count / len(child_values) * 100, 4
        ) if len(child_values) else 0   # prevents division by 0. If there are no non-null child IDs, the percentage is set to 0.
    })


check_relationship(
    orders, "orders", "customer_id",
    customers, "customers", "customer_id"
)

check_relationship(
    order_items, "order_items", "order_id",
    orders, "orders", "order_id"
)

check_relationship(
    order_items, "order_items", "product_id",
    products, "products", "product_id"
)

check_relationship(
    order_items, "order_items", "seller_id",
    sellers, "sellers", "seller_id"
)

check_relationship(
    payments, "payments", "order_id",
    orders, "orders", "order_id"
)

check_relationship(
    reviews, "reviews", "order_id",
    orders, "orders", "order_id"
)


# this line converts a list which contains dictonaries into a pandas DataFrame
relationship_report = pd.DataFrame(relationship_checks)

# this saves the relationship report into a CSV file also index=False prevents pandas from adding an extra numbered index column.
relationship_report.to_csv(
    REPORT_DIR / "relationship_validation.csv",
    index=False
)


# this prints the relationship_report to the console in a well-formatted table. 
# to_string --> converts the DataFrame's into a readable text table.
print(relationship_report.to_string(index=False))


# ============================================================
# 5. CHECK ORDER STATUS AGAINST MISSING DELIVERY DATES
# ============================================================

# This code checks data quality within the orders table

print("\nChecking order status and delivery dates...")

# Defines the date columns needed to be checked
date_columns = [
    "order_approved_at",
    "order_delivered_carrier_date",
    "order_delivered_customer_date"
]

# loops through each column in the list and convert the selected column into a date/time data type that pandas can understand
# Sometimes dates are stored as strings rather that proper datetime values. Converting them makes it easier to perform date calculations,
# compare dates, and identify missing values.
for column in date_columns:
    orders[column] = pd.to_datetime(
        orders[column],
        errors="coerce"   # this tells pandas what to do if a value cannot be converted to a valid date, if found a invalid date it will be converted to NaT. It represents a missing or invalid datetime value.
    )


# The code only flags the missing dates. It does not automatically decide whether each missing date is a legitimate error.
# This code groups orders by their status and counts missing approval, carrier handover, and customer delivery dates, helping us to identify potential data-quality issues before calculating business KPIs.
status_report = (
    orders.groupby("order_status", dropna=False)  # it divides the orders into groups based on their order_status. dropna=False ensures that rows with a missing order_status are also retianed as a group instead of being excluded from the grouping
    .agg(
        total_orders=("order_id", "count"),  # this count the non-missing values in order_id column for each status group, if order_ids are missing, those will not be included in this count
        missing_approval_date=(              # selects the order_approved_at column with each status group. here x represent the approval-date values for the current group. checks for missing values and give count of those values.
            "order_approved_at",
            lambda x:x.isna().sum()
        ),
        missing_carrier_date=(               # it answers, how many orders in each status group have no recorded carrier handover date
            "order_delivered_carrier_date",
            lambda x: x.isna().sum()
        ),
        missing_customer_delivery_date=(   
            "order_delivered_customer_date",
            lambda x:x.isna().sum()
        )
    )
    .reset_index()    # convert the grouped result back into a regular DataFrame
)

# this saves the status_report to a CSV file without adding an extra numbered index column
status_report.to_csv(
    REPORT_DIR / "order_status_date_quality.csv",
    index=False
)


# this prints the status_report to the console in a well-formatted table. 
# to_string --> converts the DataFrame's into a readable text table.
print(status_report.to_string(index=False))


# ============================================================
# 6. CHECK GELOCATION DUPLICATES
# ============================================================

# This code checks the quality of geolocation dataset, specifically whether ZIP-code prefixes are repeated and whether 
# entire rows are duplicated.

print("\nChecking geolocation ZIP-code duplication...")

# load the geolocation dataset
geolocation = pd.read_csv(
    RAW_DIR / "olist_geolocation_dataset.csv"
)

# This code measures the size and duplication patterns of your geolocation dataset, helping you understand 
# its structure and avoid problems such as row multiplication when joining it with customer or seller data.
geo_report = pd.DataFrame([{          # it convert a list of dictionary values into a DataFrame
    "total_rows": len(geolocation),   # returns the total number to rows in the dataframe. This tells us how many records exist in the dataset.
    "unique_zip_prefixes": (          
        geolocation["geolocation_zip_code_prefix"].nunique()  # selects the column containing ZIP-code prefixes. The nunique() method counts the number of distinct, non-null values in that column.
    ),                                                        # this helps to understand how many distinct ZIP-code prefixes are represented in the dataset.  
    "duplicate_zip_prefix_rows": int(                         # int() converts result to a standard python integer
        geolocation.duplicated(                               # duplicated() method marks repeated values as True, except for the 1st occurrence of each value. The 1st occurrence is retained as original, and subsequent occurrences are marked as duplicates
            subset=["geolocation_zip_code_prefix"]            # select the column to check. This tell pandas to check duplicates based only on ZIP-code prefixes
        ).sum()                                               # Count the duplicated since True = 1 and False = 0.
    ),
    "exact_duplicate_rows": int(
        geolocation.duplicated().sum()                        # This checks whether entire rows are repeated. This metric is useful for identifying complete repeated records.
    )
}])


geo_report.to_csv(
    REPORT_DIR / "geolocation_quality.csv",
    index=False
)

print(geo_report.to_string(index=False))


# ============================================================
# 7. FINISH
# ============================================================

print("\nValidation completed.")
print(f"Reports saved to: {REPORT_DIR}")
print("\nGenerated reports:")
print("1. key_validation.csv")
print("2. relationship_validation.csv")
print("3. order_status_date_quality.csv")
print("4. geolocation_quality.csv")
