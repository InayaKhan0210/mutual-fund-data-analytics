import pandas as pd
from pathlib import Path

raw_path = Path("data/raw")
processed_path = Path("data/processed")
processed_path.mkdir(parents=True, exist_ok=True)

# Load datasets
nav_history = pd.read_csv(raw_path / "02_nav_history.csv")
transactions = pd.read_csv(raw_path / "08_investor_transactions.csv")
performance = pd.read_csv(raw_path / "07_scheme_performance.csv")

# -----------------------------
# Clean nav_history
# -----------------------------
nav_history["date"] = pd.to_datetime(nav_history["date"], errors="coerce")
nav_history["nav"] = pd.to_numeric(nav_history["nav"], errors="coerce")

nav_history = nav_history.drop_duplicates()
nav_history = nav_history.sort_values(["amfi_code", "date"])
nav_history["nav"] = nav_history.groupby("amfi_code")["nav"].ffill()
nav_history = nav_history[nav_history["nav"] > 0]

nav_history.to_csv(processed_path / "02_nav_history_cleaned.csv", index=False)

# -----------------------------
# Clean investor_transactions
# -----------------------------
transactions["transaction_date"] = pd.to_datetime(
    transactions["transaction_date"], errors="coerce"
)

transactions["amount_inr"] = pd.to_numeric(transactions["amount_inr"], errors="coerce")
transactions = transactions[transactions["amount_inr"] > 0]

transactions["transaction_type"] = (
    transactions["transaction_type"]
    .astype(str)
    .str.strip()
    .str.lower()
)

type_map = {
    "sip": "SIP",
    "lumpsum": "Lumpsum",
    "lump sum": "Lumpsum",
    "redemption": "Redemption",
    "redeem": "Redemption",
}

transactions["transaction_type"] = transactions["transaction_type"].map(type_map)

transactions = transactions.dropna(subset=["transaction_type"])

transactions.to_csv(processed_path / "08_investor_transactions_cleaned.csv", index=False)

# -----------------------------
# Clean scheme_performance
# -----------------------------
performance = performance.drop_duplicates()

for col in performance.columns:
    if "return" in col.lower() or "expense" in col.lower():
        performance[col] = pd.to_numeric(performance[col], errors="coerce")

if "expense_ratio_pct" in performance.columns:
    performance["expense_ratio_anomaly"] = ~performance["expense_ratio_pct"].between(0.1, 2.5)

performance.to_csv(processed_path / "07_scheme_performance_cleaned.csv", index=False)

# -----------------------------
# Copy remaining CSVs as cleaned versions
# -----------------------------
for file in raw_path.glob("*.csv"):
    if file.name not in [
        "02_nav_history.csv",
        "08_investor_transactions.csv",
        "07_scheme_performance.csv",
    ]:
        df = pd.read_csv(file)
        df = df.drop_duplicates()
        output_name = file.stem + "_cleaned.csv"
        df.to_csv(processed_path / output_name, index=False)

print("Data cleaning completed. Cleaned files saved in data/processed/")