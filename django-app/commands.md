
```
    docker build -t django-app -f Dockerfile.django-app .
```

```
    docker run -d --name django-app1 -p 7081:7000 django-app
    
```

Celery
```
    celery --help

    celery -A dc_compose worker --beat -S django -l INFO

```