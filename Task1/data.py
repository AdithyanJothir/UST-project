import requests
from mongoengine import *


connect('countries')


url = "https://restcountries.com/v3.1/all"
response = requests.request("GET",url)
response = response.json()


class Country(Document):
    country_id = IntField()
    name = StringField()
    capital = ListField()
    area = FloatField()
    timezone = ListField()
    independance = BooleanField()
    continents = ListField()
    un_member = BooleanField()
    languages = DictField()
    population = IntField()
    region = StringField()



for i in range(len(response)):
    try:
        country = Country(country_id = i ,name = response[i]['name']['official'],area = response[i]['area'],
        timezone = response[i]['timezones'],languages =response[i]['languages'],
        continents =  response[i]['continents'],un_member = response[i]['unMember'],
        population =response[i]['population'],capital = response[i]['capital'],
        independance = response[i]['independent'], region = response[i]['region'] )
    except Exception as e:
        print(e)
    finally:
        country.validate()
        country.save()

