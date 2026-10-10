from pathlib import Path

import pandas as pd


# Project paths
PROJECT_ROOT = Path(__file__).resolve().parents[2]
SOURCE_FILE = PROJECT_ROOT / "data" / "raw" / "wind_power_data.csv"
BRONZE_DIR = PROJECT_ROOT / "data" / "bronze" / "wind_power_data"
OUTPUT_FILE = BRONZE_DIR / "wind_power_data.parquet"


def ingest_bronze() -> None:
    """Ingest the source CSV into a local Bronze Parquet dataset."""

    # 1. Check that the source file exists.
    if not SOURCE_FILE.exists():
        raise FileNotFoundError(
            f"Source dataset not found: {SOURCE_FILE}"
        )

    # 2. Read the source dataset.
    source_df = pd.read_csv(SOURCE_FILE)

    # 3. Create the Bronze output directory.
    BRONZE_DIR.mkdir(parents=True, exist_ok=True)

    # 4. Write the source data to Parquet.
    source_df.to_parquet(OUTPUT_FILE, index=False)

    # 5. Read the written dataset to validate the output.
    bronze_df = pd.read_parquet(OUTPUT_FILE)

    # 6. Validate the number of rows.
    if len(source_df) != len(bronze_df):
        raise ValueError(
            f"Row count mismatch: source={len(source_df)}, "
            f"bronze={len(bronze_df)}"
        )

    # 7. Validate the column names and order.
    if source_df.columns.tolist() != bronze_df.columns.tolist():
        raise ValueError("Column names or order do not match.")

    # 8. Validate the data after the round trip.
    if not source_df.equals(bronze_df):
        raise ValueError(
            "Data validation failed: source and Bronze data differ."
        )

    # 9. Print the ingestion summary.
    print("Bronze ingestion completed successfully.")
    print(f"Source file: {SOURCE_FILE}")
    print(f"Output file: {OUTPUT_FILE}")
    print(f"Rows ingested: {len(bronze_df)}")
    print(f"Columns ingested: {len(bronze_df.columns)}")
    print("Validation: row count, columns and values are identical.")


if __name__ == "__main__":
    ingest_bronze()