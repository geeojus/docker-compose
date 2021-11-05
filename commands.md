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


### Databases
Postgresql
```
docker pull postgres:latest
```

```
docker run --name postgres -p 6543:5432 -e POSTGRES_USER=myuser -e POSTGRES_PASSWORD=mytestpw postgres

docker run --name postgres -p 6543:5432 --env-file .env postgres
```

Connect to DB
```
    psql -h <db_host> -p <db_port> -d <db_name> -U <username> -W
```
> `psql -h localhost -p 5432 -d dc-compose -U dcuser -W`

