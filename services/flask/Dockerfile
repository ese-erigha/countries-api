# pull official base image
FROM python:3.8.1-slim-buster

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
# ENV GROUP_ID 1000
# ENV USER_ID 1000

# install system dependencies
RUN apt-get update && apt-get install -y netcat

# RUN addgroup --gid $GROUP_ID app
# RUN adduser --uid $USER_ID --gid $GROUP_ID app app --shell /bin/sh

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt /usr/src/app/requirements.txt
RUN pip install -r requirements.txt

# copy project
COPY . /usr/src/app/

CMD ["gunicorn", "--config", "./gunicorn_config.py", "manage:app"]

# change to the app user
# USER www

# run entrypoint.sh
# ENTRYPOINT ["/usr/src/app/entrypoint.sh"]
