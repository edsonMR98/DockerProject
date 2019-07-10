import json

def validar(m, r):
    """ Valida el mensaje recibido por MQTT.\n
        m: Mensaje recibido por MQTT (payload)\n
        r: Json usado para tomar las referencias de las mediciones\n
        return: Mensaje (json) validado """
    data = toDict(m)
    rangos = r

    banderaLimpieza(data, rangos)
    print(data)
    
def toDict(fileBytes):
    """ Convertir un dato tipo bytes to dict.\n
        fileBytes: mensaje tipo bytes a convertir """
    fileStr = str(fileBytes.decode("utf-8"))
    return json.loads(fileStr)

def banderaLimpieza(data, rangos):
    """ Agrega la bandera de limpieza a cada medicion.\n
    data: Mensaje\n
    rangos: Json usado para tomar las referencias de las mediciones"""
    for d in data["mediciones"]:        
        if (d["valor"] == None):
            # Estado: Dato que no está disponible ND
            d["bLimpieza"] = "ND"
        elif (d["valor"] >= rangos["limites"][d["idParametro"]]["min"]) and (d["valor"] <= rangos["limites"][d["idParametro"]]["max"]) and (d["valor"] >= 0):
            # Estado: Valido VA
            d["bLimpieza"] = "VA"
        elif (d["valor"] >= rangos["limites"][d["idParametro"]]["min"]) and (d["valor"] <= rangos["limites"][d["idParametro"]]["max"]) and (d["valor"] < 0):
            # Estado: Dato válido igualado al límite de detección o a cero VZ
            d["bLimpieza"] = "VZ"
        elif (d["valor"] < rangos["limites"][d["idParametro"]]["min"]) or (d["valor"] > rangos["limites"][d["idParametro"]]["max"]):
            # Estado: Dato inválido por rango de operación IR
            d["bLimpieza"] = "IR"