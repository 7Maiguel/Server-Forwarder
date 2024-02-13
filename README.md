# CONFIG  
Create in the server environment variables with same structure like are showed in file .env.example
# RUN
cd .
docker build --tag fuse-server-forward-img . \
echo 'y' | docker container prune \
docker run --network host --env-file .env --name fuse-server-forward fuse-server-forward-img