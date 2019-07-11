import pymongo
import ast
import sys
import json
import paho.mqtt.client as mqtt

# Usar un archivo .json como argumento
#with open(sys.argv[1]) as f:
 #   data = json.load(f)

# Visualiza los registros que se realizan
def on_log(client, userdata, level, buf):
    print("log: ",buf)

# Establece conexion al broker MQTT, Subscribirse en el topico especificado
def on_connect(client, userdata, flags, rc):
    #connected
    client.subscribe(topic='jsonValidado', qos=2)

# Recibe publicaciones del topico subscrito, Inserta en bd
# Convierte el payload a dict
def on_message(client, userdata, message):
    collection.insert_one(ast.literal_eval(message.payload))

# Define un cliente Mongo
mongoClient = pymongo.MongoClient('mongodb://mongoserver:27017/')
db = mongoClient.project
collection = db.measurements
#collection.insert_one(data)

# Define un cliente MQTT
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
#client.on_log = on_log
client.connect('mqttserver', 1883)
client.loop_forever()