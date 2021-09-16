#! /usr/bin/env python
import rospy
import paho.mqtt.client as paho
from std_msgs.msg import String


rospy.init_node('pubnode')

pub=rospy.Publisher('covea/joy',String,queue_size=10)
rate=rospy.Rate(0.000001)
my_msg = String()

def on_subscribe(client, userdata, mid, granted_qos):
    print("Subscribed to Broker : ")

def on_message(client, userdata, msg):
   my_msg.data= msg.payload 
   print( str(msg.payload))
   pub.publish(my_msg)



client = paho.Client("Joy")
client.connect("test.mosquitto.org", 1883)
client.subscribe("covea/joystick", qos=0)
client.on_subscribe = on_subscribe
client.on_message = on_message
client.loop_forever()
rate.sleep() 

 










