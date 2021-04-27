#!/bin/sh




echo "Waiting for elasticsearch..."

health='down'

until [ "$health" = 'green' ] || [ "$health" = 'yellow' ]; do
  health="$(curl -fsSL "$ELASTICSEARCH/_cat/health?h=status")"
  health="$(echo "$health" | sed -r 's/^[[:space:]]+|[[:space:]]+$//g')" # trim whitespace (otherwise we'll have "green ")
  >&2 echo "Elastic Search is unavailable - sleeping"
  sleep 1
done

>&2 echo "Elastic Search is up"
exec "$@"