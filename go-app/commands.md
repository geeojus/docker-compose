
```
    docker build -t go-app -f Dockerfile.go-app .
```

```
    docker run -d --name go-app -p 8090:8000 -e PORT=8000 go-app

    docker run -d --name go-app -p 8090:8000 -e PORT=8000 go-app
    
    docker run --rm -it --name go-app1 -p 8090:9000 go-app bash

```

```
   go commandline in container : 
   
   which go

   PORT=1234 go run server.go
```