# ShopSphere — Business Requirements Document

**Project:** E-commerce Business Analytics  
**Working dataset:** Brazilian E-Commerce Public Dataset by Olist (subject to validation during data discovery)  
**Document status:** Business requirements baseline — to be validated against available data

---

## 1. Business Background

ShopSphere is a fictional B2B2C e-commerce marketplace that connects sellers with consumers. Sellers list products on the platform, and consumers purchase products across multiple categories and regions.

To operate effectively, ShopSphere needs to understand its sales performance, customer purchasing behavior, seller performance, delivery reliability, and customer satisfaction. Management needs reliable analysis to identify growth opportunities, prioritize operational improvements, and improve the customer experience.

For this portfolio project, ShopSphere is a business case used to frame the analysis. The selected public dataset will be assessed before any requirement is treated as measurable. The project will produce historical analysis; it will not be described as a real-time analytics system unless a live data source is added.

## 2. Business Problem

Management needs a consistent view of business performance across revenue, sales, customer behavior, seller performance, delivery operations, and customer satisfaction. Without a structured analytics process, it can be difficult to identify trends, compare performance fairly, understand where problems are concentrated, and decide which areas deserve attention first.

ShopSphere therefore needs an analytics solution that combines data from relevant business areas, checks data quality, defines consistent metrics, and presents findings in a form that supports business decisions.

Some questions—such as campaign effectiveness, profit margin, inventory availability, and support-ticket drivers—may require data that is not present in the selected public dataset. These will be documented as data gaps if they cannot be measured reliably.

## 3. Project Objectives

The project aims to:

1. Analyze revenue and sales trends over time.
2. Identify the products, categories, sellers, and regions that contribute most to sales.
3. Examine customer purchasing and repeat-purchase behavior.
4. Measure delivery timeliness and identify regions or sellers with comparatively poor delivery performance.
5. Analyze customer ratings and explore their association with delivery experience.
6. Develop comparable seller-performance measures using sales, delivery, and rating data where available.
7. Identify data-quality issues and document limitations that affect interpretation.
8. Translate findings into evidence-based recommendations for management.

The project will not claim to measure profit, marketing campaign ROI, inventory availability, or causal drivers unless suitable data and methods support those analyses.

## 4. Stakeholders

### 4.1 CEO / Executive Management

**Decision to support:** Where should the business focus to grow sales and improve overall performance?

**Information needed:** Revenue trends, major sales contributors, underperforming areas, customer behavior, and operational risks.

### 4.2 Head of Sales

**Decision to support:** Which products, categories, sellers, and regions offer the strongest sales performance or potential growth opportunities?

**Information needed:** Sales value and order volume by product, category, seller, region, and time period.

### 4.3 Marketing Manager

**Decision to support:** Which customer groups and purchasing patterns should inform future marketing strategy?

**Information needed:** Customer purchase frequency, customer value, category preferences, and geographic purchasing patterns.

**Limitation:** Campaign impressions, clicks, spend, attribution, and website traffic are not assumed to be available. Campaign performance and ROI will only be analyzed if suitable campaign data is obtained.

### 4.4 Operations Manager

**Decision to support:** Where are delivery delays concentrated, and where should operational investigation be prioritized?

**Information needed:** Order status, purchase and delivery timestamps, estimated delivery dates, seller, and customer geography.

### 4.5 Seller Management Team

**Decision to support:** Which sellers are performing well, and which may need further investigation or support?

**Information needed:** Seller-level sales, order volume, delivery timeliness, cancellation information where available, and customer ratings.

### 4.6 Customer Experience Team

**Decision to support:** What patterns are associated with poor customer ratings, and where could the customer experience be improved?

**Information needed:** Customer reviews/ratings, order and delivery information, product/category information, and customer geography.

---

## 5. Stakeholder Requirements

### 5.1 CEO / Executive Management

1. The solution must show sales-value trends over time.
2. It must identify the main contributors to sales by product, category, seller, region, and customer group where the required data supports the breakdown.
3. It must highlight areas with comparatively low or declining sales.
4. It must allow comparison of business performance across consistent time periods.
5. It must summarize key findings and prioritize opportunities or risks supported by the analysis.

