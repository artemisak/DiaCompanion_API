import requests

LOGIN_URL = 'http://127.0.0.1:8000/user_login/'

headers = {
}

response = requests.get(LOGIN_URL, headers=headers)

headers['cookie'] = '; '.join([x.name + '=' + x.value for x in response.cookies])
headers['X-CSRFToken'] = response.content.decode("utf-8")

data = {
  "username": "adminDia",
  "password": "1245",
}

response = requests.post(LOGIN_URL, data=data, headers=headers)
print(response.request, response.status_code, response.content)