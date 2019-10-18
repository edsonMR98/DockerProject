# Sensornetwork
Microservicio que simula la transmisión de datos medidos por una red de sensores. La aplicación app.py publica mediciones de datos historicos cada cierto tiempo simulando una red de sensores

## Dockerfile
Para construir el servicio usar
```
$ docker build . -t sensornetwork:v1
```

Para correr el servicio usar
```
$ docker run -itd --name sensornetwork sensornetwork:v1
```