### 5.2 Head of Sales

1. The solution must compare sales value and order volume by product and category.
2. It must compare product/category performance across regions.
3. It must identify products and categories that perform strongly across multiple regions.
4. It must highlight regions with relatively low sales activity for further investigation.
5. It must compare sales performance across sellers, products, categories, and regions.

### 5.3 Marketing Manager

1. The solution must describe customer groups by purchasing behavior and sales contribution.
2. It must measure repeat-purchase behavior where customer/order identifiers allow it.
3. It must compare product-category preferences across customer groups.
4. It must compare purchasing activity across customer regions.
5. It must provide evidence-based behavioral insights that may inform future marketing decisions.

**Data caveat:** These analyses describe observed purchasing behavior; they do not prove that a marketing campaign caused a purchase. Campaign effectiveness requires campaign, traffic, spend, and attribution data.

### 5.4 Operations Manager

1. The solution must identify regions with high late-delivery rates.
2. It must compare delivery performance across relevant time periods, regions, and sellers.
3. It must examine factors associated with late delivery, without automatically treating association as causation.
4. It must distinguish delivered, late-delivered, cancelled, and otherwise undelivered orders where status information permits.
5. It must help prioritize regions or seller groups for operational investigation.

### 5.5 Seller Management Team

1. The solution must compare sellers by sales value and order volume.
2. It must compare seller delivery performance using clearly defined and comparable measures.
3. It must identify sellers with consistently low customer ratings, accounting for rating volume.
4. It must compare cancellation and fulfillment outcomes where relevant data is available.
5. It must identify sellers whose results warrant further investigation rather than labelling a seller as poor based on a single metric.

### 5.6 Customer Experience Team

1. The solution must measure customer ratings and summarize rating patterns by product, category, and seller.
2. It must explore the relationship between delivery timeliness and customer ratings.
3. It must describe repeat-purchase and high-value customer behavior using explicit, reproducible definitions.
4. It must compare customer experience patterns across regions and relevant order groups.
5. It must identify patterns associated with low ratings while clearly distinguishing correlation from causation.

---

## 6. Business Questions

### 6.1 CEO / Executive Management

1. How is sales value changing over time?
2. Which products, categories, sellers, and regions contribute most to sales value?
3. Which products, categories, sellers, or regions have comparatively low or declining sales?
4. What observable changes in order volume, average order value, product mix, or regional mix coincide with sales declines?
5. Which areas appear to offer the strongest evidence-based opportunities for growth or improvement?

### 6.2 Head of Sales

1. Which products and categories generate the highest sales value and order volume in each region?
2. Which regions have comparatively low purchasing activity or sales value?
3. Which products and categories perform consistently well across multiple regions?
4. Which categories show potential for regional growth based on observed sales patterns?
5. How does sales performance vary across sellers, products, categories, regions, and time periods?

### 6.3 Marketing Manager

1. Which observable customer groups contribute most to sales value?
2. Which customer groups show the highest repeat-purchase rate?
3. Which product categories are most frequently purchased by different customer groups?
4. Which regions have many recorded customers but relatively low purchasing activity?
5. What purchasing patterns could inform future marketing hypotheses?

### 6.4 Operations Manager

1. Which regions have the highest late-delivery rate?
2. Which order, seller, or geographic characteristics are associated with late delivery?
3. Which sellers have the highest late-delivery rate, among sellers with sufficient order volume for a meaningful comparison?
4. Which regions and sellers most often deliver on or before the estimated delivery date?
5. Where should operational investigation be prioritized based on the scale and rate of late deliveries?

### 6.5 Seller Management Team

1. Which sellers generate the highest sales value and order volume?
2. Which sellers have the strongest delivery performance?
3. Which sellers show weaker results across sales, delivery, and customer-rating measures?
4. Which sellers receive consistently low ratings, taking the number of reviews into account?
5. Which sellers should be investigated for potential improvement, and which performance measures need attention?

### 6.6 Customer Experience Team

