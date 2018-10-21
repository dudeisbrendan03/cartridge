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
        host = "11.0.0.1"
        port = 5000
        
        if host == "0.0.0.0":
            print("\nCan not continue. Invalid hostname/IP.")
            exit()

        ctcs = socket.socket()
        ctcs.connect((host,port))
         
        message = input("#{}:{}$> ".format(host,port))
        if message == "":
                print("Invalid data entered, closing the client to protect the server.")
                exit()
        while message != 'q':
                ctcs.send(message.encode())
                data = ctcs.recv(1024).decode()
                
                
                if str(data) == "1":
                    print("The server is going down for a gracious exit, closing the cilent.")
                    input("Press ENTER to close")
                    print("\nKnown from the data recieved: "+str(data))
                    exit()
                elif str(data) == "2:":
                    print("Command successfully added")
                    print("\nKnown from the data recieved: "+str(data))
                elif str(data) == "4:":
                    print("Executing command list")
                    print("\nKnown from the data recieved: "+str(data))
                elif str(data) == "5":
                    print("Cleared all the commands in list")
                    print("\nKnown from the data recieved: "+str(data))
                else:
                    print("Recieved data: "+str(data))

                message = input("\n#{}:{}$> ".format(host,port))
                if message == "":
                    print("Invalid data entered, closing the client to protect the server.")
                    exit()
        ctcs.close()

if __name__ == '__main__':
    try:
        ctc()
    except ConnectionResetError:
        print("\nThe server has gone down without specifying a reason")