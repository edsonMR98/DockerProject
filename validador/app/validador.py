import paho.mqtt.client as mqtt
import json
import sys
import validaciones as v

# Usar un archivo .json (rangos) como argumento
with open(sys.argv[1]) as f:
    rangos = json.load(f)

# Visualiza los registros que se realizan
def on_log(client, userdata, level, buf):
    print("log: ",buf)

# Establece conexion al broker MQTT, Subscribirse en el topico especificado
def on_connect(client, userdata, flags, rc):
    #connected
    client.subscribe(topic='prueba', qos=2)

# Recibe publicaciones del topico subscrito
# Validar el mensaje recibido de mqtt
# Publica al topico del indexador
def on_message(client, userdata, message):
    print(message.payload)
    v.validar(message.payload, rangos)
    #client.publish("prueba2", "Hola")

# Define un cliente MQTT
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
#client.on_log = on_log
client.connect('127.0.0.1', 1883)
client.loop_forever()