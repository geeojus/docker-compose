
```
    docker build -t dc-nginx -f Dockerfile.nginx .
```

```
    docker run -p 8080:80 --name dc-nginx1 dc-nginx 

    docker run -it dc-nginx /bin/bash

    docker run -d --name dc-nginx2 -p 8080:80 dc-nginx

```
    docker ps

    docker ps -a

    docker stop <container_id>
```