import requests

project_key = "P2323FSYP922"

url = (
    "https://greentrace.ice.com"
    "/api/greentraceservice/v1/project/"
    f"registry/ART_REGISTRY/project/{project_key}"
)

response = requests.get(url)

print("Status:", response.status_code)

data = response.json()

print(data.keys())

print()
print(
    data["projectDetail"]["projectName"]
)