1. Which customers demonstrate high sales contribution or repeat-purchase behavior?
2. Which products, categories, and sellers receive the highest and lowest customer ratings?
3. Is late delivery associated with lower customer ratings?
4. Which regions have the highest recorded concentration of repeat or high-value customers?
5. Which observed customer, product, seller, or delivery characteristics are associated with low customer ratings?

---

## 7. Data Requirements

These requirements describe the information needed conceptually. Actual fields, coverage, and limitations will be verified during data discovery and gap analysis.

### 7.1 Revenue and Sales Data

1. Order-item transaction values to estimate sales value.
2. Order timestamps or purchase dates for time-based analysis.
3. Product and category identifiers to compare product/category contributions.
4. Seller identifiers to measure seller-level sales contribution.
5. Customer/order identifiers to analyze customer purchasing patterns.
6. Shipping charges, discounts, refunds, or other adjustments if available and relevant to the chosen sales-value definition.

### 7.2 Customer Data

1. Stable customer identifiers to link purchases across orders.
2. Customer location fields for geographic comparisons.
3. Customer order history to analyze purchase frequency and repeat behavior.
4. Customer/order value information to estimate customer contribution.
5. Customer feedback and rating records where available.

Demographic or marketing attributes must not be assumed to exist. Customer segments will be defined using fields actually available and documented.

### 7.3 Product Data

1. Product identifiers and product/category descriptions.
2. Product category mapping or translation where available.
3. Order-item quantities and transaction values to compare sales performance.
4. Product review/rating records where available.
5. Product attributes, such as dimensions, if available and relevant to analysis.

Inventory/stock history is not assumed to be available and will be treated as a potential data gap.

### 7.4 Seller Data

1. Seller identifiers and available seller location fields.
2. Order-item records linking sellers to sold products and orders.
3. Sales-value and order-volume information for seller comparisons.
4. Order and delivery information linked to sellers.
5. Customer ratings/reviews linked to relevant orders, products, or sellers where the data model supports that relationship.

Seller names, seller categories, costs, and internal seller service records must not be assumed to exist.

### 7.5 Order and Delivery Data

1. Order identifiers and order status.
2. Purchase, approval, carrier handoff, and customer-delivery timestamps where available.
3. Estimated delivery dates to compare promised and actual delivery timing.
4. Cancellation or non-delivery status information.
5. Links between orders, order items, sellers, customers, and delivery records.
6. Customer and seller geography for regional comparisons.
7. Sufficient status and timestamp completeness to define eligible orders for each delivery metric.

### 7.6 Customer Experience Data

1. Review/rating identifiers, scores, and available timestamps.
2. Links between reviews, orders, products, and customers where supported.
3. Order and delivery data to compare ratings across delivery outcomes.
4. Product/category and seller information for rating comparisons.
5. Review text, if available and suitable, for optional qualitative analysis.

Support tickets, complaint categories, and customer-service resolution times are not assumed to be available.

### 7.7 Data Quality and Linkage Requirements

1. Primary identifiers should be checked for missing values and duplicates.
2. Relationships between orders, order items, products, sellers, customers, payments, and reviews should be validated.
3. Dates must be checked for invalid sequences and missing values.
4. Monetary fields must be checked for nulls, unexpected values, and consistent interpretation.
5. Order statuses must be standardized and documented before KPI calculation.
6. Any excluded records, assumptions, and limitations must be recorded.
7. KPI calculations must use clearly stated populations and denominators.

---

## 8. Key Performance Indicators (KPIs)

The following is the proposed KPI set. Definitions and formulas are provisional until the dataset has been profiled. Each KPI must be validated against field availability, grain, null handling, and business meaning before implementation.

### 8.1 Revenue and Sales KPIs

**1. Gross Item Sales Value**
- **Definition:** Sum of recorded item prices for included order items.
- **Proposed calculation:** `SUM(order_item_price)`
- **Purpose:** Measure the value of items sold before deciding whether shipping, discounts, refunds, or cancellations should be included.
- **Caution:** This is not profit. The final revenue definition must specify treatment of cancelled orders, refunds, and shipping charges.

