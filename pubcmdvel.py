#!/usr/bin/env python
import rospy
import json
import paho.mqtt.client as paho
from geometry_msgs.msg import Twist
import math


rospy.init_node('robot_cleaner', anonymous=True)
velocity_publisher = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
vel_msg = Twist()

def on_subscribe(client, userdata, mid, granted_qos):
    print("Subscribed to Broker : ")

def on_message(client, userdata, msg):

    my_msg=(msg.payload)
    my_msg=json.loads(my_msg)
    z = (my_msg['x'])
    x = (my_msg['y'])
    print (my_msg)
    #Publish the velocity
    vel_msg.linear.x = x
    vel_msg.angular.z = -z
    velocity_publisher.publish(vel_msg)
client = paho.Client("Joy")
client.connect("test.mosquitto.org", 1883)
client.subscribe("covea/joystick", qos=0)
client.on_subscribe = on_subscribe
client.on_message = on_message
client.loop_forever()
