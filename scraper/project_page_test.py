import requests

url = (
    "https://greentrace.ice.com/art/projects/"
    "registry/ART_REGISTRY/project/P2323FSYP922"
)

response = requests.get(url)

print("Status:", response.status_code)

html = response.text

print(html[:5000])

with open(
    "data/project_test.html",
    "w",
    encoding="utf-8"
) as file:
    file.write(html)

print("Saved page")