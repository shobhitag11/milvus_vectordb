## Please refer the following link to download and install Milvus: [milvus installation](https://milvus.io/docs/install_standalone-docker.md)
1. Start Docker
2. wget https://github.com/milvus-io/milvus/releases/download/v2.3.3/milvus-standalone-docker-compose.yml -O docker-compose.yml
3. Rename the milvus-standalone-docker-compose.yml file to docker-compose.yml
4. cd to the path where yaml file is downloded
5. sudo docker compose up -d
6. Check if the milvus is up and running: sudo docker compose ps
7. Connect Milvus to tcp port: docker port milvus-standalone 19530/tcp

## To view milvus dashboard, download and install attu, please refer: [attu](https://github.com/zilliztech/attu)
## Desktop Version of Attu: [Desktop Version Download](https://github.com/zilliztech/attu/releases)
9. docker run -p 8000:3000 -e MILVUS_URL={milvus server IP}:19530 zilliz/attu:v2.3.1
10. Open Browser and Visit: http://localhost:8000/#/connect

# If none of the above works, Just Install the docker-compose.yaml file from this Repo and you should be good.
