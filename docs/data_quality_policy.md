# Data Quality Policy

## 1. Purpose

This document defines how data quality anomalies are handled
in the Wind Power Analytics project.

The objective is to prevent invalid records from affecting
validated Silver data and Gold analytics.

## 2. General principles

- Data quality rules must be documented.
- Invalid records must not silently disappear.
- Corrections must be based on explicit business rules.
- Anomalies must remain traceable for investigation.
- Quality check results must be retained for auditing.

## 3. Anomaly handling

| Rule ID | Anomaly | Proposed action |
|---|---|---|
| DQ-01 | Missing production ID | Quarantine |
| DQ-02 | Duplicate production ID | Investigate and quarantine affected duplicates |
| DQ-03 | Missing or empty turbine name | Quarantine |
| DQ-04 | Negative energy production | Quarantine |
| DQ-05 | Negative wind speed | Quarantine |
| DQ-06 | Invalid status | Quarantine |
| DQ-07 | Missing measurement timestamp | Quarantine |
| DQ-08 | Duplicate turbine/timestamp combination | Investigate and quarantine affected measurements |

## 4. Data correction

Records must not be corrected automatically unless an explicit,
documented business rule justifies the correction.

For example, negative energy production must not automatically
be replaced with zero.

## 5. Traceability

Quality results must include the rule identifier, the number
of invalid records, the execution timestamp and the result.

Quarantined records should be retained separately for investigation.

## 6. Downstream consumption

Gold analytics must be built from Silver data that satisfies
the project's applicable quality requirements.
