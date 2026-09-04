# ART Carbon Predictor - System Architecture

## Overview

The system collects project information from the ART Registry and stores it in SQLite.

The database acts as the historical source of truth used for reporting and future forecasting.

---

# Data Flow

ART Registry
    ↓
Project Summary API
    ↓
load_art_data.py
    ↓
projects
project_snapshots
    ↓
Project Detail API
    ↓
load_project_details.py
    ↓
project_details
project_documents
    ↓
Analytics Layer
    ↓
Forecast Engine
    ↓
Excel Reports

---

# Database Tables

## projects

Stores relatively static project information.

Purpose:

Identify projects and associate them with countries.

Example fields:

- project_id
- project_key
- project_name
- country
- methodology
- developer

---

## project_snapshots

Stores historical project states.

Purpose:

Track how projects change over time.

Example fields:

- snapshot_date
- project_status
- issued_credits
- last_status_changed

A new snapshot should be created every collection cycle.

Historical snapshots should never be overwritten.

---

## project_details

Stores metadata retrieved from the project detail API.

Purpose:

Provide additional context used for forecasting.

Example fields:

- project_listing_status
- project_creation_date
- project_start_date
- crediting_period_dates

---

## project_documents

Stores project document history.

Purpose:

Track project maturity and progression.

Example fields:

- document_name
- document_type
- document_category
- upload_date

This is expected to become one of the most important forecasting datasets.

---

# Current Scripts

## create_database.py

Purpose:

Create all required SQLite tables.

Output:

carbon.db

---

## load_art_data.py

Purpose:

Import summary project data.

Updates:

- projects
- project_snapshots

---

## load_project_details.py

Purpose:

Import detailed project metadata and documents.

Updates:

- project_details
- project_documents

---

## verify_projects.py

Purpose:

Verify data loaded into projects table.

---

## verify_project_details.py

Purpose:

Verify data loaded into project_details table.

---

## document_summary.py

Purpose:

Summarise document types across all projects.

Used to identify maturity indicators.

---

## document_counts.py

Purpose:

Calculate document counts per project.

Used as an early project progression metric.

---

## country_summary.py

Purpose:

Generate country-level reporting.

Output:

Country_Summary.xlsx

---

## project_detail.py

Purpose:

Generate project-level reporting.

Output:

Project_Detail.xlsx

---

# Future Components

## Pagination Engine

Purpose:

Ensure all registry projects are collected.

Success Criteria:

Database project count equals registry project count.

---

## Project Progress Engine

Purpose:

Calculate project maturity scores.

Output:

Project_Progress.xlsx

---

## Forecast Engine

Purpose:

Generate:

- Predicted Issuance Date
- Predicted Credit Volume
- Confidence Score

Output:

Project_Forecast.xlsx

---

## Country Forecast Engine

Purpose:

Aggregate project forecasts into country-level predictions.

Output:

Country_Forecast.xlsx

---

# Extension Guidelines

When adding new data sources:

1. Create a dedicated collection script.
2. Store raw data in SQLite.
3. Avoid overwriting historical records.
4. Build reports from database tables rather than directly from APIs.
5. Ensure project forecasts remain the foundation of country forecasts.

This keeps forecasting logic reproducible and auditable.