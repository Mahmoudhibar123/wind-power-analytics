from pathlib import Path

import pandas as pd


# 1. Locate the project root.
PROJECT_ROOT = Path(__file__).resolve().parents[2]

# 2. Define the raw dataset path.
DATA_PATH = PROJECT_ROOT / "data" / "raw" / "wind_power_data.csv"


def main():
    """Profile the raw wind power dataset."""

    # 3. Load the dataset.
    if not DATA_PATH.exists():
        raise FileNotFoundError(f"Dataset not found: {DATA_PATH}")

    df = pd.read_csv(DATA_PATH)

    print("=" * 60)
    print("WIND POWER ANALYTICS - DATA PROFILING")
    print("=" * 60)

    # 4. Inspect dataset dimensions.
    print("\n1. DATASET DIMENSIONS")
    print(f"Rows: {df.shape[0]}")
    print(f"Columns: {df.shape[1]}")

    # 5. Inspect column types.
    print("\n2. COLUMN TYPES")
    print(df.dtypes.to_string())

    # 6. Check missing values.
    print("\n3. MISSING VALUES")
    missing = df.isna().sum()
    print(missing.to_string())

    print(f"\nTotal missing cells: {missing.sum()}")

    # 7. Check duplicate records.
    print("\n4. DUPLICATE RECORDS")
    print(f"Fully duplicated rows: {df.duplicated().sum()}")

    # 8. Check production identifiers.
    print("\n5. PRODUCTION ID CHECK")

    if "production_id" in df.columns:
        print(f"Unique IDs: {df['production_id'].nunique()}")
        print(f"Duplicate IDs: {df['production_id'].duplicated().sum()}")
        print(f"Missing IDs: {df['production_id'].isna().sum()}")

    # 9. Inspect turbines and statuses.
    print("\n6. TURBINE DISTRIBUTION")
    print(df["turbine_name"].value_counts(dropna=False).to_string())

    print("\n7. STATUS DISTRIBUTION")
    print(df["status"].value_counts(dropna=False).to_string())

    # 10. Analyze dates and timestamps.
    print("\n8. DATE AND TIME ANALYSIS")

    df["timestamp"] = pd.to_datetime(
        df["date"].astype(str) + " " + df["time"].astype(str),
        format="%Y-%m-%d %H-%M-%S",
        errors="coerce",
    )

    print(f"Invalid timestamps: {df['timestamp'].isna().sum()}")
    print(f"Earliest timestamp: {df['timestamp'].min()}")
    print(f"Latest timestamp: {df['timestamp'].max()}")

    print(
        "Duplicate timestamps per turbine:",
        df.duplicated(subset=["timestamp", "turbine_name"]).sum(),
    )

    # 11. Inspect numeric statistics.
    print("\n9. NUMERIC STATISTICS")
    print(df[["capacity", "wind_speed", "energy_produced"]].describe().to_string())

    # 12. Inspect categorical values.
    print("\n10. WIND DIRECTIONS")
    print(df["wind_direction"].value_counts(dropna=False).to_string())

    print("\n11. LOCATION DISTRIBUTION")
    print(df["location_name"].value_counts(dropna=False).to_string())

    # 12. Check turbine-to-location mapping.
    print("\n12. TURBINE AND LOCATION MAPPING")

    print(
        df.groupby("turbine_name")["location_name"]
        .nunique()
        .to_string()
    )

    # 13. Check capacity consistency.
    print("\n13. CAPACITY PER TURBINE")

    print(
        df.groupby("turbine_name")["capacity"]
        .agg(["min", "max", "nunique"])
        .to_string()
    )

    # 14. Check missing measurement timestamps.
    print("\n14. MISSING MEASUREMENT INTERVALS")

    expected_timestamps = pd.date_range(
        start=df["timestamp"].min(),
        end=df["timestamp"].max(),
        freq="10min",
    )

    for turbine in sorted(df["turbine_name"].dropna().unique()):
        actual_timestamps = pd.DatetimeIndex(
            df.loc[df["turbine_name"] == turbine, "timestamp"]
        )

        missing_timestamps = expected_timestamps.difference(
            actual_timestamps
        )

        print(
            f"{turbine}: "
            f"{len(missing_timestamps)} missing intervals"
        )

    # 15. Analyze zero energy by status.
    print("\n15. ZERO ENERGY BY STATUS")

    zero_energy = df[df["energy_produced"] == 0]

    print(f"Records with zero energy: {len(zero_energy)}")

    print(
        zero_energy["status"]
        .value_counts(dropna=False)
        .to_string()
    )


    # 16. Validate energy production against turbine status.
    print("\n16. STATUS AND ENERGY CONSISTENCY")

    online_with_zero_energy = df[
        (df["status"] == "Online")
        & (df["energy_produced"] == 0)
    ]

    non_online_with_positive_energy = df[
        (df["status"] != "Online")
        & (df["energy_produced"] > 0)
    ]

    negative_energy = df[df["energy_produced"] < 0]

    negative_wind_speed = df[df["wind_speed"] < 0]

    print(
        "Online records with zero energy:",
        len(online_with_zero_energy),
    )

    print(
        "Non-online records with positive energy:",
        len(non_online_with_positive_energy),
    )

    print("Records with negative energy:", len(negative_energy))

    print("Records with negative wind speed:", len(negative_wind_speed))

    print("\n" + "=" * 60)
    print("PROFILING COMPLETED")
    print("=" * 60)


if __name__ == "__main__":
    main()
