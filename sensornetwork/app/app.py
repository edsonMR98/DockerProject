import paho.mqtt.client as mqtt
import json
import time
import datetime
import csv
# Se importan las librerias necesarias

# Visualiza los registros que se realizan
def on_log(client, userdata, level, buf):
    print("log: ",buf)

# Establece conexion al broker MQTT
# Subscripcion en el topico especificado (sensores2)
def on_connect(client, userdata, flags, rc):
    #connected
    print("Conectado")
    client.subscribe(topic='sensores2', qos=2)
    
# Se define y crea un cliente del broker MQTT, usando la libreria mqtt
client = mqtt.Client()
client.on_connect = on_connect
client.on_log = on_log
client.connect('mqttserver', 1883)

# Usa el archivo dataset (./dataset.csv) como csvFile
# se lee el archivo csv y se reestructura para ser publicado en el broker mqtt
with open('dataset.csv') as csvFile:
    csvReader = csv.DictReader(csvFile) # Lee el archivo CSV y lo convierte en un Dict de python
    tempHour = ''
    # Se recorre el dict previamente creado
    for csvRow in csvReader:
        data = {} # Se crea un Dict vacio
        data['dateTime'] = csvRow['datetime']   # Se crea la columna dateTime y se le agrega el valor que esta en el archivo CSV
        data['idStation'] = csvRow['clave_estacion']    # Se crea la columna isStations y se le agrega el valor que esta en el archivo CSV
        data['mediciones'] = [] # Se crea la columna mediciones vacia
        parameters = ['RH','TMP','WDR','WSP','CO','NO','NO2','NOX','O3','PM10','PM2.5','PMCO','SO2'] # Se crea un list con los contaminantes
        # Se recorre la list previamente creada y se agrega el contaminante con su valor al dict medicion
        # para posteriormente irse agregando a la columna mediciones del dict data
        for param in parameters:
            medicion = {
                "idParametro": param,
                "valor": csvRow[param]
            }
            data['mediciones'].append(medicion)
        data = json.dumps(data) # El dict se convierte a un objeto JSON
        print(data)
        if (tempHour != csvRow['hora']):
            time.sleep(5)
            print('CHANGE HOUR')
        client.publish('sensores2', data) # El objeto JSON es publicado al topico sensores2
        tempHour = csvRow['hora']