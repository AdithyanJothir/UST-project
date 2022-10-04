import falcon
from models import Country 
from falcon_graphene import GrapheneRouter
import graphene
from graphene.relay import Node
from mongoengine import *
from graphene_mongo import MongoengineConnectionField,MongoengineObjectType
from graphene.types.generic import GenericScalar # solution



connect('countries')


class CountryGraph(MongoengineObjectType):
    languages = GenericScalar()
    class Meta:
        model = Country





# class CountriesConenction(relay.Connection):
#     class Meta:
#         node  = Country
#     class Edge:
#         other  = 

    

class Query(graphene.ObjectType):
    # country_query = 
    countries_query = graphene.List(CountryGraph)
    goodbye = graphene.String()


    def resolve_countries_query(root, info):
        ctry = Country.objects.all()
        return list(ctry)

    # def resolve_country_query(root, info, id):
    #     ctry = Country.objects(country_id=id).first()
    #     return ctry
        



    def resolve_goodbye(root, info):
        return 'See ya!'

    

schema = graphene.Schema(query=Query)


application = falcon.App()
schema = graphene.Schema(query=Query)
router = GrapheneRouter.from_schema(schema).serving_on(application)