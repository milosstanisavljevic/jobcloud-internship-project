# build api image and container
docker build ./api -t api
docker run --mount type=bind,source=/Users/milosstanisavljevic/.aws,target=/root/.aws -p 5000:5000 -d --rm api

# build crawler image and container
docker build ./crawler -t crawler
docker run --mount type=bind,source=/Users/milosstanisavljevic/.aws,target=/root/.aws -d --rm crawler