import socket
from consoleTools import consoleDisplay as cd

toExec = []
executionListNo = 0

if __name__ == '__main__':
    host = ""
    port = 5000
    
    if host == "0.0.0.0":
        cd.log('w','INSECURE: Serving an ALL addresses')
    catridge = socket.socket()
    catridge.bind((host,port))
     
    catridge.listen(1)
    conn, addr = catridge.accept()
    cd.log('n',"Connection from: " + str(addr))
    while True:
            data = conn.recv(1024).decode()
            if not data:
                    break
            cd.log('i',"Command recieved: " + str(data))
            if str(data) == "exec":
                print("A")
            else:
                toExec[executionListNo] = str(data)
                executionListNo+=1
            #data = str(data).upper()
            #print ("sending: " + str(data))
            #conn.send(data.encode())
             
    conn.close()