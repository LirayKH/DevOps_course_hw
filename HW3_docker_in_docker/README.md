# Build customized Image
1. Docker build kutsegor/docker
```
docker build -t kutsegor/docker:latest .
```

2. Run docker container using docker.sock inside of container
(Original article: http://jpetazzo.github.io/2015/09/03/do-not-use-docker-in-docker-for-ci/#:~:text=And%20the%20simplest%20way%20is,%3A%2Fvar%2Frun%2Fdocker.)

```
docker run -v /var/run/docker.sock:/var/run/docker.sock -it kutsegor/docker:latest
```
or run Run docker container using docker.sock inside of container and mount dockerfiles folder with prepared Dockerfiles:
```
docker run --name ekuts_docker \
           -v /var/run/docker.sock:/var/run/docker.sock \
           -v /home/kuts/Work/Docker/zone3000/DevOps_course_hw/HW3_docker_in_docker/dockerfiles:/dockerfiles \
           -p 7000:7000 \
           -it kutsegor/docker:latest
```
3. Login inside to container with docker:
```
docker exec -it ekuts_docker bash
```

4. Build and Run container inside of the docker:
```
docker exec -i ekuts_docker sh <<< "docker build -f Python.Dockerfile -t kutsegor/python_server ."
docker exec -i ekuts_docker sh <<< "docker run --name python_server -it kutsegor/python_server"

```
