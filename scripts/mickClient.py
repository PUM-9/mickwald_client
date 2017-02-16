#!/usr/bin/env python
import rospy
from chat_server.msg import Message
import sys



def select_mode():
    mode = sys.argv[sys.argv.__len__()-1]
    if mode == 'read':
        read_client()
    if mode == 'send':
        run_client()
    if mode != 'read':
        if mode != 'send':
            print("Usage: use \"read\" or  \"send\" as arguments for respective mode")
    return


def run_client():
    pub = rospy.Publisher('chat_out', Message, queue_size=10)
    rospy.init_node('mick_client', anonymous=True)
    rospy.Subscriber('chat_in', Message, callback)
    name = raw_input('Choose name: ')
    message = 0
    shutdown = False
    while not shutdown:
        message = raw_input(name + ': ')
        if message[0:5] == '/name':
            name = message[6:]
        elif message[0:5] == '/exit':
            shutdown = not shutdown
        else:
            pub.publish(name, message)
    return

def callback(message):
    if message.sender == "":
        print(\n + "Noname" + " says: " + message.message + "\n" + name)
    else:
        print(\n + message.sender + " says: " + message.message + "\n" + name)

def read_client():
    rospy.init_node('mickChatListener', anonymous=True)
    rospy.Subscriber('chat_in', Message, callback)
    print("Now accepting messages\n")
    rate = rospy.Rate(10)
    rospy.spin()
    return

if __name__ == "__main__":
    try:
        run_client()
    except rospy.ROSInterruptException:
        pass
