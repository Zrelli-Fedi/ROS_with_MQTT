import paho.mqtt.client as paho
import time

def on_publish(client, userdata, mid):
    print("mid: "+str(mid))
 
client = paho.Client()
client.on_publish = on_publish
client.connect("test.mosquitto.org", 1883)
client.loop_start
while True :
    client.publish("covea/battery-level","100", qos=1) 
    time.sleep(5)
    client.publish("covea/battery-level","75", qos=1) 
    time.sleep(5)
    client.publish("covea/battery-level","50", qos=1) 
    time.sleep(5)
    client.publish("covea/battery-level","24", qos=1) 
    time.sleep(5)
    client.publish("covea/battery-level","17", qos=1) 
    time.sleep(5)
    client.publish("covea/battery-level","9", qos=1) 
    time.sleep(5)