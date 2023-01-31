# You can use this code in your project if you want for some reason, but please mention me as creator if you release it to public beacuse it uses 4 clause BSD license.
# Thank you for reading. ;)

import subprocess, os
from getpass import getuser
from platform import system

username = getuser() #Username that is used on local machine

#Tree command function
def display_tree(path, level):
    try:
        for i in os.listdir(path):
            print("  " * level + "├───" + i)
            current_path = os.path.join(path, i)
            if os.path.isdir(current_path):
                display_tree(current_path, level + 1)
    except PermissionError:
        print("[Access Denied]")
#clear command function
def clear_terminal():
    subprocess.call("cls", shell=True)
def main():
    #Clear local terminal on startup
    clear_terminal()
    print("Copyright (c) 2023 Bartłomiej Poleś. All rights reserved.\n")
    #App's main loop
    while True:
        command = input("["+username+"@"+system()+"]$ ").split(" && ")
        for cmd in command:
            cmd = cmd.strip().split()
            if not cmd:
                continue
            elif cmd[0] == "lf":
                files = os.listdir(os.getcwd())
                for file in files:
                    print(file)
            elif cmd[0] == "cd":
                if len(cmd) == 1:
                    print("cd: missing operand")
                else:
                    try:
                        os.chdir(cmd[1])
                    except FileNotFoundError:
                        print("cd: {}: No such file or directory".format(cmd[1]))
            #pwd command showing currently opened directory
            elif cmd[0] == "pwd":
                print(os.getcwd())
            #whoami command displaying username
            elif cmd[0] == "whoami":
                print(username)
            #mkdir command creating folders
            elif cmd[0] == "mkdir":
                if len(cmd) == 1:
                    print("mkdir: missing operand")
                else:
                    os.mkdir(cmd[1])
            #touch command creating files
            elif cmd[0] == "touch":
                if len(cmd) == 1:
                    print("touch: missing operand")
                else:
                    open(cmd[1], 'a').close()
            #color command for changing terminal's colors
            elif cmd[0] == "color":
                if len(cmd) == 1:
                    print("color: missing operand")
                else:
                    os.system("color {0}".format(cmd[1]))
            #help command for showing all available commands
            elif cmd[0] == "help":
                print("List of commands:")
                print("lf - list files in current directory")
                print("cd [directory] - change directory")
                print("pwd - print current directory")
                print("mkdir [directory] - create directory")
                print("touch [file] - create file")
                print("tree - show directory tree structure")
                print("clear - clear terminal")
                print("help - show this message")
                print("exit - close the app")
                print("color - changes colors of terminal")
                print("whoami - display your username")
            #tree command displaying structure of currently opened directory
            elif cmd[0] == "tree":
                print("." + os.sep)
                display_tree(os.getcwd(), 1)
            #clear command clearing simulated terminal
            elif cmd[0] == "clear":
                clear_terminal()
            #exit command that closes app
            elif cmd[0] == "exit":
                return
            #else that executes if non-existent command is typed in
            else:
                print("{}: command not found".format(cmd[0]))

if __name__ == "__main__":
    main()
