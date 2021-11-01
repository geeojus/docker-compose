
```
    docker build -t express-app -f Dockerfile.express-app .
```

```
    docker run -d --name express-app -p 9080:8000 -e PORT=8000 express-app

    docker run -d --name express-app -p 9081:8000 -e PORT=8000 express-app
    
    docker run --rm -it --name express-app1 -p 9081:9000 express-app bash

```