# Wind Power Analytics — Data Catalog

## 1. Purpose

This document describes the datasets used in the Wind Power Analytics
project, including their structure, business meaning, origin, and role
in the data pipeline.

The project follows the Medallion Architecture:
Bronze → Silver → Gold.

## 2. Data Sources

| Property | Description |
|---|---|
| Source file | `wind_power_data.csv` |
| Source format | CSV |
| Local path | `data/raw/wind_power_data.csv` |
| Initial records | 6,048 |
| Initial columns | 14 |
| Observation period | June 1–14, 2024 |
| Turbines | Turbine A, Turbine B, Turbine C |

The physical units of capacity, wind speed, and energy production
have not yet been confirmed.

## 3. Dataset Inventory

| Table | Layer | Description |
|---|---|---|
| `workspace.default.bronze_wind_power` | Bronze | Ingested source data |
| `workspace.default.silver_wind_power` | Silver | Transformed data enriched with a measurement timestamp |
| `workspace.default.gold_daily_production` | Gold | Daily production metrics by turbine |
| `workspace.default.gold_turbine_performance` | Gold | Aggregated performance metrics by turbine |

## 4. Bronze Layer

**Table:** `workspace.default.bronze_wind_power`

**Purpose:** Store the ingested source data in Delta format.

| Column | Type | Description |
|---|---|---|
| `production_id` | integer | Production record identifier |
| `date` | date | Measurement date |
| `time` | string | Measurement time |
| `turbine_name` | string | Turbine identifier |
| `capacity` | integer | Recorded turbine capacity |
| `location_name` | string | Location identifier |
| `latitude` | double | Geographic latitude |
| `longitude` | double | Geographic longitude |
| `region` | string | Region identifier |
| `status` | string | Turbine operating status |
| `responsible_department` | string | Responsible department |
| `wind_speed` | double | Recorded wind speed |
| `wind_direction` | string | Wind direction |
| `energy_produced` | double | Recorded energy production |

## 5. Silver Layer

**Table:** `workspace.default.silver_wind_power`

**Purpose:** Provide transformed and validated measurement data.

The Silver table contains the 14 Bronze columns and an additional
`measurement_timestamp` column.

| Column | Type | Description |
|---|---|---|
| `measurement_timestamp` | timestamp | Combined measurement date and time |

The transformation logic and data quality checks are implemented
in the Silver processing notebook.

## 6. Gold Layer — Daily Production

**Table:** `workspace.default.gold_daily_production`

**Purpose:** Support daily production analysis for each turbine.

| Column | Type | Description |
|---|---|---|
| `date` | date | Production date |
| `turbine_name` | string | Turbine identifier |
| `total_energy_produced` | double | Sum of recorded energy production |
| `avg_wind_speed` | double | Average recorded wind speed |
| `total_measurements` | long | Total number of measurements |
| `online_measurements` | long | Number of Online measurements |
| `offline_measurements` | long | Number of Offline measurements |
| `online_measurement_pct` | double | Percentage of measurements with Online status |

**Expected grain:** One row per date and turbine.

## 7. Gold Layer — Turbine Performance

**Table:** `workspace.default.gold_turbine_performance`

**Purpose:** Compare aggregated performance across turbines.

| Column | Type | Description |
|---|---|---|
| `turbine_name` | string | Turbine identifier |
| `total_energy_produced` | double | Total recorded energy production |
| `avg_wind_speed` | double | Average recorded wind speed |
| `total_measurements` | long | Total number of measurements |
| `online_measurements` | long | Number of Online measurements |
| `offline_measurements` | long | Number of Offline measurements |
| `online_measurement_pct` | double | Percentage of measurements with Online status |

**Expected grain:** One row per turbine.

## 8. Initial Data Quality Findings

The initial source-data profiling identified:

- No missing values.
- No fully duplicated rows.
- No duplicate production identifiers.
- No missing production identifiers.
- No negative energy production values.
- No negative wind speed values.

These findings apply to the initial dataset and must not be
interpreted as a guarantee of future data quality.

## 9. Data Lineage

The high-level data flow is:

`wind_power_data.csv`
→ `bronze_wind_power`
→ `silver_wind_power`
→ Gold analytical tables
→ Power BI

The Gold tables provide aggregated datasets for reporting and analysis.

## 10. Governance Improvements

Planned improvements include:

- Documenting data ownership and responsibilities.
- Formalizing data quality rules.
- Tracking pipeline execution and failures.
- Documenting access permissions.
- Implementing automated data quality checks.
- Evaluating Unity Catalog capabilities.
