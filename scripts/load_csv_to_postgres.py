import os
import re
import pandas as pd
from sqlalchemy import create_engine, text


RAW_DATA_PATH = "data/raw"

DB_USER = "nuclear_user"
DB_PASSWORD = "nuclear_password"
DB_HOST = "localhost"
DB_PORT = "5434"
DB_NAME = "nuclear_source"

engine = create_engine(
    f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)


def clean_name(name: str) -> str:
    name = name.lower()
    name = re.sub(r"[^a-z0-9]+", "_", name)
    name = name.strip("_")
    return name


def load_csv(file_path: str):
    file_name = os.path.basename(file_path)
    table_name = clean_name(file_name.replace(".csv", ""))

    print(f"Loading {file_name} -> raw.{table_name}")

    df = pd.read_csv(file_path)

    df.columns = [clean_name(col) for col in df.columns]

    with engine.begin() as conn:
        conn.execute(text("CREATE SCHEMA IF NOT EXISTS raw;"))

    df.to_sql(
        table_name,
        engine,
        schema="raw",
        if_exists="replace",
        index=False
    )

    print(f"Loaded {len(df)} rows into raw.{table_name}")


def main():
    csv_files = [
        os.path.join(RAW_DATA_PATH, file)
        for file in os.listdir(RAW_DATA_PATH)
        if file.endswith(".csv")
    ]

    for csv_file in csv_files:
        load_csv(csv_file)

    print("All CSV files loaded into PostgreSQL.")


if __name__ == "__main__":
    main()