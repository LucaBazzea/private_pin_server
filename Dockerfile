FROM golang:1.22.1-alpine3.18

WORKDIR /app

RUN go install github.com/cosmtrek/air@latest

COPY . .
RUN go mod tidy
