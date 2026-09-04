# ART Carbon Predictor - Methodology

## Purpose

The ART Carbon Predictor is designed to forecast future carbon credit issuance activity within the ART Registry.

The system attempts to answer three distinct questions:

1. What stage is a project currently in?
2. When is a project likely to issue credits?
3. How many credits is a project likely to issue?

Project forecasts are generated first and country forecasts are derived from aggregated project forecasts.

---

# Forecasting Philosophy

The project does not attempt to predict credit issuance directly.

Instead the system attempts to understand and model the ART project progression process.

The central hypothesis is that projects move through a series of observable milestones prior to issuing credits.

By measuring project progression through those milestones, the system can estimate the likelihood and timing of future issuance events.

---

# Current Research Findings

## Project Status Is A Weak Signal

Many projects share the same registry status:

ACTIVE

As a result, project status alone provides limited forecasting value.

---

## Document Activity Is A Strong Signal

Projects contain different document types and document histories.

Analysis suggests that documents represent steps within the project lifecycle.

Document content appears to be more informative than project status.

---

# Multiple Project Pathways

Current evidence suggests that projects may follow different issuance pathways.

## TREES Pathway

Observed documents include:

- TREES Concept
- TREES Registration Document
- TREES Monitoring Report

Examples:

- Acre
- Para
- Bhutan

---

## FCPF Pathway

Observed documents include:

- ERPD
- Validation Report
- Verification Report
- Monitoring Report

Examples:

- Costa Rica
- Côte d'Ivoire

---

## Post-Issuance Pathway

Observed documents include:

- CATS Cancellation Certificates

Example:

- Mai-Ndombe

These documents indicate credits have already been issued and subsequently retired or cancelled.

---

# Project Lifecycle Hypothesis

The current working hypothesis is:

TREES Concept
↓
Registration
↓
Validation
↓
Verification
↓
Monitoring
↓
Issuance
↓
Cancellation

This sequence is not yet fully proven and will be refined through continued document analysis.

---

# Forecast Models

The project will ultimately contain three separate forecasting models.

## Model 1: Project Progression

Purpose:

Determine current project maturity.

Inputs:

- Document types
- Document chronology
- Status history
- Project age

Output:

- Current stage
- Stage score
- Next likely milestone

---

## Model 2: Issuance Timing

Purpose:

Estimate when credits are likely to be issued.

Inputs:

- Current stage
- Days since latest milestone
- Project pathway
- Country factors
- Historical milestone durations

Output:

- Predicted issuance date
- Confidence