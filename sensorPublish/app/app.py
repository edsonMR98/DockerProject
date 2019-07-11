import paho.mqtt.client as mqtt
import json
import time
import datetime

           #local test
mqtthost = '127.0.0.1' ##broker mqtt ip 
mqttport = 1883 #default mqtt port

#test function to publish data in the topic "wsnJson"
def reaDataWsn():
    for x in range(5):
        wsnData = '{"idSensor":"1525","mediciones":{"idParametro":55,"valor":"36"},"dateTime":"10/07/2019"}' #jsonPrueba
        client.publish("wsnJson", wsnData) #wsnJson is the name of the topic where wsnData will be publish


#client status
def on_log(client, userdata, level, buf):
    print("log: ", buf)

client = mqtt.Client()
client.on_log = on_log
client.connect(mqtthost, mqttport) 
reaDataWsn()
client.loop_forever()