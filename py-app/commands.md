
```
    docker build -t py-app1 -f Dockerfile.py-app .
```

```
    docker run -d --name py-app1-c1 -p 8081:8000 py-app1

    docker run -d --name py-app1-c2 -p 8082:8000 py-app1

    docker run -d --name pyapp1 -p 8081:8000 -e PORT=8000 -v pyappvol:/app/data docker-compose_py-app 
    
    docker run -d --name pyapp2 -p 8082:8001 -e PORT=8001 -v pyappvol:/app/data docker-compose_py-app 
    
```