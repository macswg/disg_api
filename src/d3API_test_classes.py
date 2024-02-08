import requests


ip = 'http://127.0.0.1'
base_url = "/api/session/transport/gototag"

# payload_status = {'status': 'status', 'health': 'health'}
payload_bright_off = "{ \"transports\": [ { \"transport\": { \"name\": \"trans_101\" }, \"brightness\": 0 } ]}"
payload_bright_on = "{ \"transports\": [ { \"transport\": { \"name\": \"trans_101\" }, \"brightness\": 1 } ]}"
payload_neon = "{ \"transports\": [ { \"transport\": { \"name\": \"trans_101\" }, \"type\": \"CUE\", \"value\": \"901\", \"allowGlobalJump\": false, \"playmode\": \"PlaySection\" } ]}"  

# payload = payload_status
payload = payload_neon

url = ''.join([ip, base_url])

# get request
# r = requests.get(url, params=payload)
# print(r.json())

# post request
r = requests.post(url, data=payload)


print(r.json())



# r = requests.get(url)

# print(r.json())






####
# NOTE - DELETE ME

# ip = 'http://127.0.0.1'
# base_url = "/api/session/transport/brightness"

# payload_status = {'status': 'status', 'health': 'health'}
# payload_bright = "{ \"transports\": [ { \"transport\": { \"name\": \"trans_101\" }, \"brightness\": 0 } ]}"

# payload = payload_status
# payload = payload_bright

# url = ''.join([ip, base_url])

# get request
# r = requests.get(url, params=payload)
# print(r.json())

# post request
# r = requests.post(url, params=payload)

# r = requests.post('http://127.0.0.1/api/session/transport/brightness', data=payload_bright)

# print(r.json())