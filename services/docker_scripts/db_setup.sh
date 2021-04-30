#!/bin/sh

USER_COUNT=mongo "${MONGO_INITDB_DATABASE}" \
        --host localhost \
        --port "${MONGO_PORT}" \
        -u "${MONGO_INITDB_ROOT_USERNAME}" \
        -p "${MONGO_INITDB_ROOT_PASSWORD}" \
        --authenticationDatabase admin \
        --eval "db.system.users.find({user: '${DATABASE_USERNAME}'}).count();"

if [ "$USER_COUNT" -eq 0 ]; then
  echo 'Creating application user and db'

  mongo "${MONGO_INITDB_DATABASE}" \
        --host localhost \
        --port "${MONGO_PORT}" \
        -u "${MONGO_INITDB_ROOT_USERNAME}" \
        -p "${MONGO_INITDB_ROOT_PASSWORD}" \
        --authenticationDatabase admin \
        --eval "db.createUser({user: '${DATABASE_USERNAME}', pwd: '${DATABASE_PASSWORD}', roles:[{role:'dbOwner', db: '${MONGO_INITDB_DATABASE}'}]});"

fi

