import requests

ACCESS_TOKEN = ''
BLACKLIST = []

# Pinging server on boot
print('Ping reconlive.pythonanywhere.com')
url = 'http://localhost:5000/iot/ping'
data = {
    'token': 'long live cutie'
}

response = requests.post(url, data = data)
response = response.json()
try:
    status = response['status']
    if status == 'OK':
        print('Fetching access token...')
        print('Downloading blacklist...')
        ACCESS_TOKEN = response['access_token']
        BLACKLIST = response['blacklist']
        print('Connection established.')
    else:
        print('Unable to connect')
except:
    print('Unable to connect')


# Updating info on vehicle sight
print('Uploading sight info')
url = 'http://localhost:5000/iot/sight'
data = {
    'access_token': ACCESS_TOKEN,
    'vehicle_id': 'KL30F3000',
    'cam_id': 1
}

response = requests.post(url, data = data)
response = response.json()
try:
    status = response['status']
    if status == 'OK':
        print('Sight info updated successfully')
    else:
        print('Upload failed.')
except:
    print('Upload failed.')