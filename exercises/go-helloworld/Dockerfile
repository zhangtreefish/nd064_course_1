FROM golang:alpine
LABEL maintainer="shuyu"

WORKDIR /go/src/app
COPY . .
RUN go mod init
RUN go build -o helloworld

# command to run on container start
CMD [ "./helloworld" ]