# ART Carbon Predictor - Forecasting Methodology

## Purpose

The ART Carbon Predictor is designed to estimate future carbon credit issuance activity within the ART Registry.

The system attempts to answer:

- Which projects are most likely to issue credits next?
- When are credits likely to be issued?
- How many credits are likely to be issued?
- Which countries are expected to receive future credit increases?
- When are those increases expected to occur?

Forecasts are generated at the project level and then aggregated to create country-level forecasts.

---

# Forecasting Philosophy

Projects issue credits.

Countries do not directly issue credits.

For this reason, all forecasting is performed at the project level first.

Country forecasts are derived from aggregated project forecasts.

Example:

Project Forecasts

Acre:
- Predicted Credits: 400,000
- Predicted Date: 2027-Q2

Para:
- Predicted Credits: 850,000
- Predicted Date: 2027-Q3

Country Forecast

Brazil:
- Predicted Increase: 1,250,000
- Predicted Increase Date: 2027-Q2

---

# Current Forecasting Hypothesis

Current investigation suggests project maturity is reflected more strongly by document activity than by project status.

Many projects share the status:

ACTIVE

making status alone unsuitable for forecasting.

Document growth and document types may provide stronger signals.

Examples:

- TREES Concept
- TREES Registration Document
- TREES Monitoring Report
- FCPF Supporting Documents
- CATS Cancellation Certificate

Projects with larger and more diverse document histories appear to be more mature than projects with minimal documentation.

---

# Future Project Progress Score

Future forecasts will be built using a weighted scoring model.

Candidate inputs include:

## Document Progression

Measures:

- Document count
- Document type diversity
- Document chronology

## Project Age

Calculated as:

Current Date - Project Creation Date

## Crediting Period Progress

Calculated as:

Elapsed Crediting Period / Total Crediting Period

## Status Change Activity

Calculated as:

Current Date - Last Status Change

## Historical Issuance Behaviour

Projects will eventually be compared against historical issuance patterns from completed projects.

---

# Forecast Outputs

## Project Forecast

Fields:

- Forecast Score
- Predicted Issuance Date
- Predicted Credit Volume
- Confidence Score

Example:

| Project | Score | Predicted Date | Predicted Credits |
|----------|----------|----------|----------|
| Acre | 82 | 2027-Q3 | 450,000 |

## Country Forecast

Fields:

- Current Credits
- Predicted Increase
- Predicted Increase Date
- Confidence Score

Example:

| Country | Current Credits | Predicted Increase | Predicted Date |
|----------|----------|----------|----------|
| BR | 0 | 1,250,000 | 2027-Q2 |

The Predicted Increase Date represents the earliest forecasted issuance event among projects in that country.

---

# Forecast Quality Requirements

Before forecasts are considered production-ready:

Projects Loaded
=
Projects Available In Registry

Forecasting on a partial dataset introduces bias and reduces confidence.

Full registry coverage is required before forecast outputs are trusted.

---

# Long-Term Goal

The long-term objective is to provide evidence-based forecasts of:

- Future issuance dates
- Future credit volumes
- Country-level credit increases

before the issuance events occur.