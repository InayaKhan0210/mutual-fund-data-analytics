# Data Dictionary

## 01_fund_master.csv

| Column | Data Type | Business Meaning |
|---|---|---|
| amfi_code | Integer | Unique AMFI scheme code |
| fund_house | Text | Mutual fund company / AMC |
| scheme_name | Text | Name of mutual fund scheme |
| category | Text | Main fund category |
| sub_category | Text | Fund sub-category |
| plan | Text | Plan type |
| launch_date | Date | Scheme launch date |
| benchmark | Text | Benchmark index |
| expense_ratio_pct | Float | Annual expense ratio percentage |
| exit_load_pct | Float | Exit load percentage |
| min_sip_amount | Float | Minimum SIP investment |
| min_lumpsum_amount | Float | Minimum lumpsum investment |
| fund_manager | Text | Fund manager name |
| risk_category | Text | Risk level |
| sebi_category_code | Text | SEBI category code |

## 02_nav_history.csv

| Column | Data Type | Business Meaning |
|---|---|---|
| amfi_code | Integer | Mutual fund scheme code |
| date | Date | NAV date |
| nav | Float | Net Asset Value |

## 03_aum_by_fund_house.csv

| Column | Data Type | Business Meaning |
|---|---|---|
| date | Date | Reporting date |
| fund_house | Text | AMC / fund house |
| aum_lakh_crore | Float | AUM in lakh crore |
| aum_crore | Float | AUM in crore |
| num_schemes | Integer | Number of schemes |

## 07_scheme_performance.csv

| Column | Data Type | Business Meaning |
|---|---|---|
| amfi_code | Integer | Mutual fund scheme code |
| scheme_name | Text | Scheme name |
| return_1yr_pct | Float | One-year return percentage |
| return_3yr_pct | Float | Three-year return percentage |
| return_5yr_pct | Float | Five-year return percentage |
| expense_ratio_pct | Float | Expense ratio percentage |
| aum_crore | Float | Assets under management |
| risk_grade | Text | Risk grade |

## 08_investor_transactions.csv

| Column | Data Type | Business Meaning |
|---|---|---|
| investor_id | Text | Unique investor ID |
| transaction_date | Date | Date of transaction |
| amfi_code | Integer | Scheme code |
| transaction_type | Text | SIP, Lumpsum, or Redemption |
| amount_inr | Float | Transaction amount in INR |
| state | Text | Investor state |
| city | Text | Investor city |
| city_tier | Text | City tier classification |
| age_group | Text | Investor age group |
| gender | Text | Investor gender |
| annual_income_lakh | Float | Annual income in lakh |
| payment_mode | Text | Payment method |
| kyc_status | Text | KYC verification status |

## Source References

Raw datasets are stored in `data/raw/`.

Cleaned datasets are stored in `data/processed/`.

SQLite database file: `bluestock_mf.db`.