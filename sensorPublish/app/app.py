import paho.mqtt.client as mqtt
import json
import time
import datetime
# importacion de las librerias necesarias

           # prueba local
mqtthost = '127.0.0.1' ## ip del broker mqtt
mqttport = 1883 # puerto del broker (default)

# test function para publicar datos en el topico "wsnJson"
# en este espacio estará la funcion que reciba los datos de la app movil y publicara en el topico wsnJson
def testFunction():
    for x in range(5):
        wsnData = '{"idSensor":"1525","mediciones":{"idParametro":55,"valor":"36"},"dateTime":"10/07/2019"}' #jsonPrueba
        client.publish("wsnJson", wsnData) # wsnJson es el nombre del topico donde wsnDatos será publicada


# estado del cliente
def on_log(client, userdata, level, buf):
    print("log: ", buf)

# se crea y define un cliente del broker mqtt, usando la libreria mqtt
client = mqtt.Client()
client.on_log = on_log
client.connect(mqtthost, mqttport) 
testFunction()
client.loop_forever()