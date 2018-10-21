class incorrectUsage(Exception):
        """Incorrect usage of function. Check documentation"""

class scriptFailureIOOP(Exception):
    """Script failure due to a problem creating or editing a directory or file"""

class generalError(Exception):
    """Error that has occured with no reason specified"""

#class bcolors: REDUNDANT - DOESNT WORK ON WINDOWS BY DEFAULT
#    HEADER = '\033[95m'
#    OKBLUE = '\033[94m'
#    OKGREEN = '\033[92m'
#    WARNING = '\033[93m'
#    FAIL = '\033[91m'
#    ENDC = '\033[0m'
#    BOLD = '\033[1m'
#    UNDERLINE = '\033[4m'

class consoleDisplay(object):
    from datetime import datetime as datenow #Date now command
    global fname#file named used for logging - set in __init__
    """
    consoleDisplay - A tool used for controling the output on the console

    log - send an output with a notice before it and log it to a file
        'mode': error, warning, info, notice, none

    clear - identify operating system and clear the console accordingly
    """
    def __init__(self):
        from datetime import datetime #Date now command
        date=str(datetime.now)
        #create files before use
        from os import path as p
        if p('logs/') == False:
            try:
                import os;os.mkdir('logs')
            except OSError:
                raise scriptFailureIOOP
        if p('logs/{}-log.txt'.format(date)) == False:
            f=open('logs/{}-log.txt'.format(date),'w+')
            f.close()
        fname="{}-log.txt".format(date)
        self.fname = fname

    from datetime import datetime
    fnameSet=datetime.now().strftime('%Y-%m-%d')

    @staticmethod
    def log(mode="None",out="",file=fnameSet+"-log.txt"):
        from termcolor import colored as col
        type=""
        if out == "":#User used the function incorrectly
            raise incorrectUsage#User did an oof
        if mode == "None":
            raise incorrectUsage
        elif mode == 'e':
            type = "ERROR"
            if out != "":   print(col(type,"red")+": {}".format(out)) # this shows up in the interactive prompt
        elif mode == 'w':
            type = "WARNING"
            if out != "":   print(col(type,"orange")+": {}".format(out)) # this shows up in the interactive prompt
        elif mode == 'n':
            type = "Notice"
            if out != "":   print("{}: {}".format(type,out)) # this shows up in the interactive prompt
        elif mode == 'i':
            type = "Info"
            if out != "":   print(col(type,"blue")+": {}".format(out)) # this shows up in the interactive prompt
        elif mode == 's':
            type = "Success"
            if out != "":   print(col(type,"green")+": {}".format(out)) # this shows up in the interactive prompt
        import sys
        temp = sys.stdout # store original stdout object for later
        sys.stdout = open(file, 'w') #prints now go the the file
        print("{}: {}".format(type,out))   # nothing appears. it's written to log file instead
        sys.stdout.close() # ordinary file object
        sys.stdout = temp  # restore print commands to interactive prompt

    @staticmethod
    def clear():
        import os; s=os.name()#grab OS name, store it in 's'
        if s == 'posix':#check if we're on posix/unix
            c='clear'#set clear command
        elif s == 'nt':#check if we're on an NT based system
            c='cls'#set clear command
        os.system(c)#run clear command
