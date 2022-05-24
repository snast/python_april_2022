import requests
# r = requests.get('https://api.github.com/user', auth=('user', 'pass'))
headers = {
    'TRN-api-key': 'XXXX'
}
r = requests.get('https://api.fortnitetracker.com/v1/store', headers=headers)
print(r.json())