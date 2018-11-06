# docker-selenium-hub
Hello world docker and selenium hub for win ch n ff

## environment
```
ubuntu16
```

## setup
```
Install docker compose
Clone this repository
Run parallel_test_run
```

## usage with python image
```sh
mkdir docker_tmp
cd docker_tmp
git clone https://github.com/PetrSukhov2015/docker-selenium-hub.git

sudo docker-compose up -d
#open localhost:4444 add find grid ip
sudo docker run sukhov2018/selenium:0.0.11 python parallel_test_run.py 172.17.0.1

```
where 172.17.0.1 - selenium grid server


## usage without python image
```sh
git clone https://github.com/PetrSukhov2015/docker-selenium-hub.git
docker-compose up -d
python parallel_test_run.py localhost
```
where localhost - selenium grid server

## some notes
```
sudo docker build -t sukhov2018/selenium:0.0.14 -t sukhov2018/selenium:latest --no-cache .
sudo docker push sukhov2018/selenium:0.0.14
```


      
