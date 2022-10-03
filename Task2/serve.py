import falcon

from falcon_graphene import GrapheneRouter

from graphene import ObjectType,String,Schema,JSONString,Int
import graphene

from mongoengine import *

connect('countries')

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


class Query(ObjectType):
    countriesQuery = JSONString()
    countryQuery = JSONString(id = Int(required=True))
    goodbye = String()

    def resolve_countriesQuery(root, info):
        
        ctry = Country.objects()
        json_response = ctry.to_json()
        return json_response

    def resolve_countryQuery(root, info, id):
        
        ctry = Country.objects(country_id=id).first()
        json_response = ctry.to_json()
        return json_response



    def resolve_goodbye(root, info):
        return 'See ya!'

schema = Schema(query=Query)


application = falcon.API()
schema = graphene.Schema(query=Query)
router = GrapheneRouter.from_schema(schema).serving_on(application)