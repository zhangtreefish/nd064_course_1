# Go Hello World

This is a simple Go web application that prints a "Hello World" message.

## Run the application

This application listens on port `6111`

To run the application, use the following command(if go is downlaoded):
```
go run main.go 
```
If go is not on the machine, run on an interactive go docker:
```
docker run -it --name go-helloword -p 6111:6111 -v $PWD:/mnt golang:1.11.13-alpine3.10 sh` // start a go docker
cd /mnt
ls //should see main.go
go run main.go 
```
Once verified that the app runs, exit the docker; and 
```
docker build -t go-helloworld .
docker images
docker tag go-helloworld:latest treefishdocker/go-helloworld:v1.0.0
docker images//should see the newly created image at dockerhub
docker push treefishdocker/go-helloworld:v1.0.0
```

Access the application on: http://127.0.0.1:6111/
## References
https://stackoverflow.com/questions/24958140/what-is-the-difference-between-the-copy-and-add-commands-in-a-dockerfile
