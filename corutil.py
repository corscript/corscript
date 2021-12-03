def check_and_run_command(commands, command, args, vars):
    '''
    Checks command and runs it
    '''
    if command in commands:
        RunCommand(command, args, vars, commands)  # run specified command
    else:
        print(
            f"Error: command {command} does not exist. Did you type it correctly?")     
def open_file(commands, vars, filein):
    try:
        file = open(filein, "r")
    except FileNotFoundError:
        print(f"The file {filein} does not exist. Did you type it correctly?")

    for line in file.read().splitlines():
        if line:
            command, args = line.split(" ")
            check_and_run_command(commands, command, args, vars)
    file.close()       
def RunCommand(command, args, vars, commands):
    '''
    Runs the specified corscript command with argument arg
    '''
    if command == "print":
        print(args[0]) # Print arg1
    elif command == "var":
        vars[args[0]]= "" # Create variable arg1
    elif command == "printv":
        print(vars[args[0]]) # Print variable arg1
    elif command == "setvar":
        vars[args[0]]= args[1] # Set variable arg1 to arg2
    elif command == "getin":
        vars[args[0]]= input(args[1]) # get input from user
    elif command == "load":
        open_file(commands, vars, "~/.corscript/lib" + args[0] + ".cor")