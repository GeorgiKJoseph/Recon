
import random
import requests
vehicle_no = ['KL30F1000','KL29G2000','KL33H3000','KL59J4000','KL27B5000','KL12K6000']

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

    

def generate_route(cn,vn):
    
    if cn == 1:
        nn = route_north(cn,vn)
        print(nn)
        
        
    elif cn == 20:
       ss = route_south(cn,vn)
       print(ss)

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
    print(vehicle_id)
    print('Uploading sight info')
    url = 'http://localhost:5000/iot/sight'
    data = {
    'access_token': ACCESS_TOKEN,
    'vehicle_id': 'hello',
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

    
    

def route_north(cn,vn) : 
    camera_id = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20] 
    route_north = []
    to_north = random.randrange(cn+1,len(camera_id)+1)
    for item in range(cn,to_north+1):
        route_north.append(item)
    ulti = []
    ulti.append(vn)
    ulti.append(route_north)
    return ulti
    
def route_south(cn,vn) :
    camera_id = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]   
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
    camera_id = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
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
    global vehicle_no
    
    camera_id = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
    
    

    v = random.choice(vehicle_no)
    vehicle_no.remove(v)
    c = random.choice(camera_id)

   

    result = generate_route(c,v)
    return result
    
   
    
    
a = master()
print(a)
print(vehicle_no)



