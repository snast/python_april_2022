import requests
url = 'https://api.fortnitetracker.com/v1/store'
headers = {
    'TRN-api-key': 'd717a54c-5dea-4d9a-bbec-b458d29e8ec6'
}

r = requests.get(url, headers=headers)
print(r.json())