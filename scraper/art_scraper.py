import requests
import pandas as pd

url = "https://greentrace.ice.com/art/projects"

response = requests.get(url)

data = response.json()

projects = data["datasets"]["projects"]["rows"]

df = pd.json_normalize(projects)

print(df.columns)

print(df.head())


df.to_csv(
    "data/projects.csv",
    index=False
)

df.to_excel(
    "data/projects.xlsx",
    index=False
)

print("Files exported")


country_summary = (
    df.groupby("country")
      .agg(
           Projects=("projectId", "count"),
           Credits=("issuedCredits", "sum")
      )
      .reset_index()
)


country_summary.to_excel(
    "data/country_summary.xlsx",
    index=False
)