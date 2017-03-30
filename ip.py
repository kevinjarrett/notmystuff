from sense_hat import SenseHat

import socket
import fcntl
import struct

def get_ip_address(ifname):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    return socket.inet_ntoa(fcntl.ioctl(
        s.fileno(),
        0x8915,  # SIOCGIFADDR
        struct.pack('256s', ifname[:15])
    )[20:24])

sense = SenseHat()
sense.clear()
sense.set_rotation(270)

for i in range(3):
    ip = get_ip_address('wlan0')
    sense.show_message(ip, scroll_speed=.06, text_colour=[255,255,255], back_colour=[0,0,0])
    
