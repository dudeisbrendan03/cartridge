class incorrectUsage(Exception):
        """Incorrect usage of function. Check documentation"""

class consoleDisplay(object):
    """
    consoleDisplay - A tool used for controling the output on the console

    log - send an output with a notice before it and log it to a file
        'mode': error, warning, info, notice, none

    clear - identify operating system and clear the console accordingly
    """
    
    def log(self, mode="None",out=""):
        if out == "":#User used the function incorrectly
            raise incorrectUsage#User did an oof
        if out != "":
            import sys
            temp = sys.stdout                 # store original stdout object for later
            sys.stdout = open('log.txt', 'w') # redirect all prints to this log file
            print("{}: {}".format(type,out))   # nothing appears. it's written to log file instead
            sys.stdout.close()                # ordinary file object
            sys.stdout = temp                 # restore print commands to interactive prompt
            print("{}: {}".format(type,out))           # this shows up in the interactive prompt

    @staticmethod
    def clear():
        import os; s=os.name()#grab OS name, store it in 's'
        if s == 'posix':#check if we're on posix/unix
            c='clear'#set clear command
        elif s == 'nt':#check if we're on an NT based system
            c='cls'#set clear command
        os.system(c)#run clear command

