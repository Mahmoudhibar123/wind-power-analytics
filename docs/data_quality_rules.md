# Wind Power Analytics — Data Quality Rules

## Purpose

This document defines the data quality rules used to validate
wind turbine production measurements.

## Rules

| ID | Rule | Validation | Severity |
|---|---|---|---|
| DQ-01 | Production identifier is mandatory | `production_id IS NOT NULL` | Critical |
| DQ-02 | Production identifier is unique | No duplicate `production_id` | Critical |
| DQ-03 | Turbine identifier is mandatory | `turbine_name IS NOT NULL` | Critical |
| DQ-04 | Energy production is non-negative | `energy_produced >= 0` | High |
| DQ-05 | Wind speed is non-negative | `wind_speed >= 0` | High |
| DQ-06 | Turbine status is recognized | Status belongs to the approved list | High |
| DQ-07 | Measurement timestamp is mandatory | `measurement_timestamp IS NOT NULL` | Critical |
| DQ-08 | Turbine measurement timestamp is unique | No duplicate turbine/timestamp pair | High |

## Approved Status Values

- Online
- Offline
- Preventive Maintenance
- Reactive Maintenance
- Fault
- Inspection

## Validation Principles

- Validate data before using it for analytics.
- Report the number of records violating each rule.
- Do not silently discard invalid records.
- Investigate failures before deciding whether to reject or quarantine records.
- Review business rules when source definitions or measurement units change.

## Current Limitations

The rules must be tested against the actual dataset.

The physical units of wind speed and energy production have not yet
been confirmed. No arbitrary upper limits are defined.

The relationship between turbine status and energy production
requires further business validation.
