import requests
import json

url = (
    "https://greentrace.ice.com"
    "/api/greentraceservice/v1/project/"
    "registry/ART_REGISTRY/project-summaries"
)

response = requests.get(url)

print("Status:", response.status_code)
print(response.text[:1000])
