#This script will start Cartridge server normally (with any parameters)

#Import modules that are required most of the time/at all times
from sys import argv
from os import name as opname
from consoleTools import consoleDisplay
import subprocess

if opname() == 'posix':
    print("Not supported on linux machines yet.\nTo launch anyway, run with the parameter --force")
    consoleDisplay.log('e','Killed before launch, running posix. Force launch using --force parameter')
    exit()
if subprocess.call("(dir 2>&1 *`|echo CMD);&<# rem #>echo PowerShell", shell=True) == 'PowerShell':#Returns CMD if in command prompt, returns PowerShell if in ps
    print("Not supported on powershell.\nTo launch anyway, run with the parameter --force")
    consoleDisplay.log ('e','Killed before launch, running PowerShell. Force launch using --force parameter')
    exit()