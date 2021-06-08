import requests

ACCESS_TOKEN = ''
DOMAIN = 'http://recon1234.pythonanywhere.com/'


# Pinging server on boot
print('Ping {}'.format(DOMAIN))
url = DOMAIN + '/data/ping'
data = {
    'token': 'long live cutie'
}

response = requests.post(url, data = data)
print(response)
response = response.json()
try:
    status = response['status']
    if status == 'OK':
        print('Fetching access token...')
        ACCESS_TOKEN = response['access_token']
        print('Connection established.')
    else:
        print('Unable to connect')
except:
    print('Unable to connect')


# Updating info on vehicle sight
print('Adding new Recon Iot node')
url = DOMAIN + '/data/cam'
data = {
    'access_token': ACCESS_TOKEN,
    'cam_type': 'static',
    'latitude': '9.111111',
    'longitude': '76.111111',
    'place': 'Place name',
    'description': 'test desc',
    
}

response = requests.post(url, data = data)

response = response.json()
try:
    status = response['status']
    if status == 'OK':
        print('Added successfully')
    else:
        print('Failed.')
except:
    print('Failed.')