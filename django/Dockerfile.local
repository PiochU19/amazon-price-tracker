ARG PYTHON_VERSION=3.9.5-alpine

###########
# BUILDER #
###########

# define an alias
FROM python:${PYTHON_VERSION} as python

# Python build stage
FROM python as python-build-stage

RUN apk update

# install psycopg2 dependencies
RUN apk add \
    postgresql-dev \
    gcc python3-dev \
    musl-dev

# Argon2 dependencies
RUN apk add \
    argon2 \
    libffi-dev

# # lxml dependencies
# RUN apk add \
#     libxml2 \
#     libxslt \
#     libxslt-dev

# install dependencies
RUN pip install --upgrade pip

# Requirements are installed here to ensure they will be cached
COPY ./requirements.txt .

# install wheels
RUN pip wheel --no-cache-dir --no-deps --wheel-dir /usr/src/backend/wheels -r requirements.txt

#######
# RUN #
#######

FROM python as python-run-stage

ARG APP_HOME=/amazon_price_tracker

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

WORKDIR ${APP_HOME}

# install dependencies
RUN apk update && apk add libpq
COPY --from=python-build-stage /usr/src/backend/wheels  /wheels/

# use wheels to install python dependencies
RUN pip install --no-cache-dir --no-index --find-links=/wheels/ /wheels/* \
    && rm -rf /wheels/

COPY . ${APP_HOME}

RUN ["chmod", "+x", "/amazon_price_tracker/entrypoint.sh"]

ENTRYPOINT ["/amazon_price_tracker/entrypoint.sh"]