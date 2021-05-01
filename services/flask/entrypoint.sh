#!/bin/sh

echo "Waiting for elasticsearch..."

health='down'

until [ "$health" = 'green' ] || [ "$health" = 'yellow' ]; do
  health="$(curl -fsSL "$ELASTICSEARCH_URL/_cat/health?h=status" -u "$ELASTIC_USERNAME":"$ELASTIC_PASSWORD")"
  health="$(echo "$health" | sed -r 's/^[[:space:]]+|[[:space:]]+$//g')" # trim whitespace (otherwise we'll have "green " or "yellow")
  >&2 echo "Elastic Search is unavailable - sleeping"
  sleep 1
done

>&2 echo "Elastic Search is up"
exec "$@"