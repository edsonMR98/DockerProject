# Verificador
Microservicio que limpia y verifica mediciones de sensores en tiempo real recibidas desde un topic de mqtt
La aplicación verificador.app recibe las mediciones y les aplica funciones de limpieza y verificación para validar que los datos esten dentro de los rangos aceptables y cumplan con los estandares de validación.

## Dockerfile
Para construir el servicio usar
```
$ docker build . -t verificador:v1
```

Para correr el servicio usar
```
$ docker run -itd --name verificador verificador:v1
```

