FROM python:3.10-slim

WORKDIR /usr/app

RUN apt-get update && apt-get install -y git

RUN pip install --upgrade pip \
    && pip install dbt-core dbt-snowflake

COPY . .

ENV DBT_PROFILES_DIR=/usr/app/.dbt

CMD ["dbt", "--help"]
