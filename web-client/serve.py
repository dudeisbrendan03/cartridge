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
from consoleTools import consoleDisplay
import http.server
import socketserver
import socket

#Any variables that need to be set beforehand
PORT = 8080

#Starting the server
consoleDisplay.log('i','Setup: Preparing to serve webserver on {}'.format(PORT),False)
Handler = http.server.SimpleHTTPRequestHandler
httpd = socketserver.TCPServer(("", PORT), Handler)

#Display hostname
try:
    host_name = socket.gethostname()
    host_ip = socket.gethostbyname(host_name)
    consoleDisplay.log('i',"\nHostname: {}\nIP: {}".format(host_name,host_ip),False)
except:
    consoleDisplay.log('e',"Couldn't get Hostname or IP")

try:
    httpd.serve_forever()
except KeyboardInterrupt:
    consoleDisplay.log('e',"KEYBOARD INTERRUPT. EXCEPT\n")
    pass

consoleDisplay.log('w',"Server is about to go down")
httpd.server_close()
consoleDisplay.log('i',"Server is no longer serving")
