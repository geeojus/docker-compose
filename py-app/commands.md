
```
    docker build -t py-app1 -f Dockerfile.py-app .
```

```
    docker run -d --name py-app1-c1 -p 8080:8000 py-app1
    
```