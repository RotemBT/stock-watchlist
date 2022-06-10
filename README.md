
# Stock-watchlist-microservices-project

Stock Watchlist is a platform that you can add stocks to you watch list, you will see the price value of each stock real-time and get real-time news who related to those stocks in you watch list.

### Project Architecture

#### backend-service
1. Get request from the frontend which stocks to watch and send it to redis.
2. Get real-time data from redis and send it to frontend.

#### stream-service
1. Get data from redis which stock to watch.
2. Send request to alpaca api.
3. Get response from alpaca and send to redis.

#### frontend-service
1. The UI and visualization of the data.
2. Send request to backend service to add/ remove stock.
3. Visualize the data.

![microservices drawio](https://user-images.githubusercontent.com/68068799/165177776-6bb1cbc0-b019-4490-b7cb-cf395e96006d.png)

## Getting started
First clone the project using 
`https://github.com/EASS-HIT-2022/stock-watchlist.git`
or
`gh repo clone EASS-HIT-2022/stock-watchlist`

### run with docker
Install Docker [click here to install](https://docs.docker.com/engine/install/ubuntu/)
Run services: 
1. Stream-service
```
cd stream-service
docker build . -t stream-service
docker run -ti -p 8888:8086 stream-service
```
Then got to [localhost:8888](http://localhost:8888/)

2. Backend-service
```
cd backend-service
docker build . -t backend-service
docker run -ti -p 8088:8085 backend-service
```
Then got to [localhost:8088](http://localhost:8088/)

3. Frontend-service
```
cd frontend-service
docker build . -t frontend-service
docker run -ti -p 3000:3000 frontend-service
```
Then got to [localhost:3000](http://localhost:3000/)
## TODO

- [X] backend side
- [ ] connect between backend services
- [ ] connect to redis
- [X] frontend side
- [ ] docker compose
- [ ] make a video
- [ ] Finish readme    
 
