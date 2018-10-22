# FLOPPY - The cartridge web client
#=========================
# _________________
#|# :           : #|
#|  :           :  |
#|  :           :  |
#|  :           :  |
#|  :___________:  |
#|     _________   |
#|    | __      |  |
#|    ||  |     |  |
#\____||__|_____|__|
#
#Import any important modules
from consoleTools import consoleDisplay as cd
import http.server
import socketserver
import socket
import os
from requests import get
import threading
from threading import Thread

#Any variables that need to be set beforehand
PORT = 8080
PHPPORT = 8081
customIpEnabled = True
customIp = "127.0.0.1"
#Used to grab our external IP
def ip():
    ipc = get('https://api.ipify.org').text
    return ipc


#Create a file that contains our public IP to be sent to the server to get into PHP. We use this server to log requests and we'll add some other features later on
ipFile=open('ip.txt','w+')
if customIpEnabled != True:
    ipFile.write("http://"+str(ip())+":"+str(PHPPORT))
elif customIpEnabled == True:
    ipFile.write("http://"+str(customIp)+":"+str(PHPPORT))
ipFile.close()




def func1():
    #Starting the server
    cd.log('i','Setup: Preparing to serve webserver on {}'.format(PORT))
    Handler = http.server.SimpleHTTPRequestHandler
    httpd = socketserver.TCPServer(("", PORT), Handler)

    #Display hostname
    try:
        host_name = socket.gethostname()
        host_ip = socket.gethostbyname(host_name)
        cd.log('i',"\nHostname: {}\nIP: {}".format(host_name,host_ip),False)
    except:
        cd.log('e',"Couldn't get Hostname or IP")

    try:
        cd.log('i','Server is now running')
        httpd.serve_forever()
    except KeyboardInterrupt:
        cd.log('e',"KEYBOARD INTERRUPT. EXCEPT\n")
        pass

    cd.log('w',"Server is about to go down")
    httpd.server_close()
    cd.log('i',"Server is no longer serving")


def func2():
    cd.log('i',"Starting php server")
    try:
        os.system('php -S 0.0.0.0:{} -t php/'.format(PHPPORT))
    except KeyboardInterrupt:
        cd.log('e',"KEYBOARD INTERRUPT. EXCEPT\n")
        pass
    cd.log('n',"Ended PHP server on '0.0.0.0:{}'".format(str(PHPPORT)))

if __name__ == '__main__':
    Thread(target = func1).start()
    Thread(target = func2).start()

