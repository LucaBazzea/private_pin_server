FROM golang:1.22.1-alpine3.18

WORKDIR /app

COPY . .
RUN go mod tidy
