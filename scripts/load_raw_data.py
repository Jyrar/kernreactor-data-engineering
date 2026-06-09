import os
import re
from pathlib import Path

import pandas as pd
from sqlalchemy import create_engine, text
from sqlalchemy.engine import Engine


def clean_name(name: str) -> str:
    name = name.lower()
    name = re.sub(r"[^a-z0-9]+", "_", name)
    return name.strip("_")


def build_engine(
    db_uri: str | None = None,
    *,
    user: str = "nuclear_user",
    password: str = "nuclear_password",
    host: str = "localhost",
    port: str = "5434",
    database: str = "nuclear_source",
) -> Engine:
    if db_uri:
        return create_engine(db_uri)
    return create_engine(
        f"postgresql+psycopg2://{user}:{password}@{host}:{port}/{database}"
    )


def load_csv(file_path: str, engine: Engine) -> int:
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
        index=False,
    )

    print(f"Loaded {len(df)} rows into raw.{table_name}")
    return len(df)


def load_all_csvs(raw_data_path: str, engine: Engine | None = None, db_uri: str | None = None) -> list[str]:
    data_dir = Path(raw_data_path)
    if not data_dir.is_dir():
        raise FileNotFoundError(f"Raw data directory not found: {data_dir}")

    csv_files = sorted(data_dir.glob("*.csv"))
    if not csv_files:
        raise FileNotFoundError(f"No CSV files found in {data_dir}")

    db_engine = engine or build_engine(db_uri=db_uri)
    loaded_tables = []

    for csv_file in csv_files:
        load_csv(str(csv_file), db_engine)
        loaded_tables.append(csv_file.stem)

    print(f"Loaded {len(loaded_tables)} CSV files into PostgreSQL.")
    return loaded_tables
