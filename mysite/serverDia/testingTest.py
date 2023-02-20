import requests

URL = 'http://127.0.0.1:8000/user_login/'

g = requests.get(URL)

data = {
  "username": "adminDia",
  "password": "1245",
}

r = requests.post(URL, data=data, headers=g.headers)