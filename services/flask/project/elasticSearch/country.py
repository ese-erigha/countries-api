from elasticsearch_dsl import Document, Long, Keyword, Text, Index
from project.dto.country import CountryConnection
from project.elasticSearch.query_builder import QueryBuilder

countryIndex = Index('country')


@countryIndex.document
class CountryESModel(Document):
    id = Keyword()
    name = Text(fields={'raw': Keyword()})
    metaId = Keyword()
    alpha2Code = Keyword()
    capital = Text()
    population = Long()
    region = Keyword()
    flag = Text()


def init_index():
    # delete the index, ignore if it doesn't exist
    countryIndex.delete(ignore=404)

    countryIndex.settings(number_of_shards=1)
    countryIndex.create()


def index_country(data):
    CountryESModel(
        meta={'id': data['id']},
        id=data['id'],
        metaId=data['metaId'],
        name=data['name'],
        alpha2Code=data['alpha2Code'],
        capital=data['capital'],
        population=data['population'],
        region=data['region'],
        flag=data['flag']
    ).save()

    # refresh index manually to make changes live
    countryIndex.refresh()


class CountrySearch:
    def __init__(self):
        pass

    @classmethod
    def compute_limit(cls, start_index):
        page_size = 12
        return page_size + start_index

    @classmethod
    def has_next_page(cls, total, limit):
        if total == 0:
            return False
        return limit < total

    @classmethod
    def has_prev_page(cls, offset):
        return int(offset) > 0

    @classmethod
    def search(cls, searchInput):
        start_index = searchInput.get('offset')
        limit = cls.compute_limit(start_index)
        query = QueryBuilder(searchInput).build()
        s = CountryESModel.search()
        results = s[start_index:limit].query(query).execute()
        mapped_country_list = [country.to_dict() for country in results]
        page_info = {
            "hasPrevPage": cls.has_prev_page(start_index),
            "hasNextPage": cls.has_next_page(results.hits.total.value, limit)
        }
        return CountryConnection(nodes=mapped_country_list, pageInfo=page_info)
