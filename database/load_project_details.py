import sqlite3
import requests
from datetime import datetime

conn = sqlite3.connect("database/carbon.db")

cursor = conn.cursor()

cursor.execute("""
SELECT
    project_id,
    project_key
FROM projects
""")

projects = cursor.fetchall()

print(f"Projects to process: {len(projects)}")

for project_id, project_key in projects:

    url = (
        "https://greentrace.ice.com"
        "/api/greentraceservice/v1/project/"
        f"registry/ART_REGISTRY/project/{project_key}"
    )

    response = requests.get(url)

    if response.status_code != 200:

        print(f"Failed: {project_id}")

        continue

    data = response.json()

    detail = data["projectDetail"]

    print(f"Loaded: {project_id}")

    cursor.execute("""
    INSERT OR REPLACE INTO project_details
    (
        project_id,
        project_listing_status,
        project_creation_date,
        project_start_date,
        current_crediting_period_start,
        current_crediting_period_end,
        project_holdings_total_quantity,
        updated_at
    )
    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """,
    (
        detail["projectReferenceId"],
        detail["projectListingStatus"],
        detail["projectCreationDate"],
        detail["projectStartDate"],
        detail["currentCreditingPeriodStartDate"],
        detail["currentCreditingPeriodEndDate"],
        detail["projectHoldingsTotalQuantity"],
        datetime.today().strftime("%Y-%m-%d")
    ))

    documents = (
        data["documents"]
        ["datasets"]
        ["publicDocuments"]
        ["rows"]
    )

    for doc in documents:

        cursor.execute("""
        INSERT OR IGNORE INTO project_documents
        (
            project_id,
            document_name,
            document_title,
            document_type,
            document_category,
            upload_date,
            download_url
        )
        VALUES (?, ?, ?, ?, ?, ?, ?)
        """,
        (
            project_id,
            doc["name"],
            doc["title"],
            doc["type"],
            doc["category"],
            doc["uploadDate"],
            doc["download"]["url"]
        ))

conn.commit()

conn.close()

print("Project details loaded")