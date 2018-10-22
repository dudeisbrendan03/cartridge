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
        elif host == "":
            print("\nCan not continue. Set host in script.")

        ctcs = socket.socket()
        try:
            ctcs.connect((host,port))
        except OSError:
            print("\nThe server you are trying to connect to isn't probably running, or is busy at this time.")
            input("\nPress ENTER to exit the script")
            exit()
         
        message = input("#{}:{}$> ".format(host,port))

        if message == "":
                print("Invalid data entered, closing the client to protect the server.")
                exit()

        while message != 'q':
                ctcs.send(message.encode())
                data = ctcs.recv(1024).decode()
                
                print(str(type(data)))
                if str(data) == "1":
                    print("The server is going down for a gracious exit, closing the cilent.")
                    input("Press ENTER to close")
                    print("\nKnown from the data recieved: "+str(data))
                    exit()
                elif str(data) == "2":
                    print("Command successfully added")
                    print("\nKnown from the data recieved: "+str(data))
                elif str(data) == "4":
                    print("Executing command list")
                    print("\nKnown from the data recieved: "+str(data))
                elif str(data) == "5":
                    print("Cleared all the commands in list")
                    print("\nKnown from the data recieved: "+str(data))
                elif str(data) == "6":
                    print("\nThe command failed to execute\nThe server was not armed. BUT IT NOW IS.\n\n!!!WARNING!!!\nMake sure you know what you are doing before executing your command list.\nRun /exec again to execute the command list")
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