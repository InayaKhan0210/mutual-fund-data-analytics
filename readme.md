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