imageName=testcontainer:${BUILD_NUMBER}
containerName=testcontainer
PORT=5005

docker system prune -af
docker build -t $imageName .
docker stop $containerName || true && docker rm -f $containerName || true
docker run -p $PORT:$PORT -d --name $containerName $imageName

# python3 aissurance.py
