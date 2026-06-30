# Mutual Fund Data Analytics

## Project Description

This project focuses on analyzing mutual fund data to understand fund performance, investor behavior, and industry trends using Python, SQL, and data visualization tools. The project follows a complete data analytics workflow, starting from data collection and cleaning, followed by database design, exploratory data analysis, and dashboard development.

The datasets include information about mutual fund schemes, NAV history, SIP inflows, AUM, investor transactions, portfolio holdings, and benchmark indices. Through this project, the data is transformed into meaningful insights using Python, SQLite, SQL, and visualization libraries such as Matplotlib, Seaborn, and Plotly.

The objective is to build a complete end-to-end analytics project that demonstrates practical skills in data preprocessing, database management, exploratory data analysis, and business reporting.

## Technologies Used

- Python
- Pandas
- NumPy
- SQL
- SQLite
- SQLAlchemy
- Matplotlib
- Seaborn
- Plotly
- Jupyter Notebook
- Git & GitHub
- VS Code

----------------------------------------------------------------------------------------------------------------------------


# Day 1 – Project Setup & Data Ingestion

## Objective

The goal of Day 1 was to set up the project environment, organize the project structure, load the provided datasets, fetch live NAV data using an API, and perform an initial assessment of the data before starting the cleaning process.

## Work Completed

- Created the complete project folder structure for organizing datasets, notebooks, SQL scripts, reports, and dashboards.
- Set up the Python virtual environment and installed all required libraries.
- Generated the `requirements.txt` file for project dependencies.
- Loaded all provided CSV datasets using Pandas.
- Explored each dataset by checking its dimensions, column names, data types, and sample records.
- Fetched live NAV data from the MFAPI and saved it as raw CSV files.
- Retrieved NAV data for multiple mutual fund schemes for comparison.
- Explored the Fund Master dataset to understand fund houses, categories, sub-categories, and risk classifications.
- Validated AMFI scheme codes between datasets to check data consistency.
- Prepared a Data Quality Summary highlighting observations from the raw datasets.
- Initialized the Git repository and pushed the project to GitHub.

## Tools & Libraries Used

- Python
- Pandas
- Requests
- NumPy
- Jupyter Notebook
- Git & GitHub
- VS Code

## Files Created

- `data_ingestion.py`
- `live_nav_fetch.py`
- `requirements.txt`
- `data_quality_summary.txt`
- Project folder structure
- Raw NAV CSV files

## Outcome

Successfully completed the project setup and data ingestion process. All datasets were loaded successfully, the project environment was configured, live NAV data was collected, and the initial data quality assessment was completed. This prepared the project for data cleaning and database development in the next phase.


----------------------------------------------------------------------------------------------------------------------------

# Day 2 – Data Cleaning & SQLite Database Design

## Objective

The goal of Day 2 was to clean the raw mutual fund datasets, validate the data, and store the processed data in a structured SQLite database. The focus was on improving data quality, designing the database schema, and preparing the datasets for further analysis.

## Work Completed

- Cleaned the NAV history dataset by handling missing values, removing duplicates, sorting records, and validating NAV values.
- Cleaned the investor transactions dataset by standardizing transaction types, validating transaction amounts, correcting date formats, and checking KYC status values.
- Cleaned the scheme performance dataset by validating return values, checking expense ratio ranges, and identifying anomalies.
- Saved all cleaned datasets in the `data/processed` directory.
- Designed the SQLite database schema using SQL.
- Created database tables and loaded all cleaned datasets using SQLAlchemy.
- Verified that database row counts matched the source CSV files after loading.
- Wrote analytical SQL queries to extract business insights from the data.
- Created a data dictionary describing each dataset, its columns, data types, and business meaning.

## Tools & Libraries Used

- Python
- Pandas
- SQLAlchemy
- SQLite
- SQL
- Jupyter Notebook (for validation)
- VS Code

## Files Created

- `data_cleaning.py`
- `database_setup.py`
- `schema.sql`
- `queries.sql`
- `data_dictionary.md`
- `bluestock_mf.db`
- `data/processed/` (Cleaned datasets)

## Outcome

Successfully cleaned and validated all datasets, loaded them into a SQLite database, verified data integrity, and prepared the project for exploratory data analysis. The processed datasets and database are now ready for visualization and dashboard development in the next phase of the project.

----------------------------------------------------------------------------------------------------------------------------

# Day 3 – Exploratory Data Analysis (EDA)

## Objective

The goal of Day 3 was to perform Exploratory Data Analysis (EDA) on the cleaned mutual fund datasets and identify meaningful patterns using visualizations. Different charts were created to understand trends in NAV, SIP inflows, AUM growth, investor demographics, portfolio allocation, and overall market behaviour.

## Work Completed

- Created an EDA notebook (`EDA_Analysis.ipynb`) using Jupyter Notebook.
- Analysed daily NAV trends of all mutual fund schemes from 2022 to 2026.
- Visualized yearly AUM growth across different fund houses and highlighted SBI Mutual Fund's market leadership.
- Plotted monthly SIP inflows and marked the highest recorded SIP inflow.
- Created a heatmap to analyse category-wise monthly inflows.
- Analysed investor demographics using age group distribution, gender distribution, and SIP amount box plots.
- Compared SIP investments across different states and city tiers.
- Visualized mutual fund folio growth over the analysis period.
- Generated a correlation matrix to study relationships between selected mutual fund schemes.
- Analysed portfolio sector allocation using a donut chart.
- Documented key observations and insights for each visualization.

## Tools & Libraries Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Plotly
- Jupyter Notebook

## Files Created

