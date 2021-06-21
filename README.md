# Countries API


A dockerized Flask GraphQL API that provides information about countries of the world. A modified version (in a private repo) that powers [Countries Browser](https://countries.eseerigha.com/countries) has been deployed to AWS (ECS, ECR, EC2) via github actions.


Application provides the following features:

* Filter countries based on regions - Africa, Europe, America e.t.c
* Search for country
* View country details

Development:

* [docker-compose](https://docs.docker.com/compose/)
* [docker](https://docs.docker.com/get-started/overview/)
* [python](https://hub.docker.com/_/python)
* [Flask](https://flask.palletsprojects.com/en/2.0.x/)
* [Nginx](https://hub.docker.com/_/nginx)
* [ElasticSearch](https://hub.docker.com/_/elasticsearch)
* [Kibana](https://hub.docker.com/_/kibana)
* [Logstash](https://hub.docker.com/_/logstash)
* [Mongo](https://hub.docker.com/_/mongo)
* [Mongo Express](https://hub.docker.com/_/mongo-express)


## Getting Started

### Prerequisites
* Install [Docker](https://docs.docker.com/get-docker/)
* Install [Docker-Compose](https://docs.docker.com/compose/install/)

### Installing
Clone the repository
```
git clone https://github.com/eseerigha/countries-api.git
```
Configure environment variables
```
Create a env.dev file in the application root
```
Add configs specified in the environment variables of docker-compose services to the env.dev file such as the example below
```
MONGO_HOST=<insert value>
```

### Running application

Development Environment:

Setup Authentication keys to enable secure connection between ElasticSearch and Kibana,Logstash
```
docker-compose --f docker-compose.setup.yml --env-file env.dev run --rm keystore
docker-compose --f docker-compose.setup.yml --env-file env.dev run --rm certs
```

Run services
```
docker-compose --f docker-compose.yml --env-file env.dev up  --build
```

Load data via POST REQUEST
```
HEADERS = {Authorization: <auth token from dev.env config>}
http://localhost:500/country/data/load
```

View API Schema
```
http://localhost:500/graphql
```

## License
This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

