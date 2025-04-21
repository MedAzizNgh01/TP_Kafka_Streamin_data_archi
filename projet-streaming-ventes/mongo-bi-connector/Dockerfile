FROM ubuntu:22.04

# Installer dépendances
RUN apt-get update && apt-get install -y \
  curl \
  tar \
  libcurl4 \
  libkrb5-3 \
  libldap-2.5-0 \
  libsasl2-2 \
  libssl3 \
  ca-certificates

# Télécharger le BI Connector
RUN curl -O https://downloads.mongodb.com/bi-connector/mongodb-bi-linux-x86_64-ubuntu2204-latest.tgz && \
    tar -xvzf mongodb-bi-linux-*-latest.tgz && \
    mv mongodb-bi-linux-* /opt/mongodb-bi && \
    rm mongodb-bi-linux-*-latest.tgz

# Ajouter le fichier de config
COPY mongosqld.conf /opt/mongodb-bi/mongosqld.conf

# Définir le point d’entrée
WORKDIR /opt/mongodb-bi
CMD ["./bin/mongosqld", "--config", "mongosqld.conf"]
