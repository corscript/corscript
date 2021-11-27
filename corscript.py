import sys # Used for arguments
import corutil # Used for utilities
commands = ["print", "var"] # Command list

try:
    filein = sys.argv[1] # Find filename
except IndexError:
    print("Usage: corscript file.cor") # No arguments
    exit(1)
try:
    file = open(filein, "r")
except FileNotFoundError:
    print(f"The file {filein} does not exist. Did you type it correctly?")

for line in file.read().splitlines():
    if line:
        command, arg = line.split()
        if command in commands:
            corutil.RunCommand(command, arg) # run specified command
        else:
            print(f"Error: command {command} does not exist. Did you type it correctly?")