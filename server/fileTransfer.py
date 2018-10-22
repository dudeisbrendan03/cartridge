import sys
import socket

argamnt=len(sys.argv)
arglist=sys.argv
del arglist[0]
try:
    fileTransferHost = arglist[0]
    fileTransferPort = arglist[1]
    maxcon = arglist[3]
    maxcon = int(maxcon)
    fileTransferPort = int(fileTransferPort)
except IndexError: print("Did not give port, host and max connections. Should be used: fileTransfer.py abc.tld 1234 1 | fileTransfer.py HOST PORT MAXIMUM_CONNECTIONS")


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((fileTransferHost, fileTransferPort))
s.listen(maxcon)

print("Listening ...")

while True:
    conn, addr = s.accept()
    print("[+] Client connected: ", addr)

    # get file name to download
    f = open("payload", "wb")
    while True:
        # get file bytes
        data = conn.recv(4096)
        if not data:
            break
        # write bytes on file
        f.write(data)
    f.close()
    print("[+] Download complete!")

    # close connection
    conn.close()
    print("[-] Client disconnected")