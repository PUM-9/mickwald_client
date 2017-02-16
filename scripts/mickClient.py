import rospy
from chat_server.msg import Message
import sys


def select_mode():
    print(sys.argv)
    mode = sys.argv[sys.argv.__len__()-1]
    return

def send_client():
    pub = rospy.Publisher('chat_out', Message, queue_size=10)
    rospy.init_node('mick_sender', anonymous=True)
    name = 'mickwald'
    message = 0
    while message != '/exit':
        message = raw_input('Message: ')
        #pub.publish(name,message)
    return

def read_client():
    return

if __name__ == "__main__":
    try:
        select_mode()
    except rospy.ROSInterruptException:
        pass
