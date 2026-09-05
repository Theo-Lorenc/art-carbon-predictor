import subprocess

DATABASE_SCRIPTS = [

    "database/create_database.py",
    "database/load_art_data.py",
    "database/load_project_details.py"

]

REPORT_SCRIPTS = [

    "database/document_summary.py",
    "database/document_type_summary.py",
    "database/issued_project_documents.py",
    "database/issued_vs_not_issued.py",
    "database/project_document_matrix.py",
    "database/project_document_timeline.py",

    "reports/country_summary.py",
    "reports/project_detail.py",
    "reports/project_analysis.py",
    "reports/project_milestones.py",
    "reports/project_progress.py",
    "reports/project_ranking.py"

]

FORECAST_SCRIPTS = [

    "reports/forecast_features.py",
    "reports/forecast_projects.py",
    "reports/forecast_countries.py"

]

for script in (
    DATABASE_SCRIPTS
    + REPORT_SCRIPTS
    + FORECAST_SCRIPTS
):
    ...

print("All tasks completed")