- `notebooks/EDA_Analysis.ipynb`
- `outputs/charts/`
  - NAV Trend
  - AUM Growth
  - SBI AUM Dominance
  - SIP Inflow Trend
  - Category Inflow Heatmap
  - Age Group Distribution
  - SIP Amount Box Plot
  - Gender Distribution
  - SIP by State
  - T30 vs B30 Distribution
  - Folio Count Growth
  - NAV Return Correlation Matrix
  - Sector Allocation Donut

## Outcome

Successfully completed the exploratory analysis of the mutual fund datasets by creating multiple visualizations and identifying important trends related to investor behaviour, fund performance, SIP growth, portfolio allocation, and market patterns. The notebook and exported charts will be used for the final project report and dashboard development.


----------------------------------------------------------------------------------------------------------------------------

# Day 4 – Fund Performance Analytics

## Objective

The objective of Day 4 was to evaluate the performance of mutual fund schemes using key financial metrics and build a comprehensive fund scorecard. The analysis focused on daily return calculations, risk-adjusted performance, benchmark comparison, and ranking funds based on multiple performance indicators.

## Work Completed

* Created a Performance Analytics notebook (`Performance_Analytics.ipynb`) using Jupyter Notebook.
* Calculated daily returns for all mutual fund schemes using historical NAV data.
* Analysed the distribution of daily returns to validate return patterns.
* Explored key performance metrics, including 1-year, 3-year, and 5-year returns, Sharpe Ratio, Sortino Ratio, Alpha, Beta, Maximum Drawdown, and Expense Ratio.
* Built a weighted Fund Scorecard by ranking schemes using return, risk-adjusted performance, expense ratio, and downside risk metrics.
* Exported the complete Fund Scorecard for further analysis and reporting.
* Extracted and exported Alpha and Beta values for all mutual fund schemes.
* Created an Alpha vs Beta scatter plot to visualize fund performance relative to market risk.
* Compared the top-performing mutual funds against the NIFTY100 benchmark using a benchmark comparison chart.
* Documented observations and key insights for each analysis and visualization.

## Tools & Libraries Used

* Python
* Pandas
* NumPy
* Matplotlib
* SciPy
* Jupyter Notebook

## Files Created

* `notebooks/Performance_Analytics.ipynb`
* `outputs/fund_scorecard.csv`
* `outputs/alpha_beta.csv`
* `outputs/charts/`

  * Daily Return Distribution
  * Alpha vs Beta Scatter Plot
  * Top 10 Fund Score
  * Benchmark Comparison

## Outcome

Successfully completed the performance analytics phase by evaluating mutual fund schemes using multiple financial and risk-adjusted performance metrics. A comprehensive fund scorecard was developed to rank schemes based on return, risk, expense ratio, and downside protection. The generated visualizations and exported datasets provide meaningful insights into fund performance and serve as a foundation for the final project report and dashboard development.

----------------------------------------------------------------------------------------------------------------------------

# Day 5 – Power BI Dashboard Development

## Objective

The objective of Day 5 was to build an interactive Power BI dashboard using the processed mutual fund datasets and present key insights through dynamic visualizations. The dashboard focused on industry performance, fund analysis, investor behavior, and SIP market trends to provide an interactive business intelligence solution.

## Work Completed
* Imported all cleaned mutual fund datasets into Power BI Desktop.
* Established relationships between datasets using amfi_code and other relevant fields.
* Designed a four-page interactive dashboard to analyze different aspects of the mutual fund industry.
* Created KPI cards displaying Total AUM, Total SIP Inflows, Total Folios, and Total Schemes.
* Built an Industry Overview dashboard featuring industry AUM trends and fund house-wise AUM distribution.
* Developed a Fund Performance dashboard with Return vs Risk analysis, Fund Performance Scorecard, historical NAV trend,   and interactive slicers.
* Created an Investor Analytics dashboard to analyse transaction amount by state, SIP amount across age groups, transaction type distribution, and KYC status.
* Developed a SIP & Market Trends dashboard including Monthly SIP Inflow Trend, NIFTY 50 Market Trend, Category Inflow Heatmap, and Top 5 Categories by Net Inflow.
* Added interactive slicers to enable filtering by fund house, category, plan, state, age group, and city tier.
Organized dashboard visuals with consistent formatting, titles, and layouts for improved readability and user experience.

## Tools & Technologies Used
* Power BI Desktop
* Power Query
* DAX (Basic Measures)
* CSV Data Sources
* Interactive Visualizations
* Filters & Slicers
* Files Created
* bluestock_mf_dashboard.pbix
* Dashboard.pdf
* outputs/dashboard_screenshots/
* Industry Overview
* Fund Performance
* Investor Analytics
* SIP & Market Trends

## Outcome

Successfully developed a four-page interactive Power BI dashboard that provides comprehensive insights into mutual fund industry performance, fund analytics, investor behavior, and SIP market trends. The dashboard enables users to explore data using interactive filters and visualizations, making it easier to analyse performance, compare schemes, and support data-driven decision-making. The completed dashboard serves as the final visualization component of the Mutual Fund Data Analytics project.

## Dashboard Preview

### Industry Overview

![Industry Overview](outputs/dashboard_screenshots/mutual_fund_industry_overview.png)

### Fund Performance Dashboard

![Fund Performance Dashboard](outputs/dashboard_screenshots/mutual_fund_performance_dashboard.png)

### Investor Analytics Dashboard

![Investor Analytics Dashboard](outputs/dashboard_screenshots/investor_analytics_dashboard.png)

### SIP & Market Trends Dashboard

![SIP & Market Trends Dashboard](outputs/dashboard_screenshots/SIP_&_market_trends_dashboard.png)

----------------------------------------------------------------------------------------------------------------------------
