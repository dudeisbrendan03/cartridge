import socket
try:
    from consoleTools import consoleDisplay as cd
except ModuleNotFoundError:
    print("\nYou don't have consoleTools. This is used to displaying items to the console as well as logging them")
global toExec
global executionListNo
toExec = []
executionListNo = 0
exitval = False

"""
CODE LIST
======
1 - Gracious exit
2 - Command added
3 - Terminated (loss of connection)
4 - Exec list
5 - Clear list

"""

if __name__ == '__main__':
    try:
        host = "11.0.0.1"
        port = 5000
        
        if host == "0.0.0.0":
            cd.log('w','INSECURE: Serving an ALL addresses')
        cd.log('i','Socket setup - 1 - Preparing socket')
        catridge = socket.socket()
        cd.log('i','Socket setup - 2 - Binding cartridge server to "{}:{}"'.format(str(host),str(port)))
        try:    catridge.bind((host,port))
        except OSError as e:
            cd.log('e','Could not start the server. Is the port in use?')
            print("\n\n=================\nInformation for nerds:\n"+str(e))
            exit()
        cd.log('s','Socket setup - 2 - Successfully bound the port')
        cd.log('i','Socket setup - 3 - Starting to listen on port')
        catridge.listen(1)
        cd.log('s','Socket setup - COMPLETE - Server is up and listening on "{}:{}"'.format(str(host),str(port)))
        conn, addr = catridge.accept()
        cd.log('n',"Connection from: " + str(addr))
        while True:
            try:
                data = conn.recv(1024).decode()
                if not data:
                        break
                cd.log('i',"Command recieved: " + str(data))
                if str(data) == "exec":
                    cd.log('w',"About to run the following commands: "+str(toExec))
                    print("A")
                elif str(data) == "term":
                    cd.log('e',"TERMINATE - NOW")
                    exit()
                elif str(data) == "gracious":
                    cd.log('w',"Server is beginning gracious exit")
                    data = "1"
                    cd.log('n',"Sending: '{}'  to  '{}' ".format(str(data),str(addr)))
                    conn.send(data.encode())
                    catridge.close()
                    toExec = []
                    executionListNo = 0
                    exit(1)
                elif str(data) == "list_commands":
                    data = str(toExec)
                    cd.log('n',"Sending: '{}'  to  '{}' ".format(str(data),str(addr)))
                    conn.send(data.encode())
                elif str(data) == "clear_commands":
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

