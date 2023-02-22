import requests
from time import time

port = 8181
endpoint = "api_saludar"
url = "http://127.0.0.1:{:d}/{:s}".format(port, endpoint)
headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}
query = {"nombre": "Gabriel"}
if __name__ == '__main__':
    a = time()
    x = requests.post(url, json=query, headers=headers)
    print(x.text)
    print(f"Request's time: {time() - a} seconds")
