import os
import sys

sys.path.insert(0, os.path.dirname(__file__))

from load_raw_data import build_engine, load_all_csvs


RAW_DATA_PATH = os.environ.get("RAW_DATA_PATH", os.path.join("..", "data"))

DB_USER = os.environ.get("DB_USER", "nuclear_user")
DB_PASSWORD = os.environ.get("DB_PASSWORD", "nuclear_password")
DB_HOST = os.environ.get("DB_HOST", "localhost")
DB_PORT = os.environ.get("DB_PORT", "5434")
DB_NAME = os.environ.get("DB_NAME", "nuclear_source")


def main() -> None:
    engine = build_engine(
        user=DB_USER,
        password=DB_PASSWORD,
        host=DB_HOST,
        port=DB_PORT,
        database=DB_NAME,
    )
    load_all_csvs(RAW_DATA_PATH, engine=engine)


if __name__ == "__main__":
    main()
