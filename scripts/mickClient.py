#!/usr/bin/env python
import rospy
from chat_server.msg import Message
import sys



def select_mode():
    read_client()
    return

def unused():
    mode = sys.argv[sys.argv.__len__()-1]
    if mode == 'read':
        read_client()
    if mode == 'send':
        send_client()
    if mode != 'read':
        if mode != 'send':
            print("Usage: use \"read\" or  \"send\" as arguments for respective mode")
    return


def send_client():
    pub = rospy.Publisher('chat_out', Message, queue_size=10)
    rospy.init_node('mick_sender', anonymous=True)
    name = raw_input('Choose name: ')
    message = 0
    shutdown = False
    while not shutdown:
        message = raw_input(name + ': ')
        if message[0:5] == '/name':
            message = message[0:]
            message = message.split(' ')
            name = message[1]
        elif message[0:5] == '/exit':
            shutdown = not shutdown
        else:
            pub.publish(name, message)
    return

def callback(message):
    print(message.sender + " says: " + message.message)

def read_client():
    rospy.init_node('mickChatListener', anonymous=True)
    rospy.Subscriber('chat_in', Message, callback)
    print("Now accepting messages\n")
    rate = rospy.Rate(10)
    rospy.spin()
    return

if __name__ == "__main__":
    try:
        select_mode()
    except rospy.ROSInterruptException:
        pass
