import graphene


class MappedCountry(graphene.ObjectType):
    id = graphene.String()
    name = graphene.String()
    alpha2Code = graphene.String()
    capital = graphene.String()
    population = graphene.Int()
    region = graphene.String()
