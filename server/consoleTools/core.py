class incorrectUsage(Exception):
        """Incorrect usage of function. Check documentation"""

class scriptFailureIOOP(Exception):
    """Script failure due to a problem creating or editing a directory or file"""

class generalError(Exception):
    """Error that has occured with no reason specified"""

class missingContent(Exception):
    """You are missing a dependancy required by the script"""

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
        date=str(datetime.now().strftime('%Y-%m-%d'))
        #create files before use
        import os.path as p
        if p.exists('logs/') == False:
            try:
                import os;os.mkdir('logs')
            except OSError:
                raise scriptFailureIOOP
        if p.exists('logs/{}-log.txt'.format(date)) == False:
            f=open('logs/{}-log.txt'.format(date),'w+')
            f.close()
        fname="{}-log.txt".format(date)
        
    from datetime import datetime
    fnameSet="logs/"+str(datetime.now().strftime('%Y-%m-%d'))+"-log.txt"

    @staticmethod
    def log(mode="None",out="",noLog=False,file=fnameSet):
        try:
            from termcolor import colored as col
            from termcolor import cprint as cp
            import colorama
        except ImportError:
            print("\nMissing dependancy\n")
            raise missingContent
        from datetime import datetime

        colorama.init()
        
        type=""
        if out == "":#User used the function incorrectly
            raise incorrectUsage#User did an oof
        if mode == "None":
            raise incorrectUsage
        elif mode == 'e':
            type = "ERROR"
            if out != "":  cp("{}".format(type),"white",'on_red',attrs=['bold'],end=""); print(": {}".format(out)) # this shows up in the interactive prompt
        elif mode == 'w':
            type = "Warning"
            if out != "":   cp("{}".format(type),"yellow",attrs=['bold'],end=""); print(": {}".format(out)) # this shows up in the interactive prompt
        elif mode == 'n':
            type = "Notice"
            if out != "":   print("{}: {}".format(type,out)) # this shows up in the interactive prompt
        elif mode == 'i':
            type = "Info"
            if out != "":   cp("{}".format(type),"blue",attrs=['bold'],end=""); print(": {}".format(out)) # this shows up in the interactive prompt
        elif mode == 's':
            type = "SUCCESS"
            if out != "":   print("{}: {}".format(col(type,"green",attrs=['bold']),out)) # this shows up in the interactive prompt
        if noLog == False:
            f = open(file, 'a') #prints now go the the file
            f.write("\n{} - {}: {}".format(str(datetime.now().strftime('%Y-%m-%d %H:%M:%S')),type,out))   # nothing appears. it's written to log file instead
            f.close

    @staticmethod
    def clear():
        import os; s=os.name()#grab OS name, store it in 's'
        if s == 'posix':#check if we're on posix/unix
            c='clear'#set clear command
        elif s == 'nt':#check if we're on an NT based system
            c='cls'#set clear command
        os.system(c)#run clear command

