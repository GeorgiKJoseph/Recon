import requests

ACCESS_TOKEN = ''

# Pinging server on boot
print('Ping reconlive.pythonanywhere.com')
url = 'http://localhost:5000/data/ping'
data = {
    'token': 'long live cutie'
}

response = requests.post(url, data = data)
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
print('Adding new Vehicle')
url = 'http://localhost:5000/data/vehicle'
data = {
    'access_token': ACCESS_TOKEN,
    'vehicle_no': 'KL00A0000',
    'owner': 'Noone',
    'vehicle_type': 'sedan',
    'brand': 'Brand',
    'model': 'Model',
    'color': 'Color',
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