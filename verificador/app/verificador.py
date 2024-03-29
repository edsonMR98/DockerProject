import pymongo
import paho.mqtt.client as mqtt
import json
import sys
import ast
import criterios as c # Se importa el archivo criterios (./criterios.py) como c
import datetime
# Importar las librerias y scripts necesarios


# Usar un archivo .json (./rangos,json) como argumento
# Convierte un json en un objeto de Python
with open(sys.argv[1]) as f:
    rangos = json.load(f)

# Visualiza los registros y todo lo que se realiza
def on_log(client, userdata, level, buf):
    print("log: ",buf)

# Establece conexion al cliente del broker MQTT
# Subscribirse en el topico especificado (sensores2)
def on_connect(client, userdata, flags, rc):
    #connected
    print("Conectado")
    client.subscribe(topic='sensores2', qos=2)

# Recibe publicaciones del topico subscrito (sensores2)
# Verifica el mensaje recibido del broker mqtt con la funcion verificar (criterios.py)
# Se obtiene la fecha y hora y se reformatea para despues agregarlo a la coleccion
# Inserccion en base de datos (project) de mongo, a la coleccion measurements
def on_message(client, userdata, message):
    # varificar datos
    verificado = c.verificar(message.payload, rangos)

    #formato de datetime
    dateStr = verificado['dateTime']
    dateFormat = datetime.datetime.strptime(dateStr, "%Y-%m-%d %H:%M:%S")
    
    print(verificado)
    
    #collection.insert_one(ast.literal_eval(verificado))
    collection.insert({
        "idStation": verificado['idStation'],
        "dateTime": dateFormat,
        "mediciones": verificado['mediciones']
    })

# Define un cliente Mongo y se obtiene la base de datos y collecion, usando la libreria pymongo
mongoClient = pymongo.MongoClient('mongodb://mongodb:27017/')
db = mongoClient.project
collection = db.measurements

# Define un cliente MQTT, usando la libreria mqtt
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.on_log = on_log
client.connect('mqttserver', 1883)
client.loop_forever()