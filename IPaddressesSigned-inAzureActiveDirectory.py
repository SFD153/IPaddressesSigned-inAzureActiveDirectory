import requests
import json

tenant_id = "b8cb644c-f583-4be4-8c0d-9b9313735f23"
client_id = "1cfead55-88e7-4722-b618-e02b377d4b09"
client_secret = "wko8Q~rdyRZ4YJOnFhOvG12rMUEMX7~ovikAqa.D"

# Get access token
token_url = f"https://login.microsoftonline.com/{tenant_id}/oauth2/v2.0/token"
scope = "https://graph.microsoft.com/.default"
payload = {
    "client_id": client_id,
    "client_secret": client_secret,
    "scope": scope,
    "grant_type": "client_credentials"
}
response = requests.post(token_url, data=payload)
access_token = response.json()["access_token"]

url = "https://graph.microsoft.com/v1.0/auditLogs/signIns"
headers = {
    "Authorization": f"Bearer {access_token}",
    "Content-Type": "application/json"
}

response = requests.get(url, headers=headers)
results = json.loads(response.text)

for result in results["value"]:
    #print("User:", result["userDisplayName"])
    print("IP Address:", result["ipAddress"])
    print("--------------------------------------------------------")
