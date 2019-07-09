import json

# m: payload, message from mqtt
# r: archivo rangos.json
def validar(m, r):
    data = toDict(m)    # data recibida de mqtt en tipo dict
    rangos = r          # rangos para validar la data

    for d in data["mediciones"]:
        print("Id: ", d["idParametro"])
        if (d["valor"] >= rangos["limites"][d["idParametro"]]["min"]) and (d["valor"] <= rangos["limites"][d["idParametro"]]["max"]):
            print("Estado: Correcto")
        else:
            print("Estado: Incorrecto")
        print("")
    
    
    

# Convertir un dato tipo bytes to dict
def toDict(fileBytes):
    fileStr = str(fileBytes.decode("utf-8"))
    return json.loads(fileStr)