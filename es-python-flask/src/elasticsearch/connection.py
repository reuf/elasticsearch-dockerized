from src.common.helpers.yaml_manager import YamlManager
from elasticsearch_dsl import connections


class Connection:

    @staticmethod
    def create_connection() -> connections:
        hosts = YamlManager.read_yaml_content('parameters.yaml')['elasticsearch']['hosts']
        return connections.create_connection(hosts=hosts)
