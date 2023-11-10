FROM debian:bullseye-slim
RUN mkdir /api-peliculas

WORKDIR /api-peliculas

RUN apt-get update && \
    apt-get install -y curl python3-pip && \
    rm -rf /var/lib/apt/lists/*

COPY . /api-peliculas/

RUN pip3 install --upgrade pip && \
    pip3 install -r requirements.txt

ENV FLASK_APP "entrypoint:app"
ENV FLASK_ENV "development"
ENV APP_SETTINGS_MODULE  "config.default"
ENV PORT 5000

RUN flask db init 
RUN flask db revision --rev-id 0e7ad55e9a3f
RUN flask db migrate
RUN flask db upgrade

EXPOSE ${PORT}

CMD ["flask", "run", "--host", "0.0.0.0"]



