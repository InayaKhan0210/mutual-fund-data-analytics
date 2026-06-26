import pandas as pd
from sqlalchemy import create_engine, text
from pathlib import Path

processed_path = Path("data/processed")

engine = create_engine("sqlite:///bluestock_mf.db")

with open("schema.sql", "r") as file:
    schema_sql = file.read()

with engine.connect() as conn:
    for statement in schema_sql.split(";"):
        if statement.strip():
            conn.execute(text(statement))
    conn.commit()

print("Schema created successfully.")

for file in processed_path.glob("*.csv"):
    df = pd.read_csv(file)
    table_name = file.stem.replace("_cleaned", "")
    df.to_sql(table_name, engine, if_exists="replace", index=False)
    print(f"Loaded table: {table_name} | Rows: {len(df)}")

print("Database setup completed successfully.")

print("\nVerifying row counts...\n")

for file in processed_path.glob("*.csv"):
    df = pd.read_csv(file)

    table_name = file.stem.replace("_cleaned", "")

    db_count = pd.read_sql(
        f'SELECT COUNT(*) AS total FROM "{table_name}"',
        engine
    ).iloc[0]["total"]

    csv_count = len(df)

    status = "MATCH" if csv_count == db_count else "MISMATCH"

    print(f"{table_name}: CSV={csv_count}, DB={db_count} --> {status}")