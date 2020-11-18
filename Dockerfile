FROM python:3.9.0-alpine

ARG PORT

WORKDIR /app

COPY . .

RUN apk add make && make install

EXPOSE ${PORT}

CMD ["make", "run"]