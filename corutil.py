def RunCommand(command, arg):
    '''
    Runs the specified corscript command with argument arg
    '''
    if command == "print":
        print(arg)
def check_and_run_command(commands, command, arg):
    if command in commands:
        RunCommand(command, arg)  # run specified command
    else:
        print(
            f"Error: command {command} does not exist. Did you type it correctly?")            
