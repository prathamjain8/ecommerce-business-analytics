# pathlib --> python's modern object-oriented filesystem path library. It handled paths seamlessly
#             across windows, macOS, and Linux, without worrying about manual 
#             backslash/forward-slash(/ vs \) issue

# Pandas --> data manipulation python library
from pathlib import Path
import pandas as pd


# ==================================================
# STEP 1: SET UP PROJECT PATHS
# ==================================================

# Dynamically find the root folder of our project regardless of where we run the script from
# __file__ --> a special python variable containing the path of current script
# .resolve() --> convert the path into complete absolute path
# .parents[3] --> 3rd parent directory from the current script (moves to root)
PROJECT_ROOT = Path(__file__).resolve().parents[2]


# uses pathlib's (/) operator to join the path components
RAW_DIR = PROJECT_ROOT / "02_Data" / "Raw"


# Constructs the target path directory where generated data profiling reports will be saved.
REPORT_DIR = PROJECT_ROOT/"02_Data"/"Documentation"/"profiling_reports"


# .mkdir() --> created directory on our disk
# parents = True --> created any intermediate parent folders if they dont already exist
# exist_ok = True --> prevent parent from throwing a FileExistError if the profiling_reports folder
#                     already exists. making the script re-runnable without errors.
REPORT_DIR.mkdir(parents=True, exist_ok=True)


# ==================================================
# STEP 2: FIND ALL CSV FILES
# ==================================================


# Searched RAW_DIR and find all files ending with .csv, returning them as path objects
# sorted() --> sort the files alphabetically, ensuring consistent processing order
# csv_files = stores the resulting list of sorted csv file paths.
csv_files = sorted(RAW_DIR.glob("*.csv"))


# checks if csv_files list is empty, and immediately stops script execution with a clear error message
# if not CSVs are found, preventing silent failures or crashes later on.
if not csv_files:
    raise FileNotFoundError(
        f"No CSV files found in the folder: {RAW_DIR}"
    )

print(f"Number of CSV files found: {len(csv_files)}")
print(f"Raw data location: {RAW_DIR}")



# ==================================================
# STEP 3: CREATE EMPTY LISTS FOR REPORTS
# ==================================================
inventory = []
column_profiles = []
missing_profiles = []
duplicate_profiles = []
sample_previews = []



# ==================================================
# STEP 4: ANALYZE EACH CSV FILE
# ==================================================

for file_path in csv_files:
    print(f"\nProcessing: {file_path.name}")

    df = pd.read_csv(file_path, low_memory=False)  # loads the csv in dataframe, low_memory=False --> reads the file in full to avoid mixed data-type inference warnings.

    row_count, column_count = df.shape

    # ------------------------------------------------
    # 4A. DATA INVENTORY
    # ------------------------------------------------

    inventory.append({
        "file_name": file_path.name,
        "row_count": row_count,
        "column_count": column_count,
        "file_size_mb": round(
            file_path.stat().st_size / (1024*1024),3  # gets file size in bytes via .stat().st_size, convert to MB, and round to 3 decimal places
        )
    })


    # ------------------------------------------------
    # 4B. COLUMN PROFILE
    # ------------------------------------------------
    for column in df.columns:   # loop through every column in the current dataframe
        column_profiles.append({
            "file_name": file_path.name,
            "column_name": column,
            "data_type": str(df[column].dtype),
            "non_null_count": int(df[column].count()),  # number of non-missing entries
            "unique_values": int(df[column].nunique(dropna=True)) # count distinct values, ignoring nulls.
        })


    # ------------------------------------------------
    # 4C. MISSING VALUES
    # ------------------------------------------------
    missing_counts = df.isna().sum()  # find all null/NaN values per cell and sums them up for each column, 
                                      # returning a Series mapping column names to missing counts.

    for column, count in missing_counts.items():

        missing_percentage = (
            (count/row_count)*100
            if row_count > 0
            else 0
        )

        missing_profiles.append({
            "file_name": file_path.name,
            "column_name": column,
            "missing_count": int(count),
            "missing_percentage":round(missing_percentage, 2)
        })


    # ------------------------------------------------
    # 4D. EXACT DUPLICATE ROWS
    # ------------------------------------------------
    duplicate_count = int(df.duplicated().sum())

    duplicate_percentage = (
            (duplicate_count/row_count)*100
            if row_count > 0
            else 0
        )

    duplicate_profiles.append({
            "file_name": file_path.name,
            "row_count": row_count,
            "exact_duplicate_rows": duplicate_count,
            "duplicate_percentage":round(duplicate_percentage, 2)
        })

    
    
    # ------------------------------------------------
    # 4E. SAMPLE DATA PREVIEW
    # ------------------------------------------------
    preview = df.head(5).copy()  #Extract the first 5 rows and creates an independent copy 
                                 # so changes dont affect the original DataFrame or trigger warnings.

    # Inserts a new column named "source_file" at index 0 containing filename, 
    # identifying which CSV the preview rows belong to.
    preview.insert(
        0,
        "source_file",
        file_path.name
    )

    # Adds the 5-row preview DataFrame to the sample_previews list for combining into a final report later
    sample_previews.append(preview)


# ==================================================
# STEP 5: CONVERT RESULTS INTO DATAFRAMES
# ==================================================
inventory_df = pd.DataFrame(inventory)

column_profiles_df = pd.DataFrame(column_profiles)

missing_profiles_df = pd.DataFrame(missing_profiles)

duplicate_profiles_df = pd.DataFrame(duplicate_profiles)

# stacks all the individual 5-row sample DataFrame vertically into one combined preview table.
# ignore_index=True --> creates a fresh, continuous row index instead of repeating 0-4 from each subset
# sort=False --> retains the original column ordering rather than sorting columns alphabetically.
sample_previews_df = pd.concat(
    sample_previews, ignore_index=True, sort=False
)


# ==================================================
# STEP 6: SAVE REPORTS AS CSV FILES
# ==================================================
inventory_df.to_csv(REPORT_DIR/"data_inventory.csv", index=False)

column_profiles_df.to_csv(REPORT_DIR / "column_profile.csv",index=False)

missing_profiles_df.to_csv(REPORT_DIR / "missing_values.csv",index=False)

duplicate_profiles_df.to_csv(REPORT_DIR / "duplicate_summary.csv",index=False)

sample_previews_df.to_csv(REPORT_DIR / "sample_preview.csv",index=False)


# ==================================================
# STEP 7: DISPLAY SUMMARY IN THE TERMINAL
# ==================================================
print("\n" + "=" * 60)
print("DATA INVENTORY SUMMARY")
print("=" * 60)

print(inventory_df.to_string(index=False))

print("\n" + "=" * 60)
print("EXACT DUPLICATE ROW SUMMARY")
print("=" * 60)

print(duplicate_profiles_df.to_string(index=False))

print("\n" + "=" * 60)
print("PROFILING COMPLETED SUCCESSFULLY")
print("=" * 60)

print(f"\nReports saved in:\n{REPORT_DIR}")

print("\nGenerated reports:")
print("1. data_inventory.csv")
print("2. column_profile.csv")
print("3. missing_values.csv")
print("4. duplicate_summary.csv")
print("5. sample_preview.csv")