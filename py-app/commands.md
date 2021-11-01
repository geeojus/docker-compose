
```
    docker build -t py-app1 -f Dockerfile.py-app .
```

```
    docker run -d --name py-app1-c1 -p 8081:8000 py-app1

    docker run -d --name py-app1-c2 -p 8082:8000 py-app1
    
```