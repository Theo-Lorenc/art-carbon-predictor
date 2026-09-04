# ART Carbon Predictor - System Architecture

## Overview

The ART Carbon Predictor collects project data from the ART Registry and stores it in a local SQLite database.

The database functions as the project's source of truth.

All reports and future forecasts are generated from the database rather than directly from API responses.

---

# Current Data Flow

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
Stage Classification
↓
Forecast Engine
↓
Country Aggregation
↓
Excel Reports

---

# Registry Coverage

Current Coverage:

30 / 30 Projects

Project summary pagination has been implemented using:

offset
pageNumber
max

The system now retrieves all available ART projects.

---

# Database Tables

## projects

Stores project identity information.

Examples:

- project_id
- project_key
- project_name
- country
- methodology
- jurisdiction

---

## project_snapshots

Stores historical project state information.

Examples:

- snapshot_date
- project_status
- issued_credits
- last_status_changed

Purpose:

Track project changes over time.

---

## project_details

Stores project-level metadata.

Examples:

- project_creation_date
- project_start_date
- coverage_area
- crediting_period
- listing_status

Purpose:

Store variables useful for future forecasting.

---

## project_documents

Stores document metadata.

Examples:

- document_type
- document_title
- upload_date
- download_url

Purpose:

Track project progression through documentation.

---

# Future Tables

## project_stages

Purpose:

Assign projects to observed lifecycle stages.

Example fields:

- project_id
- stage
- stage_score
- stage_date
- days_since_stage

---

## project_forecasts

Purpose:

Store project forecasts.

Example fields:

- project_id
- predicted_issuance_date
- predicted_credit_volume
- confidence_score

---

## country_forecasts

Purpose:

Store country forecast outputs.

Example fields:

- country
- predicted_increase
- predicted_date
- confidence_score

---

# Current Scripts

## load_art_data.py

Downloads project summaries.

Updates:

- projects
- project_snapshots

---

## load_project_details.py

Downloads project details and document metadata.

Updates:

- project_details
- project_documents

---

## document_summary.py

Analyses document categories.

---

## document_counts.py

Calculates document counts.

---

## issued_vs_not_issued.py

Compares issued and non-issued projects.

---

## project_document_matrix.py

Maps document types by project.

---

## project_document_timeline.py

Analyses document chronology.

---

## issued_project_documents.py

Analyses document history for projects that have already issued credits.

---

# Next Development Phase

## Stage Classification Engine

Purpose:

Identify project lifecycle stages from document evidence.

Potential stages:

- Concept
- Registration
- Validation
- Verification
- Monitoring
- Issued
- Cancelled

---

## PDF Intelligence Engine

Purpose:

Download and extract information from project documents.

Potential outputs:

- Validation dates
- Verification dates
- Monitoring dates
- Carbon estimates
- Forest metrics
- Expected reductions

---

## Forecast Engine

Purpose:

Generate:

- Project progression forecasts
- Issuance date forecasts
- Credit volume forecasts

---

## Country Aggregation Engine

Purpose:

Aggregate project forecasts into country forecasts.

Outputs:

- Predicted credit increases
- Predicted increase dates
- Confidence scores

---

# Extension Rules

When adding new functionality:

1. Store raw information first.
2. Preserve historical records.
3. Avoid direct API-to-report workflows.
4. Generate analytics from database tables.
5. Generate country forecasts from project forecasts.
6. Validate forecasting variables before using them in production models.

This ensures the forecasting process remains transparent, reproducible and auditable.