**2. Sales Value Growth Rate**
- **Definition:** Percentage change in sales value between comparable periods.
- **Proposed calculation:** `(Current-period sales value - Previous-period sales value) / Previous-period sales value × 100`
- **Purpose:** Track growth or decline.
- **Caution:** If the previous period is zero or missing, the growth rate is undefined. Compare equivalent periods.

**3. Total Orders**
- **Definition:** Count of distinct orders within the defined order population.
- **Proposed calculation:** `COUNT(DISTINCT order_id)`
- **Purpose:** Measure order volume.
- **Caution:** State whether cancelled, unavailable, or otherwise incomplete orders are included.

**4. Average Order Value (AOV)**
- **Definition:** Average recorded sales value per eligible order.
- **Proposed calculation:** `Eligible sales value / Number of eligible orders`
- **Purpose:** Understand average basket value.
- **Caution:** Use a consistent order population and specify whether shipping charges are included.

**5. Average Items per Order**
- **Definition:** Average number of order items per eligible order.
- **Proposed calculation:** `Total order-item rows (or units, depending on available quantity) / Number of eligible orders`
- **Purpose:** Understand basket size.
- **Caution:** Distinguish order-item lines from physical item quantity if a quantity field exists.

**6. Sales Contribution Percentage**
- **Definition:** Share of total sales value contributed by a product, category, seller, or region.
- **Proposed calculation:** `Segment sales value / Total sales value × 100`
- **Purpose:** Identify major contributors and concentration.
- **Caution:** The segment and total must use the same filters and eligible order population.

### 8.2 Customer KPIs

**1. Unique Purchasing Customers**
- **Definition:** Count of distinct customers with at least one eligible purchase.
- **Proposed calculation:** `COUNT(DISTINCT customer_id)`
- **Purpose:** Measure the active purchasing customer base.
- **Caution:** Confirm whether the dataset's customer identifier represents a person, account, or order-specific customer record.

**2. Repeat Customer Rate**
- **Definition:** Percentage of eligible customers who made more than one distinct order during the analysis period.
- **Proposed calculation:** `Customers with >1 eligible order / Customers with ≥1 eligible order × 100`
- **Purpose:** Assess repeat purchasing.
- **Caution:** Results depend on the observation window and customer identifier quality.

**3. Orders per Purchasing Customer**
- **Definition:** Average number of eligible orders per purchasing customer.
- **Proposed calculation:** `Distinct eligible orders / Unique purchasing customers`
- **Purpose:** Measure purchase frequency at an aggregate level.

**4. Customer Sales Contribution**
- **Definition:** Sales value attributed to a customer over the defined analysis period.
- **Proposed calculation:** Sum eligible order-item sales value by customer.
- **Purpose:** Identify customers with high observed sales contribution.
- **Caution:** Historical contribution is not a prediction of future value.

**5. High-Value Customer Share**
- **Definition:** Percentage of purchasing customers classified as high-value under a documented rule.
- **Proposed calculation:** `Customers meeting the high-value rule / Purchasing customers × 100`
- **Purpose:** Describe the size of a selected customer segment.
- **Caution:** Define the rule using observed data (for example, a documented sales-value percentile); do not label customers “genuine” without evidence.

### 8.3 Product KPIs

**1. Product Sales Value**
- **Definition:** Eligible item sales value attributed to each product.
- **Proposed calculation:** Sum item price by product.
- **Purpose:** Rank products by sales contribution.

**2. Units or Order-Item Lines Sold**
- **Definition:** Number of units sold or order-item lines, depending on available quantity data.
- **Proposed calculation:** Sum quantity if available; otherwise count order-item lines and label the metric accordingly.
- **Purpose:** Compare sales volume.
- **Caution:** Do not call order-item line count “units sold” unless quantity is known.

**3. Product Sales Contribution Percentage**
- **Definition:** Product sales value as a share of total eligible sales value.
- **Proposed calculation:** `Product sales value / Total sales value × 100`
- **Purpose:** Measure each product's contribution.

**4. Category Sales Value**
- **Definition:** Eligible item sales value grouped by product category.
- **Proposed calculation:** Sum item price by category.
- **Purpose:** Identify high- and low-contributing categories.

