from abc import ABC, abstractmethod
from elasticsearch_dsl import query
from elasticsearch_dsl.query import MatchPhrasePrefix, Term, Bool, Match, MatchAll


class QueryBuilderStrategy(ABC):

    def __init__(self, searchInput):
        self.name = searchInput.get('name')
        self.region = searchInput.get('region')

    @abstractmethod
    def check(self) -> bool:
        pass

    @abstractmethod
    def build(self) -> query:
        pass


class NameQueryBuilderStrategy(QueryBuilderStrategy):
    def __init__(self, searchInput):
        super().__init__(searchInput)

    def check(self):
        state = False
        if self.name and self.region is None:
            state = True
        return state

    def build(self):
        return Bool(
            should=[
                MatchPhrasePrefix(name={"query": self.name}),
                Match(name={"query": self.name, "fuzziness": "AUTO"}),
            ],
        )


class RegionQueryBuilderStrategy(QueryBuilderStrategy):
    def __init__(self, searchInput):
        super().__init__(searchInput)

    def check(self):
        state = False
        if self.region and self.name is None:
            state = True
        return state

    def build(self):
        return Term(region={"value": self.region})


class NameAndRegionQueryBuilderStrategy(QueryBuilderStrategy):
    def __init__(self, searchInput):
        super().__init__(searchInput)

    def check(self):
        state = False
        if self.name and self.region:
            state = True
        return state

    def build(self):
        return Bool(
            must=[
                Match(name={"query": self.name, "fuzziness": "AUTO"}),
                MatchPhrasePrefix(name={"query": self.name}),
                Term(region={"value": self.region})
            ],
        )


class QueryBuilder:
    def __init__(self, searchInput):
        self.strategies = [
            NameQueryBuilderStrategy(searchInput),
            RegionQueryBuilderStrategy(searchInput),
            NameAndRegionQueryBuilderStrategy(searchInput),
        ]

    def build(self):
        strategy = next((strategy for strategy in self.strategies if strategy.check() is True), None)
        if strategy is None:
            return MatchAll()
        return strategy.build()
