import rospy
from chat_server.msg import Message

message = raw_input('Enter message: ')
print("Your message is \"" + message + "\"")

def run_client():
