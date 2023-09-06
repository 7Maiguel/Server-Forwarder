# CONFIG  
Create in the server environment variables with same structure like are showed in file .env.example
# RUN
docker build --tag fuse-server-forward-img .  \
docker run --env-file .env --name fuse-server-forward -it fuse-server-forward-img
