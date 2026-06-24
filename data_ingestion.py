import pandas as pd
from pathlib import Path

raw_folder = Path("data/raw")
csv_files = list(raw_folder.glob("*.csv"))

print(f"Total CSV files found: {len(csv_files)}")

for file in csv_files:
    print("\n" + "=" * 80)
    print(f"FILE: {file.name}")

    df = pd.read_csv(file)

    print("Shape:", df.shape)
    print("\nData Types:")
    print(df.dtypes)

    print("\nFirst 5 Rows:")
    print(df.head())

    print("\nMissing Values:")
    print(df.isnull().sum())

    print("\nDuplicate Rows:", df.duplicated().sum())

    print("\n" + "=" * 80)
print("FUND MASTER EXPLORATION")

fund_master = pd.read_csv("data/raw/01_fund_master.csv")
nav_history = pd.read_csv("data/raw/02_nav_history.csv")

print("\nUnique Fund Houses:")
print(fund_master["fund_house"].unique())

print("\nCategories:")
print(fund_master["category"].unique())

print("\nSub Categories:")
print(fund_master["sub_category"].unique())

print("\nRisk Categories:")
print(fund_master["risk_category"].unique())

print("\n" + "=" * 80)
print("AMFI CODE VALIDATION")

master_codes = set(fund_master["amfi_code"].dropna().astype(str))
nav_codes = set(nav_history["amfi_code"].dropna().astype(str))

missing_codes = master_codes - nav_codes

print("Total AMFI codes in fund_master:", len(master_codes))
print("Total AMFI codes in nav_history:", len(nav_codes))
print("Missing AMFI codes in nav_history:", len(missing_codes))

if missing_codes:
    print("Missing codes:")
    print(missing_codes)
else:
    print("All AMFI codes from fund_master exist in nav_history.")