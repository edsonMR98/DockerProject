# Stats
API para el cálculo de medidas de estadística descriptiva desarrollado en R y con docker :whale:

## Contrucción
```
$ docker build . -t stats:v1
```

## Ejecución
```
$ docker run -it --name stats_api -p 3030:8000 --rm --mount type=bind,source="$(pwd)"/stats,target=/usr/local/src/stats stats:v1 
```

# Referencia de la API

## Stats API
### http://localhost:3030/api/v1/

## Describe
### POST
Obten las medidas descriptivas básicas de un conjunto de datos
```
http://localhost:3030/api/v1/describe?columns=Temperatura
```
#### Parametros
| Parametro | Descripción                                            | Ejemplo                             |
|-----------|--------------------------------------------------------|-------------------------------------|
| columns   | Define de cuales columnas obtener el resumen, 'Todas' por defecto      | `?columns=Temperatura,C02,altitude` |
#### Objecto Request
```
{
    "data": [
        {"Date": "2016-12-06", "Temperatura": 0.7895, "Source": "GCAG"},
        {"Date": "2016-12-06", "Temperatura": 0.81, "Source": "GISTEMP"},
        {"Date": "2016-11-06", "Temperatura": 0.7504, "Source": "GCAG"},
        {"Date": "2016-11-06", "Temperatura": 0.93, "Source": "GISTEMP"},
        {"Date": "2016-10-06", "Temperatura": 0.7292, "Source": "GCAG"},
        {"Date": "2016-10-06", "Temperatura": 0.89, "Source": "GISTEMP"},
        {"Date": "2016-09-06", "Temperatura": 0.8767, "Source": "GCAG"},
        {"Date": "2016-09-06", "Temperatura": 0.87, "Source": "GISTEMP"},
        {"Date": "2016-08-06", "Temperatura": 0.8998, "Source": "GCAG"}
    ]
}
```
#### Objecto Response
```
{
    "summary": {
        "Temperatura": {
            "length": 0,
            "columns": 0,
            "min": 0,
            "max": 0,
            "mean": 0,
            "median": 0,
            "mode": 0,
            "range": 0,
            "var": 0,
            "sd": 0,
            "quantile": {
                "0": 0.0,
                "25": 0.0,
                "75": 0.0,
                "100": 0.0
            }
        }
    }
}
```

## Correlation
### POST
Obtiene varianza, desviación estandar, covarianza y coeficiante de correlación de un conjunto de datos
```
http://localhost:3030/api/v1/correlation?columns=test,Temperature
```
#### Parametros
| Parametro | Descripción                                            | Ejemplo                             |
|-----------|--------------------------------------------------------|-------------------------------------|
| columns   | Define las columnas a obtener cor y cov, todas por defecto      | `?columns=test,Temperature` |
| method   | Define el método para obtener la correlación ('pearson', 'kendall', 'spearman'), 'pearson' por defecto    | `?method=pearson` |
#### Objeto Request
```
{
    "data": [
        {"Date": "2016-12-06", "Radiation":0.23, "test":34, "Temperature": 0.7895, "Source": "GCAG"},
        {"Date": "2016-11-06", "Radiation":0.64, "test":30, "Temperature": 0.7504, "Source": "GCAG"},
        {"Date": "2016-10-06", "Radiation":0.18, "test":35, "Temperature": 0.7292, "Source": "GCAG"},
        {"Date": "2016-05-06", "Radiation":0.73, "test":30, "Temperature": 0.93, "Source": "GISTEMP"},
        {"Date": "2016-04-06", "Radiation":0.65, "test":24, "Temperature": 1.0733, "Source": "GCAG"},
        {"Date": "2016-04-06", "Radiation":0.61, "test":31, "Temperature": 1.09, "Source": "GISTEMP"},
        {"Date": "2016-03-06", "Radiation":0.53, "test":30, "Temperature": 1.2245, "Source": "GCAG"},
        {"Date": "2016-03-06", "Radiation":0.89, "test":11, "Temperature": 1.3, "Source": "GISTEMP"}
    ]
}
```
#### Objeto Response
```
{
  "correlation": {
    "size": 73,
    "variables": "test,Temperature",
    "covariance": 17.0051,
    "correlation": 0.7767,
    "correlationMethod": "pearson",
    "variance": {
      "test": 36.0638,
      "Temperature": 13.4418
    },
    "standarDeviation": {
      "test": 6.0053,
      "Temperature": 3.6663
    }
  }
}
```
Más de dos columnas regresa una matriz de correlación y covarianzas, Objeto Response de `http://localhost:3030/api/v1/correlation?columns=test,Radiation,Temperature`:
```
...
"correlation": [
      {
        "test": 1,
        "Radiation": -0.7728,
        "Temperature": -0.7186,
        "_row": "test"
      },
      {
        "test": -0.7728,
        "Radiation": 1,
        "Temperature": 0.656,
        "_row": "Radiation"
      },
      {
        "test": -0.7186,
        "Radiation": 0.656,
        "Temperature": 1,
        "_row": "Temperature"
      }
    ]
...
```

