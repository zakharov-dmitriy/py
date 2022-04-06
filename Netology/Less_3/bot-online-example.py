command = "/add 12.12.2021 Task's text"

splitted_command = command.split(maxsplit=2)
print(splitted_command)
date = splitted_command[1]
task = splitted_command[2]
