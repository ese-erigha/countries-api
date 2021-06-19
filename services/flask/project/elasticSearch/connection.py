from elasticsearch_dsl.connections import connections


def connect(app_config, mode):
    elastic_host = app_config["ELASTICSEARCH_HOST"]
    if mode == "local":
        connections.create_connection(hosts=[elastic_host])
    else:
        elastic_auth = "{username}:{password}".format(username=app_config["ELASTIC_USERNAME"],
                                                      password=app_config["ELASTIC_PASSWORD"])
        connections.create_connection(hosts=[elastic_host], http_auth=elastic_auth)
