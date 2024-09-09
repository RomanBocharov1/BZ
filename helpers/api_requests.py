import hashlib
import hmac
import json
import requests

# def request(url):  # запрос без авторизации
#     req = requests.get(url)
#     code = req.status_code
#     response = req.json()
#     return response, code
#
#
# data = request('https://mobileapi.berizaryad.ru/api/v2/vendings?location_id=11111&zone=RUS_SBER')
# print(json.dumps(data, ensure_ascii=False, indent=1))


base_url = 'https://stageapi.berizaryad.ru'  # запрос c авторизацией
endpoint = "/orders"
signature_key = '722aaad988e04a8782f7f3d5f6c313c6'
request_data = {
        "app_version": "5.8.0",
        "phone": "79858906684",
        "udid": "1A5AA5C7-7C73-4C03-A92E-7AF2F381876E",
        "platform": "Android",
        "os_version": "10"
    }
access_token = ''


def generate_signature(payload):
    msg = json.dumps(payload).encode()
    messenger_key = signature_key.encode()
    signature = hmac.new(messenger_key, msg, digestmod=hashlib.sha256).hexdigest()
    return {'Locale': 'ru', 'signature': signature, 'Content-Type': 'application/json'}


def login(number):
    url = "/auth/api/v2/login"
    data_json = request_data
    data_json['phone'] = number
    return requests.post(url=base_url+url, json=data_json, headers=generate_signature(data_json))


def confirm(number):
    url = "/auth/api/v2/confirm"
    data_json = request_data
    data_json['phone'] = number
    data_json['code'] = "0001"
    return requests.post(url=base_url+url, json=data_json, headers=generate_signature(data_json))


def req(token):
    headers = {
        "authorization": f"Bearer {token}"
        }
    return requests.get(url=base_url+endpoint, headers=headers)


generate_signature(request_data)
login(request_data['phone'])

data_request = confirm(request_data['phone'])
json_data_request = data_request.json()
access_token = json_data_request['access_token']

data_main_request = req(access_token)
response = data_main_request.json()
print(json.dumps(response, ensure_ascii=False, indent=1))
