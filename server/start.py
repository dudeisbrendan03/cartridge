#This script will start Cartridge server normally (with any parameters)

#Import modules that are required most of the time/at all times
import sys#needed for arguments
from os import name as opname#needed to identify os
from consoleTools import consoleDisplay#needed for logging
import subprocess#needed for execution

argamnt=len(sys.argv)
arglist=sys.argv
del arglist[0]
try:
    if arglist[0] == "--force":
        cont=True
except IndexError: cont=False
print(str(sys.argv))

if opname == 'posix':
    print("Not supported on linux machines yet.\nTo launch anyway, run with the parameter --force")
    if cont == False:
        try:
            consoleDisplay.log('e','Killed before launch, running posix. Force launch using --force parameter')
        except ImportError:
            print("Missing dependencies.")
        exit()

from datetime import datetime
consoleDisplay.log('i','Server start attempt at {}'.format(datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
consoleDisplay.log('i','Going to launch server using default posix shell or command prompt (windows).')
subprocess.call("python server.py", shell=True)
