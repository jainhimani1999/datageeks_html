#!/usr/bin/python3
import cgi
import cgitb
import socket
import random
import webbrowser
cgitb.enable()
import subprocess
print("Content-type: text/html")
print("")
sock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
for i in range(10):
    value=random.randint(5000,65000)
    result = sock.connect_ex(('127.0.0.1',value))
    if(result == 0):
        break
    else:
        continue
sock.close()
#print('the port allocated is'+str(value))
#print('<h1>Humara Paraytan Katai Jahar</h1>')
continer=subprocess.getoutput('sudo docker run -itd -p '+str(value)+':80 my-apache2')

