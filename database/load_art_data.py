import json
import sqlite3
from datetime import datetime

# Connect to database

conn = sqlite3.connect("database/carbon.db")
cursor = conn.cursor()

print("Connected to database")

# Load ART JSON

import requests

url = (
    "https://greentrace.ice.com"
    "/api/greentraceservice/v1/project/"
    "registry/ART_REGISTRY/project-summaries/results"
)

all_projects = []

offset = 0
page_number = 1
max_results = 20

while True:

    payload = {
        "offset": offset,
        "pageNumber": page_number,
        "developer": "",
        "projectType": "",
        "max": max_results
    }

    response = requests.post(
        url,
        data=payload
    )

    data = response.json()

    projects = (
        data["datasets"]
        ["projects"]
        ["rows"]
    )

    print(
        f"Page {page_number}: "
        f"{len(projects)} projects"
    )

    if len(projects) == 0:
        break

    all_projects.extend(projects)

    if len(projects) < max_results:
        break

    offset += max_results
    page_number += 1

print(
    f"Total Projects Found: "
    f"{len(all_projects)}"
)

projects = all_projects

# print(f"Projects Found: {len(projects)}")

# Load Projects Table

print(

    f"Projects being inserted: {len(projects)}"
)

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