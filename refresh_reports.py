import subprocess

scripts = [

    # Database reports
    "database/document_summary.py",
    "database/document_type_summary.py",
    "database/issued_project_documents.py",
    "database/issued_vs_not_issued.py",
    "database/project_document_matrix.py",
    "database/project_document_timeline.py",

    # Report generation
    "reports/country_summary.py",
    "reports/project_detail.py",
    "reports/project_analysis.py",
    "reports/project_milestones.py",
    "reports/project_progress.py",
    "reports/project_ranking.py",
    "reports/forecast_features.py",
    "reports/forecast_projects.py",
    "reports/forecast_countries.py",
]

for script in scripts:
    print("\n" + "=" * 60)
    print(f"Running: {script}")
    print("=" * 60)

    try:
        subprocess.run(["python", script], check=True)
        print(f"✅ Completed: {script}")

    except Exception as e:
        print(f"❌ Failed: {script}")
        print(e)

print("\n🎉 Report refresh complete")