# Wind Power Analytics

## 1. Project Overview

Wind Power Analytics is a Data Engineering learning project focused on
analyzing wind turbine production data.

The objective is to build a data pipeline that ingests raw data, validates
and transforms it, and prepares reliable datasets for analytics and reporting.

The project will progressively use Python, pandas, Azure Databricks,
PySpark, and Power BI.

The pipeline will follow the Medallion Architecture:

- Bronze: raw data ingestion.
- Silver: data cleaning, validation, and transformation.
- Gold: business-oriented datasets and analytical metrics.
- Reporting: visualization and analysis with Power BI.

The project is being developed step by step, starting with local Python
processing before introducing cloud technologies.

## 2. Business Objectives

The project aims to:

- Analyze wind turbine production.
- Monitor production across turbines and locations.
- Understand the relationship between wind conditions and energy production.
- Identify potential data quality issues.
- Build reliable datasets for reporting.
- Practice Data Engineering concepts using a realistic workflow.

## 3. Dataset

The initial dataset is a CSV file named `wind_power_data.csv`.

Expected local location:

`data/raw/wind_power_data.csv`

### Dataset characteristics

- Number of records: 6,048
- Number of columns: 14
- Observation period: June 1–14, 2024
- Turbines: Turbine A, Turbine B, Turbine C
- Measurement frequency: every 10 minutes

### Main columns

| Column | Description |
|---|---|
| `production_id` | Production record identifier |
| `date` | Measurement date |
| `time` | Measurement time |
| `turbine_name` | Turbine identifier |
| `capacity` | Recorded turbine capacity |
| `location_name` | Location identifier |
| `latitude` | Geographic latitude |
| `longitude` | Geographic longitude |
| `region` | Region identifier |
| `status` | Turbine operating status |
| `responsible_department` | Responsible department |
| `wind_speed` | Recorded wind speed |
| `wind_direction` | Wind direction |
| `energy_produced` | Recorded energy production |

The physical units of capacity, wind speed, and energy production
have not yet been confirmed.

## 4. Technologies

### Currently used

- Python 3.10
- pandas
- Git
- GitHub
- Ubuntu Linux

### Planned technologies

- Microsoft Azure
- Azure Databricks
- Apache Spark / PySpark
- Delta Lake
- Power BI

## 5. Project Structure

```text
wind-power-analytics/
├── README.md
├── .gitignore
├── data/
│   └── raw/
│       └── wind_power_data.csv
└── src/
    └── wind_power/
        └── profile_data.py
