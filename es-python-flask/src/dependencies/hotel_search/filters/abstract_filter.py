import abc
from src.model.criteria.hotel_search_criteria import HotelSearchCriteria
from elasticsearch_dsl import Q


class AbstractFilter(abc.ABC):

    @abc.abstractstaticmethod
    def create_filter(self, criteria: HotelSearchCriteria) -> Q:
        pass
