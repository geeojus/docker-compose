```
    docker compose build --no-cache
```

```
    docker compose up
```

```
    docker compose down

    
```

Delete all images
```
    docker rmi -f $(docker images -a -q)
```


Delete all containers
```
    docker rm -f $(docker ps -a -q)
```

Volume
```
    docker volume ls
```

Automated Volume Creation
```
    docker run -d --name <container_name> -v <volume_name>:<mount_path_on_container> <image_name>    
```
> `docker run -d --name pyapp1 -p 8081:8000 -e PORT=8000 -v pyappvol:/app/data docker-compose_py-app`


Manual Volume Creation
```
    docker run -d --name <container_name> -v <path_of_folder>:<mount_path_on_container> <image_name>
```
> `docker run -d --name pyapp1 -p 8081:8000 -e PORT=8000 -v /Users/geetharg/Documents/Training/CFE/DockerCompose/docker-compose/data:/app/data docker-compose_py-app`
