import json
import sqlite3
from datetime import datetime

# Connect to database

conn = sqlite3.connect("database/carbon.db")
cursor = conn.cursor()

print("Connected to database")

# Load ART JSON

with open(
    "data/art_projects.json",
    "r",
    encoding="utf-8"
) as file:

    data = json.load(file)

projects = data["datasets"]["projects"]["rows"]

print(f"Projects Found: {len(projects)}")

# Load Projects Table

for project in projects:

    cursor.execute("""
    INSERT OR REPLACE INTO projects
    (
        project_id,
        project_key,
        project_name,
        country,
        project_type,
        methodology,
        developer,
        crediting_program,
        jurisdiction
    )
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    """,
    (
        project["projectId"],
        project["projectKey"],
        project["projectName"],
        project["country"],
        project["projectType"],
        project["projectMethodology"],
        project["projectDeveloper"],
        project["creditingProgram"],
        project["projectExtensionMap"].get("programJurisdiction")
    ))

conn.commit()

print("Projects Loaded")

# Create Daily Snapshot

today = datetime.today().strftime("%Y-%m-%d")

for project in projects:

    cursor.execute("""
    INSERT INTO project_snapshots
    (
        snapshot_date,
        project_id,
        project_status,
        issued_credits,
        last_status_changed
    )
    VALUES (?, ?, ?, ?, ?)
    """,
    (
        today,
        project["projectId"],
        project["projectStatus"],
        project["issuedCredits"],
        project["projectExtensionMap"].get(
            "lastProjectStatusChanged"
        )
    ))

conn.commit()

print("Snapshots Loaded")

conn.close()

print("Database Updated")