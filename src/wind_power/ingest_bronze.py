from pathlib import Path

import pandas as pd


# Project paths
PROJECT_ROOT = Path(__file__).resolve().parents[2]
SOURCE_FILE = PROJECT_ROOT / "data" / "raw" / "wind_power_data.csv"
BRONZE_DIR = PROJECT_ROOT / "data" / "bronze" / "wind_power_data"


def ingest_bronze() -> None:
    """Read the source CSV and write a local Bronze dataset in Parquet format."""

    # 1. Check that the source file exists.
    if not SOURCE_FILE.exists():
        raise FileNotFoundError(
            f"Source dataset not found: {SOURCE_FILE}"
        )

    # 2. Read the source dataset.
    df = pd.read_csv(SOURCE_FILE)

    # 3. Create the Bronze output directory.
    BRONZE_DIR.mkdir(parents=True, exist_ok=True)

    # 4. Write the dataset to Parquet.
    output_file = BRONZE_DIR / "wind_power_data.parquet"
    df.to_parquet(output_file, index=False)

    # 5. Print a summary of the ingestion.
    print("Bronze ingestion completed successfully.")
    print(f"Source file: {SOURCE_FILE}")
    print(f"Output file: {output_file}")
    print(f"Rows ingested: {len(df)}")
    print(f"Columns ingested: {len(df.columns)}")


if __name__ == "__main__":
    ingest_bronze()
