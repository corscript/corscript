def RunCommand(command, arg, vars):
    '''
    Runs the specified corscript command with argument arg
    '''
    if command == "print":
        print(arg)
    elif command == "var":
        vars[arg]= ""
    elif command == "printv":
        print(vars[arg])
def check_and_run_command(commands, command, arg, vars):
    if command in commands:
        RunCommand(command, arg, vars)  # run specified command
    else:
        print(
            f"Error: command {command} does not exist. Did you type it correctly?")            
