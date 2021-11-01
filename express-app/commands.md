
```
    docker build -t express-app -f Dockerfile.express-app .
```

```
    docker run -d --name express-app -p 8080:8000 -e PORT=8000 express-app
    
    docker run --rm -it --name express-app1 -p 8081:9000 express-app bash

```