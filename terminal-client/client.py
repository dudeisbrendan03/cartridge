import socket
from tkinter import filedialog
import os
from consoleTools import fileTools
import sys

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
        elif host == "":
            print("\nCan not continue. Set host in script.")

        ctcs = socket.socket()
        try:
            ctcs.connect((host,port))
        except OSError:
            print("\nThe server you are trying to connect to isn't probably running, or is busy at this time. Check if you got the address correct")
            input("\nPress ENTER to exit the script")
            exit()
         
        message = input("#{}:{}$> ".format(host,port))

        if message == "":
            print("Invalid data entered, closing the client to protect the server.")
            exit()
        elif message == "/payload load":
            print("Next time run another operation before beginning loading. Try doing `/commands list` then run `/payload load`. The script will now exit")
            ctcs.close()
            exit()
        while message != '/exit':
                if message == "/payload load":
                    a = input("#File Name$> ")
                    if a == "/easy":
                        localFile = filedialog.askopenfilename()
                    else:   localFile = a
                    fileTools.universemove('localFile',os.getcwd()+'payload')


                    hostf = "127.0.0.1"
                    portf = 5001

                    filetransfer = socket.socket(socket.AF_INET,   socket.SOCK_STREAM)
                    filetransfer.connect((hostf, portf))
                    print("[+] Connected with Server")

                    # get file name to send
                    f_send = 'payload'
                    # open file
                    with open(f_send, "rb") as f:
                        # send file
                        print("[+] Sending file...")
                        data = f.read()
                        filetransfer.sendall(data)

                        # close connection
                        filetransfer.close()
                        print("[-] Disconnected")
                        sys.exit(0)
                ctcs.send(message.encode())
                data = ctcs.recv(1024).decode()
                
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

                if message == "/payload load":
                    print()
                elif message == "":
                    print("Invalid data entered, closing the client to protect the server.")
                    ctcs.close()#so the server doesn't hang
                    exit()
        ctcs.close()

if __name__ == '__main__':
    try:
        ctc()
    except ConnectionResetError:
        print("\nThe server has gone down without specifying a reason")