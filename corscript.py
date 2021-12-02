import sys  # Used for arguments
import corutil  # Used for utilities
commands = ["print", "var", "printv", "setvar", "getin"]  # Command list
vars = {} # Variable list
args = []

try:
    filein = sys.argv[1]  # Find filename
except IndexError:
    print("Corscript version 1.0.0 Shell")
    while True:
        args = input("corscript>").split(" ") # get shell input
        command = args.pop(0) # find command
        corutil.check_and_run_command(commands, command, args, vars) # check and run command

try:
    file = open(filein, "r")
except FileNotFoundError:
    print(f"The file {filein} does not exist. Did you type it correctly?")

for line in file.read().splitlines():
    if line:
        command, args = line.split(" ")
        corutil.check_and_run_command(commands, command, args, vars)
