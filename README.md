# Wind Power Analytics

## 1. Project Overview

Wind Power Analytics is a hands-on Data Engineering learning project
focused on analyzing wind turbine production data.

The objective is to build an end-to-end data pipeline that ingests raw data,
validates and transforms it, and produces reliable datasets for analytics,
reporting, and future Machine Learning applications.

The project uses Python, pandas, Microsoft Azure Databricks, PySpark,
Delta Lake, Git, GitHub, and Power BI.

The data pipeline follows the Medallion Architecture:

- **Bronze:** ingestion of raw data into a Delta table.
- **Silver:** data cleaning, validation, quality checks, and transformation.
- **Gold:** business-oriented aggregations and analytical metrics.
- **Reporting:** visualization and analysis using Power BI.

The project is developed incrementally, with an emphasis on understanding
Data Engineering concepts, implementing best practices, and preparing for
the Databricks Certified Data Engineer Associate certification.

## 2. Business Objectives

The project aims to:

- Analyze wind turbine energy production.
- Compare production performance across turbines.
- Monitor turbine operating status.
- Understand the relationship between wind conditions and energy production.
- Identify potential data quality issues.
- Build reliable analytical datasets.
- Develop an interactive Power BI dashboard.
- Explore future applications of Machine Learning.
- Practice version control and GitHub workflows.
- Apply concepts relevant to the Databricks Data Engineer certification.

## 3. Dataset

The initial dataset is a CSV file named `wind_power_data.csv`.

Location:

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

### Initial data quality assessment

The initial profiling identified:

- No missing values.
- No fully duplicated rows.
- No duplicate `production_id` values.
- No missing production identifiers.
- No negative energy production values.
- No negative wind speed values.
- No online records with zero energy production.
- No non-online records with positive energy production.

These results describe the initial dataset and do not guarantee
that future data will satisfy the same conditions.

## 4. Architecture

The project follows the Medallion Architecture using Azure Databricks
and Delta Lake.

### Bronze Layer

**Purpose:** Store ingested source data in a structured Delta table.

Main responsibilities:

- Read the source dataset.
- Load data into Databricks.
- Preserve the source information.
- Perform initial ingestion checks.

Main table:

`workspace.default.bronze_wind_power`

### Silver Layer

**Purpose:** Produce a validated and enriched dataset.

Main responsibilities:

- Validate data quality.
- Check identifiers and duplicate records.
- Analyze turbine operating statuses.
- Apply appropriate data types.
- Combine measurement dates and times.
- Create a `measurement_timestamp` column.

The Silver layer prepares the data for downstream analytics.

### Gold Layer

**Purpose:** Create business-oriented analytical datasets.

The daily production aggregation provides metrics by date and turbine.

Main table:

`workspace.default.gold_daily_production`

The table contains the following analytical columns:

| Column | Description |
|---|---|
| `date` | Production date |
| `turbine_name` | Turbine identifier |
| `total_energy_produced` | Total recorded energy production |
| `avg_wind_speed` | Average recorded wind speed |
| `total_measurements` | Total number of measurements |
| `online_measurements` | Number of measurements with Online status |
| `offline_measurements` | Number of measurements with Offline status |
| `online_measurement_pct` | Percentage of measurements with Online status |

The Gold table has been created and validated.

The current dataset produces 42 daily turbine groups,
corresponding to 14 days of observations across three turbines.

### Reporting Layer

**Purpose:** Make the analytical results accessible through Power BI.

The project uses a Databricks SQL connection to access the Gold dataset.

Planned dashboard name:

**Wind Power Performance Dashboard**

Potential reporting indicators include:

- Total energy production.
- Daily production trends.
- Production comparisons between turbines.
- Average wind speed.
- Turbine operating status.
- Online measurement percentage.

## 5. Technologies

### Local development

- Python 3.10
- pandas
- Git
- GitHub
- Ubuntu Linux
- Visual Studio Code / Jupyter notebooks

### Data platform

- Microsoft Azure
- Azure Databricks
- Apache Spark
- PySpark
- Delta Lake

### Analytics and reporting

- Databricks SQL
- Power BI

### Future technologies and concepts

- Databricks Workflows / Lakeflow Jobs
- Automated data quality checks
- CI/CD
- Machine Learning
- Predictive maintenance

## 6. Project Structure

```text
wind-power-analytics/
├── README.md
├── .gitignore
├── data/
│   └── raw/
│       └── wind_power_data.csv
├── notebooks/
│   ├── 01_bronze_ingestion.ipynb
│   ├── 02_silver_transformation.ipynb
│   └── 03_gold_analytics.ipynb
└── src/
    └── wind_power/
        ├── ingest_bronze.py
        └── profile_data.py