**5. Average Customer Rating by Product/Category**
- **Definition:** Mean recorded rating for products or categories with review data.
- **Proposed calculation:** `SUM(rating) / COUNT(non-null ratings)` within the group.
- **Purpose:** Compare customer feedback.
- **Caution:** Show review count alongside averages; small samples can be misleading.

### 8.4 Seller KPIs

**1. Seller Sales Value**
- **Definition:** Eligible item sales value attributed to each seller.
- **Proposed calculation:** Sum item price by seller.
- **Purpose:** Compare seller sales contribution.

**2. Seller Order Volume**
- **Definition:** Number of distinct orders containing at least one item sold by a seller.
- **Proposed calculation:** Count distinct order IDs by seller.
- **Purpose:** Compare seller activity.
- **Caution:** An order can contain items from multiple sellers; seller order counts therefore should not necessarily be summed to get marketplace order count.

**3. Seller Late Delivery Rate**
- **Definition:** Percentage of eligible delivered orders/items associated with a seller that arrived after the estimated delivery date.
- **Proposed calculation:** `Late eligible deliveries / Eligible deliveries with valid actual and estimated dates × 100`
- **Purpose:** Compare seller-linked delivery outcomes.
- **Caution:** Confirm whether delivery dates can be attributed at order or seller/item level. Do not penalize sellers for outcomes they do not control without further investigation.

**4. Average Seller-Linked Delivery Time**
- **Definition:** Average elapsed time between purchase and delivery for eligible delivered orders associated with a seller.
- **Proposed calculation:** Average of `actual delivery timestamp - purchase timestamp`.
- **Purpose:** Compare elapsed delivery time.
- **Caution:** Compare like-for-like orders and state the unit (hours or days).

**5. Average Rating for Seller-Linked Reviews**
- **Definition:** Mean customer rating for reviews that can be reliably linked to a seller's orders/items.
- **Proposed calculation:** Average eligible rating by seller.
- **Purpose:** Identify potential customer-experience issues.
- **Caution:** Display rating count and avoid ranking sellers with very small samples as if they were directly comparable.

### 8.5 Operations KPIs

**1. Late Delivery Rate**
- **Definition:** Percentage of eligible delivered orders delivered after the estimated delivery date.
- **Proposed calculation:** `Delivered orders with actual delivery after estimated date / Delivered orders with valid actual and estimated dates × 100`
- **Purpose:** Measure delivery timeliness.
- **Caution:** Exclude or separately report records without valid dates; document the eligible population.

**2. On-Time Delivery Rate**
- **Definition:** Percentage of eligible delivered orders delivered on or before the estimated delivery date.
- **Proposed calculation:** `Delivered orders with actual delivery on or before estimated date / Delivered orders with valid actual and estimated dates × 100`
- **Purpose:** Measure adherence to estimated delivery dates.
- **Caution:** Under a consistent definition, on-time and late rates should total 100% within the same eligible population.

**3. Average Delivery Time**
- **Definition:** Average elapsed time from purchase to customer delivery for eligible delivered orders.
- **Proposed calculation:** Average of `customer delivery timestamp - purchase timestamp`.
- **Purpose:** Measure elapsed fulfillment time.
- **Caution:** This includes multiple stages of the fulfillment process and does not, by itself, identify which stage caused a delay.

**4. Average Delivery Delay (Days)**
- **Definition:** Average number of days between actual and estimated delivery for eligible late orders, or signed difference if explicitly defined that way.
- **Proposed calculation:** Average of `actual delivery date - estimated delivery date` for late deliveries.
- **Purpose:** Quantify delay severity.
- **Caution:** State whether early/on-time deliveries are excluded. This proposed version includes late deliveries only.

**5. Cancellation Rate**
- **Definition:** Percentage of orders cancelled within a clearly defined order population.
- **Proposed calculation:** `Cancelled orders / Orders in the defined population × 100`
- **Purpose:** Monitor cancellations.
- **Caution:** Define the eligible status population and confirm that cancellation statuses are present and reliable. The rate does not explain cancellation reasons unless reason data exists.

