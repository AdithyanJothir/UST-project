import requests
from mongoengine import *
from models import Country




     
connect('countries')

url = "https://restcountries.com/v3.1/all"
response = requests.request("GET",url)
response = response.json()


for i in range(len(response)):
    
    
    try:
        country = Country(country_id = i ,name = response[i]['name']['official'],area = response[i]['area'],
        timezone = response[i]['timezones'],languages =list(response[i]['languages'].keys()),
        continents =  response[i]['continents'],un_member = response[i]['unMember'],
        latlong =response[i]['latlng'][::-1],capital = response[i]['capital'],
        independance = response[i]['independent'], region = response[i]['region'] ,population = response[i]['population'])
    except Exception as e:
        print(e)
    finally:
        country.validate()
        country.save()


