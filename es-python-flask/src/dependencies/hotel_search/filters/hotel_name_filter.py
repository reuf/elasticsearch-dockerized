from src.dependencies.hotel_search.filters.abstract_filter import AbstractFilter
from src.model.criteria.hotel_search_criteria import HotelSearchCriteria
from elasticsearch_dsl import Q


class HotelNameFilter(AbstractFilter):
    @staticmethod
    def create_filter(criteria: HotelSearchCriteria) -> Q:
        q_res = Q("match", name={"query": criteria.hotel_name})

        return q_res
