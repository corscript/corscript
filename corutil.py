import subprocess
def check_and_run_command(commands, command, args, vars, fileargs):
    '''
    Checks command and runs it
    '''
    if command in commands:
        RunCommand(command, args, vars, commands, fileargs)  # run specified command
    else:
        print(
            f"Error: command {command} does not exist. Did you type it correctly?")     
def open_file(commands, vars, filein, fileargs):
    '''
    Opens a file and runs it
    '''
    try:
        global file
        file = open(filein, "r")
    except FileNotFoundError:
        print(f"The file {filein} does not exist. Did you type it correctly?")

    for line in file.read().splitlines():
        if line:
            args = line.split(" ")
            command = args.pop(0)
            check_and_run_command(commands, command, args, vars, fileargs)
    file.close()       
def RunCommand(command, args, vars, commands, fileargs):
    '''
    Runs the specified corscript command with argument arg
    '''
    if command == "print":
        for arg in args:
            print(arg, end=' ')
        print()
    elif command == "var":
        vars[args[0]]= "" # Create variable arg1
    elif command == "printv":
        print(vars[args[0]]) # Print variable arg1
    elif command == "setvar":
        vars[args[0]]= args[1] # Set variable arg1 to arg2
    elif command == "getin":
        vars[args[0]]= input(args[1]) # get input from user
    elif command == "load":
        newargs = args.pop(0)
        open_file(commands, vars, "~/.corscript/lib" + args[0] + ".cor", newargs) # Load module
    elif command == "*":
        print(subprocess.run(['python', '-c', args[0]], stdout=subprocess.PIPE).stdout.decode('utf-8')) # run python command
    elif command == "ifequals":
        if vars[args[0]] == vars[args[1]]:
            newargs = args.copy()
            newargs.pop(0)
            newargs.pop(1)
            check_and_run_command(commands, args[2], newargs, vars)
    elif command == "getarg":
        vars[args[1]]= fileargs[0]
        