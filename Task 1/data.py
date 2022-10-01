import requests
url = "https://restcountries.com/v3.1/all"
response = requests.request("GET",url)
print(response.text)