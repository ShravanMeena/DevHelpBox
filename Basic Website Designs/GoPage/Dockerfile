FROM golang:alpine
RUN apk add git
RUN mkdir /app
ADD . /app/
WORKDIR /app
RUN go get -d github.com/gorilla/mux
RUN go build -o main . 
RUN adduser -S -D -H -h /app appuser
USER appuser
CMD ["./main"]

