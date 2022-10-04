from mongoengine import *

class Country(Document):
    meta = {'collection': 'country'}
    country_id = IntField()
    name = StringField()
    capital = ListField(StringField())
    area = FloatField()
    timezone = ListField(StringField())
    independance = BooleanField()
    continents = ListField(StringField())
    un_member = BooleanField()
    languages = ListField(StringField())
    latlong = ListField(IntField())
    region = StringField()