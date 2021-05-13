import graphene


class PageInfo(graphene.ObjectType):
    hasPrevPage = graphene.Boolean()
    hasNextPage = graphene.Boolean()


class MappedCountry(graphene.ObjectType):
    id = graphene.String()
    name = graphene.String()
    metaId = graphene.String()
    alpha2Code = graphene.String()
    capital = graphene.String()
    population = graphene.Int()
    region = graphene.String()
    flag = graphene.String()


class CountryConnection(graphene.ObjectType):
    nodes = graphene.List(MappedCountry)
    pageInfo = graphene.Field(PageInfo)


class CountrySearchError(graphene.ObjectType):
    message = graphene.String()


class CountrySearchResponse(graphene.Union):
    class Meta:
        types = (CountryConnection, CountrySearchError)
