
# Stock-watchlist-microservices-project

Stock Watchlist is a platform that you can add stocks to you watch list, you will able to get news and bar from current year who related to those stocks in you watch list.
[Link to video](https://youtu.be/hUi-NHNOa5A)
### Project Architecture

#### backend-service
1. Get request from the frontend which stocks to watch.
2. Get data from alpaca-api and send it to frontend.

#### frontend-service
1. The UI and visualization of the data.
2. Check if the requested data is in redis cache if not send request to backend service.
3. Visualize the data.

![microservices drawio](https://user-images.githubusercontent.com/68068799/173195341-df7f4021-9a8b-4dd1-b9d1-7a89fcc05c3f.png)

## Getting started
First clone the project using 
`https://github.com/EASS-HIT-2022/stock-watchlist.git`
or
`gh repo clone EASS-HIT-2022/stock-watchlist`

### run with docker
Install Docker [click here to install](https://docs.docker.com/engine/install/ubuntu/)
Run services: 

1. Backend-service
```
cd backend-service
docker build . -t backend-service
docker run -ti -p 8088:8085 backend-service
```
Then got to [localhost:8088](http://localhost:8088/)

2. Frontend-service
```
cd frontend-service
docker build . -t frontend-service
docker run -ti -p 3000:3000 frontend-service
```
Then got to [localhost:3000](http://localhost:3000/)

3. Redis cache

### run with docker compose

``` 
docker-compose up 
```
