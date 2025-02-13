imageName=staitus:${BUILD_NUMBER}
containerName=staitus
PORT=5003
DOCKER_GID=$(stat -c "%g" /var/run/docker.sock)

docker system prune -af
docker build -t $imageName .
docker stop $containerName || true && docker rm -f $containerName || true
# Read-only access to Docker, Persistent logs, Match the docker group GID
docker run -p $PORT:$PORT -d --name $containerName -v /var/run/docker.sock:/var/run/docker.sock:ro -v $(pwd)/logs:/logs --group-add $DOCKER_GID $imageName
