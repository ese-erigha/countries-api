from mongoengine import connect


def auto_connect(app_config, mode):
    if mode == "local":
        connect(db=app_config["DB_NAME"], host=app_config["DB_HOST"])  # localhost
    else:
        connection_string = "mongodb://{username}:{password}@{host}:{port}/{db_name}?authSource=admin". \
            format(username=app_config["DB_USERNAME"], password=app_config["DB_PASSWORD"], host=app_config["DB_HOST"],
                   port=app_config["DB_PORT"], db_name=app_config["DB_NAME"])
        connect(host=connection_string)
