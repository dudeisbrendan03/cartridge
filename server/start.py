#This script will start Cartridge server normally (with any parameters)

#Import modules that are required most of the time/at all times
from sys import argv
from os import name as opname
from consoleTools import consoleDisplay
if opname() == 'posix':
    print("Not supported on linux machines yet.\nTo launch anyway, run with the parameter --force")
    consoleDisplay.log('e','Killed before launch, running posix. Force launch using --force parameter')
    exit()