### 8.6 Customer Experience KPIs

**1. Average Customer Rating**
- **Definition:** Mean of valid recorded customer ratings.
- **Proposed calculation:** `SUM(valid ratings) / COUNT(valid ratings)`
- **Purpose:** Summarize recorded customer feedback.
- **Caution:** Rating scales and missing values must be validated; include the number of ratings.

**2. Low-Rating Share**
- **Definition:** Percentage of valid ratings at or below a threshold defined before analysis.
- **Proposed calculation:** `Ratings at/below defined threshold / All valid ratings × 100`
- **Purpose:** Track the share of low ratings.
- **Caution:** Choose and document the threshold based on the dataset's rating scale before interpreting results.

**3. Rating by Delivery Outcome**
- **Definition:** Average rating for eligible on-time versus late deliveries.
- **Proposed calculation:** Average rating grouped by delivery outcome.
- **Purpose:** Explore whether late delivery is associated with lower ratings.
- **Caution:** This is an association, not proof that delay caused a rating.

**4. Review Coverage**
- **Definition:** Percentage of eligible orders with a linked review, if the relationships permit reliable order-level linkage.
- **Proposed calculation:** `Eligible orders with linked review / Eligible orders × 100`
- **Purpose:** Understand how much of the order population is represented by reviews.
- **Caution:** Confirm the review table's grain and linkage rules before calculation.

**5. Customer Rating by Product Category/Seller**
- **Definition:** Average rating and number of reviews for each product category or seller where linkage is reliable.
- **Proposed calculation:** Average valid rating and count of valid ratings by group.
- **Purpose:** Identify groups that may warrant further investigation.
- **Caution:** Account for sample size and do not infer causality from group differences.

### 8.7 KPI Governance Rules

1. Every KPI must have one documented definition, formula, grain, time field, filter set, and data source.
2. Numerators and denominators must use consistent populations.
3. Missing, invalid, cancelled, and undelivered records must be handled explicitly.
4. Monetary KPIs must state whether they include item prices, freight/shipping, discounts, refunds, and cancelled orders.
5. Customer and seller comparisons must include sample sizes where appropriate.
6. Historical sales value must not be labelled profit or net revenue without the necessary cost and adjustment data.
7. KPIs will be finalized only after data profiling and availability checks.

---

## 9. Expected Business Outcomes

The project is expected to deliver the following analytical outputs and decision support. These are intended outcomes, not guaranteed business improvements; no percentage targets are assumed before a baseline is measured.

### 9.1 Revenue and Sales Visibility

- Provide a consistent view of historical sales-value trends and order volume.
- Identify major contributors and areas with declining or comparatively low sales.
- Support evidence-based discussion of potential growth priorities.

### 9.2 Customer Behavior Insights

- Describe repeat-purchase behavior and customer sales contribution.
- Identify customer groups using transparent, reproducible rules.
- Reveal product/category preferences and geographic purchasing patterns that may inform future engagement strategies.

### 9.3 Product and Category Performance

- Rank products and categories by sales value and available volume measures.
- Identify products/categories that perform strongly across regions.
- Highlight areas that merit further investigation, without assuming that low sales necessarily mean poor product quality or low demand.

### 9.4 Seller Performance Visibility

- Compare seller sales contribution, order volume, delivery outcomes, and ratings where data supports those comparisons.
- Flag potential performance issues for review using multiple measures and adequate sample sizes.
- Provide a consistent basis for seller-management discussions.

### 9.5 Delivery and Operations Insights

- Quantify late-delivery rate, on-time delivery rate, elapsed delivery time, and delay severity where dates are valid.
- Identify regions, periods, and seller-linked groups with comparatively poor delivery outcomes.
- Help prioritize operational investigation while distinguishing observed associations from confirmed causes.

### 9.6 Customer Experience Insights

- Summarize customer ratings and low-rating patterns.
- Explore the association between delivery outcomes and ratings.
- Identify products, categories, sellers, or regions that may need deeper investigation.

### 9.7 Data Quality and Reproducibility

