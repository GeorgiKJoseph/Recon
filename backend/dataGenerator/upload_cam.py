import requests
import csv

ACCESS_TOKEN = ''
DOMAIN = 'http://localhost:5000'


def upload(row):
    # Updating info on vehicle sight
    print('Adding new Recon Iot node')
    url = DOMAIN + '/data/cam'
    data = {
        'access_token': ACCESS_TOKEN,
        'cam_type': row['type'],
        'latitude': row['latitude'],
        'longitude': row['longitude'],
        'place': row['place'],
        'description': row['description'],
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


if __name__ == '__main__':
    # Pinging server on boot
    print('Ping {}'.format(DOMAIN))
    url = DOMAIN + '/data/ping'
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


    with open('files/camera.csv', 'r') as in_file:
        csv_in = csv.DictReader(in_file)
        for row in csv_in:
            upload(row)
