from elasticsearch_dsl import InnerDoc, Text, Integer, Date


class Comment(InnerDoc):
    hotel_id = Integer()
    content = Text()
    stars = Integer()
    created_at = Date()
