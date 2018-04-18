# docker
## remove
docker rmi [ImageID]
docker rm [containerID]
```
docker rmi -f $(docker images | grep "<none>" | awk "{print \$3}")
docker rm $(docker ps --all -q -f status=exited)
```
## tag
docker tag IMAGEID(镜像id) REPOSITORY:TAG（仓库：标签）

## start [container]
## run [image]
## fg/bg
docker attach
Ctrl+P+Q