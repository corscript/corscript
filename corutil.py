def RunCommand(command, args, vars):
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
def check_and_run_command(commands, command, args, vars):
    '''
    Checks command and runs it
    '''
    if command in commands:
        RunCommand(command, args, vars)  # run specified command
    else:
        print(
            f"Error: command {command} does not exist. Did you type it correctly?")            
