# Udemy Sergii Demianchuk PYTHON ElasticSearch Example

## Setup

1. Set connection to ElasticSEarch at **parameters.yml** in case modifications from docker compose side

2. Run docker compose to bring docker environment: _docker-compose up -d_

3. site is available on http://localhost:56733/test

####How to fill elasticsearch with test data
docker exec -it udemy_python_app python src/command/fill_elasticsearch.py

###How to stop and remove container
docker-compose stop

###How to check logs
docker logs udemy_python_app -f
tail -f /var/log/uwsgi.log (inside container)

###How to refresh code
docker exec -it udemy_python_app touch uwsgi.ini

###How to test search:
1. Using swagger ui: http://localhost:56733/swagger-ui/

2. Manually using direct url:
   http://localhost:56733/hotels/search?size=10&n=star&lat=52.21&page=1&lng=21.01&age=5&c=warsaw&fpn=true
   
###How to check coding standards
docker exec -it udemy_python_app flake8

###How to run tests
docker exec -it udemy_python_app pytest -s

#### Pytest, Mock documentation:
- https://docs.pytest.org/
- https://mock.readthedocs.io/
