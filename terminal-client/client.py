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
        host = "127.0.0.1"
        port = 5000
        
        if host == "0.0.0.0":
            print("\nCan not continue. Invalid hostname/IP.")
            exit()

        ctcs = socket.socket()
        ctcs.connect((host,port))
         
        message = input("#{}:{}$> ".format(host,port))
         
        while message != 'q':
                ctcs.send(message.encode())
                data = ctcs.recv(1024).decode()
                
                print("Recieved data: "+str(data))
                if str(data) == "1":
                    print("The server is going down for a gracious exit, closing the cilent.")
                    input("Press ENTER to close")
                    exit()
                
                message = input("#{}:{}$> ".format(host,port))
                 
        ctcs.close()

if __name__ == '__main__':
    try:
        ctc()
    except ConnectionResetError:
        print("\nThe server has gone down without specifying a reason")