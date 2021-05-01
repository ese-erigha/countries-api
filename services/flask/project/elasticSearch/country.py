from elasticsearch_dsl import Document, Long, Keyword, Text, Index
from elasticsearch_dsl.query import MatchPhrasePrefix, Term, Bool, Match
from project.dto.country import CountryConnection

countryIndex = Index('country')


@countryIndex.document
class CountryESModel(Document):
    id = Keyword()
    name = Text(fields={'raw': Keyword()})
    alpha2Code = Keyword()
    capital = Text()
    population = Long()
    region = Keyword()


def init_index():
    # delete the index, ignore if it doesn't exist
    countryIndex.delete(ignore=404)

    countryIndex.settings(number_of_shards=1)
    countryIndex.create()


def index_country(data):
    CountryESModel(
        meta={'id': data['id']},
        id=data['id'],
        name=data['name'],
        alpha2Code=data['alpha2Code'],
        capital=data['capital'],
        population=data['population'],
        region=data['region']
    ).save()

    # refresh index manually to make changes live
    countryIndex.refresh()


class CountrySearch:
    def __init__(self):
        pass

    @classmethod
    def compute_limit(cls, start_index):
        page_size = 10
        return page_size + start_index

    @classmethod
    def compute_next_page(cls, total, limit):
        if total == 0:
            return False
        return limit < total

    @classmethod
    def compute_prev_page(cls, offset):
        return int(offset) > 0

    @classmethod
    def build_query(cls, name, region):
        query = ''
        if name and region is None:
            query = Bool(
                should=[
                    MatchPhrasePrefix(name={"query": name}),
                    Match(name={"query": name, "fuzziness": "AUTO"}),
                ],
            )

        if name is None and region:
            query = Term(region={"value": region})

        if name and region:
            query = Bool(
                must=[
                    Match(name={"query": name, "fuzziness": "AUTO"}),
                    MatchPhrasePrefix(name={"query": name}),
                    Term(region={"value": region})
                ],
            )

        return query

    @classmethod
    def search(cls, searchInput):
        name = searchInput.get('name')  # optional field
        region = searchInput.get('region')  # optional field
        start_index = searchInput.get('offset')
        limit = cls.compute_limit(start_index)
        query = cls.build_query(name, region)
        s = CountryESModel.search()
        results = s[start_index:limit].query(query).execute()
        has_next_page = cls.compute_next_page(results.hits.total.value, limit)
        has_previous_page = cls.compute_prev_page(start_index)
        mapped_country_list = [country.to_dict() for country in results]
        page_info = {
                "hasPrevPage": has_previous_page,
                "hasNextPage": has_next_page
        }
        return CountryConnection(nodes=mapped_country_list, pageInfo=page_info)
