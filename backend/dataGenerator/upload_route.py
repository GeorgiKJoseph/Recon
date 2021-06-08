import random
import csv
import requests

COUNT = 99
ACCESS_TOKEN = ''
BLACKLIST = []
DOMAIN = 'http://localhost:5000'


camera_id = [i for i in range(1,26)]
CAMID_MAX = len(camera_id)

# Collection vehicle numbers
vehicle_no = []
with open('files/domain/vehicle_no.csv', 'r') as in_file:
    csv_in = csv.DictReader(in_file)
    for row in csv_in:
        vehicle_no.append(row['vehicle_no'])


# Pinging server on boot
print('Ping reconlive.pythonanywhere.com')
url = DOMAIN + '/iot/ping'
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


def generate_route(cn,vn):
    if cn == 1:
        nn = route_north(cn,vn)
        print(nn)
        dhuru = nn

    elif cn == CAMID_MAX:
       ss = route_south(cn,vn)
       print(ss)
       dhuru = ss

    else:
        xx  = route_north(cn,vn)
        yy = route_south(cn,vn)
        zz = route_commute(cn,vn)
        print(xx)
        print(yy)
        print(zz)

        cutie = []
        cutie.append(xx)
        cutie.append(yy)
        cutie.append(zz)
        dhuru = random.choice(cutie)
        print(dhuru)
    upload_dhuru(dhuru)


def upload_dhuru(dhuru):
    [vehicle_id,cam_ids] = dhuru
    for id in cam_ids:
        print('Uploading sight info')
        url = DOMAIN + '/iot/sight'
        data = {
        'access_token': ACCESS_TOKEN,
        'vehicle_id': vehicle_id,
        'cam_id': id
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



def route_north(cn,vn) :
    global camera_id
    route_north = []
    to_north = random.randrange(cn+1,len(camera_id)+1)
    for item in range(cn,to_north+1):
        route_north.append(item)
    ulti = []
    ulti.append(vn)
    ulti.append(route_north)
    print(ulti)
    return ulti


def route_south(cn,vn) :
    global camera_id
    route_south = []
    to_south = random.randrange(camera_id[0],cn)
    for item in range(to_south,cn+1):
        route_south.append(item)
    route_south.sort(reverse=True)
    ulti = []
    ulti.append(vn)
    ulti.append(route_south)
    return ulti


def route_commute(cn,vn):
    global camera_id
    route_commute = []
    to_commute = random.randrange(cn+1,len(camera_id)+1)
    for item in range(cn,to_commute+1):
        route_commute.append(item)
    for x in range(route_commute[-1]-1,cn-1,-1):
        route_commute.append(x)
    ulti = []
    ulti.append(vn)
    ulti.append(route_commute)
    return ulti



def master():
    global vehicle_no, camera_id
    v = random.choice(vehicle_no)
    vehicle_no.remove(v)
    c = random.choice(camera_id)
    print('Cam id: ',c)
    result = generate_route(c,v)
    return result


if __name__ == "__main__":
    if COUNT < len(vehicle_no):
        for i in range(COUNT):
            a = master()
