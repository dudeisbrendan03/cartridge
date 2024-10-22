import socket
try:
    from consoleTools import consoleDisplay as cd
except ImportError:
    print("\nYou don't have consoleTools. This is used to displaying items to the console as well as logging them\nGet it by running: pip install console-tools")
    input()
    exit()
try:
    from time import sleep
except ImportError:
    print("\nYour python install is damaged")
    input()
    exit()
global toExec
global executionListNo
global safeexec

#Config (to be moved to a file)
defExec = []#Default exec - run these commands every time the /exec command is given
ver = "0.1.12"#Script version
safeexec = False#The value used to confirm execution - set to true to never warn about execution
maxcon = 1#Maximum amount of connections at a single time (haven't added support for logging which IP did what yet)
consolePort = 5000#The port that the console runs on (currently multi-tasks as file transfer and console/going to be changed)
consoleHost = "127.0.0.1"#The place to bind the server to
fileTransferPort = 50001#not in use
fileTransferHost = "127.0.0.1"#not in use
###CONFIG END

toExec = defExec
executionListNo = 0
exitval = False
host = consoleHost#To be removed
port = consolePort#To be removed

"""
CODE LIST
======
0 - Unknown error
1 - Gracious exit
2 - Command added
3 - Terminated (loss of connection)
4 - Exec list
5 - Exec list cleared
6 - Exec list arm

"""

if __name__ == '__main__':
    try:
        
        if fileTransferHost == "0.0.0.0":
            cd.log('w','INSECURE: [File transfer] Serving on ALL addresses')
        if consoleHost == "0.0.0.0":
            cd.log('w','INSECURE: Serving on ALL addresses')
        cd.log('i','Socket setup - 1 - Preparing socket')
        catridge = socket.socket()
        cd.log('i','Socket setup - 2 - Binding cartridge server to "{}:{}"'.format(str(consoleHost),str(consolePort)))
        try:    catridge.bind((consoleHost,consolePort))
        except OSError as e:
            cd.log('e','Could not start the server. Is the port in use?')
            print("\n\n=================\nInformation for nerds:\n"+str(e))
            exit()
        cd.log('s','Socket setup - 2 - Successfully bound the port')
        cd.log('i','Socket setup - 3 - Starting to listen on port')
        catridge.listen(maxcon)
        cd.log('s','Socket setup - COMPLETE - Server is up and listening on "{}:{}"'.format(str(consoleHost),str(consolePort)))
        sleep(1)
        cd.clear()
        cd.log('i',"Cartridge (base) is up and running")
        cd.printFile('atari.ascii')
        print("\n\nCartridge v{} (https://github.com/dudeisbrendan03/cartridge) running at {} on port {}".format(ver,consoleHost,consolePort))
        conn, addr = catridge.accept()
        cd.log('n',"Connection from: " + str(addr))
        while True:
            try:
                data = conn.recv(1024).decode()
                if not data:
                        break
                cd.log('i',"Command recieved: " + str(data))
                if str(data) == "/exec":
                    cd.log('w',"About to run the following commands: "+str(toExec))
                    if safeexec == False:
                        cd.log('w',"Attempt to run the commands failed - not armed.")
                        data = "6"
                        cd.log('n',"Sending: '{}'  to  '{}' ".format(str(data),str(addr)))
                        conn.send(data.encode())
                        safeexec = True
                    elif safeexec == True:
                        cd.log('w',"RUNNING THE EXECUTION LIST !!!WARNING!!! Exec list:"+str(toExec))
                        data = "4"
                        cd.log('n',"Sending: '{}'  to  '{}' ".format(str(data),str(addr)))
                        conn.send(data.encode())
                        for x in toExec:
                            from os import system as s
                            s(x)
                        safeexec = False
                elif str(data) == "/payload recieve":
                    import os
                    os.system('python fileRecieve.py {} {} {}'.format(fileTransferHost,fileTransferPort,maxcon))
                elif str(data) == "/payload upload":
                    print("")
                    #this will be used to send a payload to the other device
                elif str(data) == "/payload load":
                    cd.log('e',"A client command was recieved by the server for some reason")
                    data = "0"
                    cd.log('n',"Sending: '{}'  to  '{}' ".format(str(data),str(addr)))
                    conn.send(data.encode())
                elif str(data) == "/payload settings":
                    print("")
                    #this will be used to send how the payload will be executed
                elif str(data) == "/payload exec":
                    print()
                    #this will run whatever the payloads execution command is
                elif str(data) == "/term":
                    cd.log('e',"TERMINATE - NOW")
                    exit()
                elif str(data) == "/gracious":
                    cd.log('w',"Server is beginning gracious exit")
                    data = "1"
                    cd.log('n',"Sending: '{}'  to  '{}' ".format(str(data),str(addr)))
                    conn.send(data.encode())
                    catridge.close()
                    toExec = defExec
                    executionListNo = 0
                    exit(1)
                elif str(data) == "/commands list":
                    data = str(toExec)
                    cd.log('n',"Sending: '{}'  to  '{}' ".format(str(data),str(addr)))
                    conn.send(data.encode())
                elif str(data) == "/commands clear":
                    data = "5"
                    cd.log('n',"Sending: '{}'  to  '{}' ".format(str(data),str(addr)))
                    conn.send(data.encode())
                    cd.log('i',"Clearing command list")
                    toExec = []
                    cd.log('s',"Command list cleared")
                else:
                    toExec.append(str(data))
                    executionListNo+=1
                    data = "2"
                    cd.log('n',"Sending: '{}'  to  '{}' ".format(str(data),str(addr)))
                    conn.send(data.encode())
            except ConnectionResetError:
                cd.log('w','The remote client exited without a reason')
    
        conn.close()

    except KeyboardInterrupt:
        if exitval == False:
            exitval = True
            print("Press CTRL+C again for violent exit")
            pass
        else:
            cd.log('e',"VIOLENT EXIT")
            exit()

