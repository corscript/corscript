import sys  # Used for arguments
import corutil  # Used for utilities
commands = ["print", "var", "printv", "setvar", "getin", "*", "ifequals", "getarg"]  # Command list
vars = {} # Variable list
args = []

try:
    filein = sys.argv[1]  # Find filename
except IndexError:
    print("Corscript version 1.2.2 Shell")
    while True:
        args = input("corscript>").split(" ") # get shell input
        command = args.pop(0) # find command
        corutil.check_and_run_command(commands, command, args, vars, []) # check and run command
newargs = sys.argv.copy()
newargs.pop(0)
newargs.pop(0)
corutil.open_file(commands, vars, filein, newargs)