- Produce a documented data dictionary and data-quality report.
- Record missing values, duplicates, invalid timestamps, relationship issues, and metric exclusions.
- Maintain reproducible SQL/Python analyses and documented KPI definitions.
- Provide an executive summary/dashboard and practical recommendations linked to evidence.

### 9.8 Success Criteria for the Analytics Project

The project will be considered analytically complete when:

1. The selected dataset and its limitations are documented.
2. Required tables and relationships have been profiled and validated.
3. Data-quality issues and resolution/exclusion decisions are documented.
4. Each implemented KPI has a reviewed definition and reproducible calculation.
5. The key business questions have been answered where data permits, and unavailable questions are recorded as gaps.
6. The final dashboard/report communicates findings, caveats, and recommendations clearly.
7. Recommendations are traceable to results and do not claim causal effects that the analysis cannot establish.

---

## 10. Assumptions, Constraints, and Data Gaps to Validate

The Olist public dataset is the proposed analytical source, but its exact coverage must be checked before implementation.

| Business need | Current assumption / risk | Validation approach |
|---|---|---|
| Profit and profit margin | Product costs, operating costs, and full margin data may be absent | Do not calculate profit unless cost data is found and validated |
| Marketing campaign ROI | Campaign spend, impressions, clicks, and attribution may be absent | Mark campaign ROI as unavailable unless additional data is sourced |
| Inventory and stockouts | Inventory snapshots/history may be absent | Do not infer stock availability from sales alone |
| Customer demographics | Detailed demographics may be absent | Build segments only from available, appropriate fields |
| Customer support | Support tickets and resolution data may be absent | Treat support-driver analysis as out of scope unless data is obtained |
| Delivery-delay causes | Timestamp patterns show associations, not necessarily causes | Phrase conclusions as associations and recommend investigation |
| Seller delivery attribution | Orders may contain items from multiple sellers | Validate the grain and seller-to-order relationships before assigning delivery outcomes |
| Repeat customers | Identifier semantics may affect customer-level analysis | Validate customer IDs and define the observation period |
| Real-time reporting | The public dataset is historical | Describe outputs as historical analytics, not real-time monitoring |
| Geographic comparisons | Location coverage and granularity may vary | Validate location fields and document excluded/unknown locations |

---

## 11. Scope and Deliverables

### In Scope

- Business requirement and question documentation.
- Dataset discovery, table profiling, and data dictionary.
- Data-quality checks and relationship validation.
- KPI definitions and data-gap assessment.
- SQL analysis for revenue, customers, products, sellers, delivery, and customer experience.
- Python-based profiling and supplementary analysis where useful.
- Excel analysis where it adds value.
- Power BI dashboard/report.
- Documented findings, limitations, recommendations, and executive presentation.

### Out of Scope Unless Additional Data Becomes Available

- Profit-margin calculations requiring unavailable costs.
- Marketing campaign ROI requiring campaign performance/spend data.
- Inventory/stockout analysis requiring inventory history.
- Causal claims about why delays, low ratings, or sales declines occurred.
- Real-time monitoring based solely on a historical public dataset.

### Planned Deliverables

1. Business Requirements Document.
2. Data dictionary and data availability/gap matrix.
3. Data-quality report.
4. KPI dictionary.
5. SQL scripts and analysis outputs.
6. Python notebooks/scripts for profiling and supplementary analysis.
7. Power BI report/dashboard.
8. Insights and recommendations document.
9. Executive presentation.
10. Project README with setup instructions, methodology, and limitations.

---

## 12. Next Steps

1. Review and freeze this business requirements baseline.
2. Download and inventory the Olist dataset.
3. Create a data dictionary and profile every table.
4. Map each requirement and KPI to actual fields/tables in a data availability matrix.
5. Record unsupported requirements as data gaps instead of inventing data.
6. Perform data-quality checks and validate table relationships.
7. Finalize KPI definitions based on confirmed data grain and availability.
8. Complete SQL analysis, Python analysis, dashboarding, and recommendations.

**Important:** KPI definitions in Section 8 are proposed definitions. They must be confirmed after data discovery, particularly the sales-value definition, eligible order populations, customer identifier semantics, review linkage, and seller-level delivery attribution.
