from pyspark.sql import DataFrame
from pyspark.sql import functions as F


def run_quality_checks(df: DataFrame) -> DataFrame:
    """
    Execute data quality checks on a Spark DataFrame.

    Returns one result per rule with:
    - rule_id
    - rule_description
    - invalid_records
    - result
    - execution_timestamp
    """

    allowed_statuses = [
        "Online",
        "Offline",
        "Preventive Maintenance",
        "Reactive Maintenance",
        "Fault",
        "Inspection",
    ]

    # DQ-01: production_id must not be null
    missing_id_count = df.filter(
        F.col("production_id").isNull()
    ).count()

    # DQ-02: production_id must be unique
    duplicate_id_count = (
        df.groupBy("production_id")
        .count()
        .filter(F.col("count") > 1)
        .count()
    )

    # DQ-03: turbine_name must not be null or empty
    missing_turbine_count = df.filter(
        F.col("turbine_name").isNull()
        | (F.trim(F.col("turbine_name")) == "")
    ).count()

    # DQ-04: energy_produced must be non-negative
    negative_energy_count = df.filter(
        F.col("energy_produced") < 0
    ).count()

    # DQ-05: wind_speed must be non-negative
    negative_wind_speed_count = df.filter(
        F.col("wind_speed") < 0
    ).count()

    # DQ-06: status must belong to the allowed list
    invalid_status_count = df.filter(
        F.col("status").isNull()
        | (~F.col("status").isin(allowed_statuses))
    ).count()

    # DQ-07: measurement_timestamp must not be null
    missing_timestamp_count = df.filter(
        F.col("measurement_timestamp").isNull()
    ).count()

    # DQ-08: turbine_name + measurement_timestamp must be unique
    duplicate_measurement_count = (
        df.groupBy("turbine_name", "measurement_timestamp")
        .count()
        .filter(F.col("count") > 1)
        .count()
    )

    rules = [
        (
            "DQ-01",
            "production_id must not be null",
            missing_id_count,
        ),
        (
            "DQ-02",
            "production_id must be unique",
            duplicate_id_count,
        ),
        (
            "DQ-03",
            "turbine_name must not be null or empty",
            missing_turbine_count,
        ),
        (
            "DQ-04",
            "energy_produced must be non-negative",
            negative_energy_count,
        ),
        (
            "DQ-05",
            "wind_speed must be non-negative",
            negative_wind_speed_count,
        ),
        (
            "DQ-06",
            "status must belong to the allowed list",
            invalid_status_count,
        ),
        (
            "DQ-07",
            "measurement_timestamp must not be null",
            missing_timestamp_count,
        ),
        (
            "DQ-08",
            "turbine_name + measurement_timestamp must be unique",
            duplicate_measurement_count,
        ),
    ]

    results = [
        (
            rule_id,
            description,
            int(invalid_records),
            "PASS" if invalid_records == 0 else "FAIL",
        )
        for rule_id, description, invalid_records in rules
    ]

    quality_schema = """
        rule_id STRING,
        rule_description STRING,
        invalid_records LONG,
        result STRING
    """

    quality_df = df.sparkSession.createDataFrame(
        results,
        schema=quality_schema,
    )

    return quality_df.withColumn(
        "execution_timestamp",
        F.current_timestamp(),
    )
