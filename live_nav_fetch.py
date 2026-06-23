import requests
import pandas as pd
from pathlib import Path

# Create raw folder if it doesn't exist
Path("data/raw").mkdir(parents=True, exist_ok=True)

schemes = {
    "HDFC_Top_100_Direct": 125497,
    "SBI_Bluechip": 119551,
    "ICICI_Bluechip": 120503,
    "Nippon_Large_Cap": 118632,
    "Axis_Bluechip": 119092,
    "Kotak_Bluechip": 120841,
}

for scheme_name, scheme_code in schemes.items():
    url = f"https://api.mfapi.in/mf/{scheme_code}"

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()

        nav_data = data.get("data", [])

        df = pd.DataFrame(nav_data)

        output_file = f"data/raw/{scheme_name}_nav.csv"

        df.to_csv(output_file, index=False)

        print(f"Saved: {output_file}")
        print(f"Rows: {len(df)}")
        print("-" * 50)

    else:
        print(f"Failed for {scheme_name}")