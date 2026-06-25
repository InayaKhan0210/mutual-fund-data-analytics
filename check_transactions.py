import pandas as pd

transactions = pd.read_csv("data/raw/08_investor_transactions.csv")

print("Investor Transactions Columns:")
print(transactions.columns)

print("\nFirst 5 rows:")
print(transactions.head())