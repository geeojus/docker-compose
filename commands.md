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

docker compose -f docker-compose.dev.yml up --build -d

docker compose up --build -d

docker compose up --build

docker compose down

```

Connect to DB
```
    psql -h <db_host> -p <db_port> -d <db_name> -U <username> -W
```
> `psql -h localhost -p 5432 -d dckcompose -U dcuser -W`

```
```

## Pushing to Docker Hub

### 1. Tag images for dockerhub:

Tags must be:
`docker-hub-username`/`reponame`
or
`docker-hub-username`/`reponame:v1`

Such as:

```
    docker build -t geetharg/myrepo -f Dockerfile .

    docker build -t geetharg/dockerdc-express-app -f Dockerfile.express-app .

```

or 

```
    docker build -t geetharg/myrepo:v3 -f Dockerfile .
```

or

```
    docker image ls
```
I have an image with the id of `c762835ed3ea` that I am going to tag to `geetharg/dockerdc-express-app:v1.0`

```
    docker tag c762835ed3ea geetharg/dockerdc-express-app:v1
```

The format is 
```
    docker tag <built-image-id> <new-tag>
```

### 2. Push with new tag:

```
    docker push <new-tag>
```

like

```
    docker push geetharg/dockerdc-express-app:v1
```