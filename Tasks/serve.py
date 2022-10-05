from itertools import count
import falcon
from models import Country 
from falcon_graphene import GrapheneRouter
import graphene 
from graphene.relay import Node,Connection,ConnectionField
from mongoengine import *
from graphene_mongo import MongoengineConnectionField,MongoengineObjectType
from graphene.types.generic import GenericScalar 
from graphql import GraphQLError


connect('countries')


class CountryGraph(MongoengineObjectType):
    languages = GenericScalar()
    class Meta:
        model = Country


        
class CountryMutation(graphene.Mutation):

    class Arguments:
        country_id = graphene.Int(required = True)
        area = graphene.Float(required = True)
        region = graphene.String(required = True)
        population = graphene.Int(required =True)
    
    country = graphene.Field(CountryGraph)
    
    def mutate(self,info,area,population,region,country_id):
        country = Country.objects.get(country_id=country_id)
        country.population = population
        country.area = area
        country.region = region
        country.save()
        return CountryMutation(country = country)
        



    

class Query(graphene.ObjectType):
    country_query = graphene.Field(CountryGraph,id = graphene.Int(required = True))
    countries_query = graphene.List(CountryGraph,first  = graphene.Int(),skip = graphene.Int())
    countries_by_language = graphene.List(CountryGraph,lang = graphene.String(required = True))
    countries_nearby = graphene.List(CountryGraph,loc = graphene.List(graphene.Int))
    goodbye = graphene.String()


    def resolve_countries_query(root,info,first,skip):
        ctry = Country.objects.all()
        if skip:
            ctry = ctry[skip:]
        if first:
            ctry = ctry[:first]
        if skip and first:
            ctry = ctry[skip:skip+first]
        
        return list(ctry)

    def resolve_country_query(root, info, id):
        try:
            ctry = Country.objects.get(country_id= id)
            return ctry
        except Exception as e:
            print(e)
            raise (e)
    
    def resolve_countries_by_language(root, info, lang):
        ctry = Country.objects(languages = lang)
        
        return list(ctry)

    def resolve_countries_nearby(root, info, loc):
        ctry = Country.objects(latlong__near = loc)
        return list(ctry)

    def resolve_goodbye(root, info):
        return 'See ya!'

class Mutation(graphene.ObjectType):
    country_edit_mutation = CountryMutation.Field()





application = falcon.API()
schema = graphene.Schema(query=Query,mutation = Mutation)
try:
    router = GrapheneRouter.from_schema(schema).serving_on(application)
except Exception as e:
    print(e)
