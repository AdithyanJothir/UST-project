import falcon
from models import Country 
from falcon_graphene import GrapheneRouter
import graphene 
from graphene.relay import Node,Connection,ConnectionField
from mongoengine import *
from graphene_mongo import MongoengineConnectionField,MongoengineObjectType
from graphene.types.generic import GenericScalar # solution
from graphql import GraphQLError


connect('countries')


class CountryGraph(MongoengineObjectType):
    languages = GenericScalar()
    class Meta:
        model = Country






    

class Query(graphene.ObjectType):
    country_query = graphene.List(CountryGraph,id = graphene.Int(required = True))
    countries_query = graphene.List(CountryGraph,first = graphene.Int(),skip = graphene.Int())
    countries_by_language = graphene.List(CountryGraph,lang = graphene.String(required = True))
    goodbye = graphene.String()


    def resolve_countries_query(root, info,first,skip):
        ctry = Country.objects.all()
        if skip:
            ctry  = ctry[skip:]
        if first:
            ctry = ctry[:first]
            
        return list(ctry)

    def resolve_country_query(root, info, id):
        if isinstance(id,int) == False:
            raise GraphQLError('Please enter a valid id')
        else:
            ctry = Country.objects(country_id= id)
            return list(ctry)
   
    def resolve_countries_by_language(root, info, lang):
        ctry = Country.objects(languages = lang)
        return list(ctry)

    def resolve_goodbye(root, info):
        return 'See ya!'

    

schema = graphene.Schema(query=Query)


application = falcon.API()
schema = graphene.Schema(query=Query)
router = GrapheneRouter.from_schema(schema).serving_on(application)