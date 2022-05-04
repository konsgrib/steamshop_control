FROM postgres

ENV POSTGRES_PASSWORD password#1

ENV POSTGRES_DB app

ENV POSTGRES_USER user

# COPY world.sql /docker-entrypoint-initdb.d/
VOLUME  ["./data/postgresql", "/var/log/postgresql", "/var/lib/postgresql"]

# PGDATA /var/lib/postgresql/data

EXPOSE 5432

