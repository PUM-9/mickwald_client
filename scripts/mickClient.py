import rospy
from chat_server.msg import Message
import sys


def select_mode():
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
    name = 'mickwald'
    message = 0
    while message != '/exit':
        message = raw_input('Message: ')
        if message == '/name':
            message.split(' ')
            name = message[1]
        else
            pub.publish(name,message)
    return

def read_client():
    return

if __name__ == "__main__":
    try:
        select_mode()
    except rospy.ROSInterruptException:
        pass
