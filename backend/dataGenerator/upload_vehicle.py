import requests
import csv


ACCESS_TOKEN = ''
DOMAIN = 'http://localhost:5000'

def upload(row):
    # Updating info on vehicle sight
    print('Adding new Vehicle')
    url = DOMAIN + '/data/vehicle'
    data = {
        'access_token': ACCESS_TOKEN,
        'vehicle_no': row['vehicle_no'],
        'owner': row['owner'],
        'vehicle_type': row['vehicle_type'],
        'brand': row['brand'],
        'model': row['model'],
        'color': row['color'],
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
    print('Ping reconlive.pythonanywhere.com')
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

    with open('files/vehicle_reg.csv', 'r') as in_file:
        csv_in = csv.DictReader(in_file)
        for row in csv_in:
            upload(row)
