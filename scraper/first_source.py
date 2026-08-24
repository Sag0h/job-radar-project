import requests

URL = "https://empleos.educacionit.com/"

response = requests.get(URL)

print(response.status_code)
print(response.text[:2000])