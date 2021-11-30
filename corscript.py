import sys  # Used for arguments
import corutil  # Used for utilities
commands = ["print"]  # Command list
vars = {} # Variable list


try:
    filein = sys.argv[1]  # Find filename
except IndexError:
    print("Corscript version 0.0.1 Shell")
    while True:
        command, arg = input("corscript>").split(" ")
        corutil.check_and_run_command(commands, command, arg, vars)
    exit()
try:
    file = open(filein, "r")
except FileNotFoundError:
    print(f"The file {filein} does not exist. Did you type it correctly?")

for line in file.read().splitlines():
    if line:
        command, arg = line.split(" ")
        corutil.check_and_run_command(commands, command, arg)
