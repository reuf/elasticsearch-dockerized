from marshmallow import Schema, fields
from elasticsearch_dsl.response import Hit


class HotelSearchSimpleItemSchema(Schema):
    name = fields.Str()
    star = fields.Int()

    @staticmethod
    def create_item_from_es_response(hotel: Hit):
        return {"name": hotel.name, "star": hotel.stars}
