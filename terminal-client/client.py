import socket

print("""

C A R T R I D G E
_________________
Terminal client
v0.1 | NOT stable
_________________
https://github.com/dudeisbrendan03/cartridge - Dev | Maintainer
https://github.com/superigi - Dev
_________________

""")
def ctc():
        host = ""
        port = 5000
        
        if host == "0.0.0.0":
            print("\nCan not continue. Invalid hostname/IP.")
            exit()

        ctcs = socket.socket()
        ctcs.connect((host,port))
         
        message = input(" -> ")
         
        while message != 'q':
                ctcs.send(message.encode())
                data = ctcs.recv(1024).decode()
                 
                print ('Received from server: ' + data)
                 
                message = input("#{}:{}$> ".format(host,port))
                 
        ctcs.close()

if __name__ == '__main__':
    ctc()