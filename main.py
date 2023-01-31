# You can use this code in your project if you want, but please mentio me as creator if you release it to public beacuse it uses 4 clause BSD license.
# Thank you for reading. ;)

import subprocess, getpass, os, platform

username = getpass.getuser()

def display_tree(path, level):
    for i in os.listdir(path):
        print("  " * level + "├───" + i)
        current_path = os.path.join(path, i)
        if os.path.isdir(current_path):
            display_tree(current_path, level + 1)

def clear_terminal():
    if platform.system() == "Windows":
        subprocess.call("cls", shell=True)
    else:
        subprocess.call("clear", shell=True)

def main():
    clear_terminal()
    while True:
        command = input("["+username+"@"+platform.system()+"]$ ").split(" && ")
        for cmd in command:
            cmd = cmd.strip().split()
            if not cmd:
                continue
            elif cmd[0] == "ls":
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
            elif cmd[0] == "pwd":
                print(os.getcwd())
            elif cmd[0] == "whoami":
                print(username)
            elif cmd[0] == "mkdir":
                if len(cmd) == 1:
                    print("mkdir: missing operand")
                else:
                    os.mkdir(cmd[1])
            elif cmd[0] == "touch":
                if len(cmd) == 1:
                    print("touch: missing operand")
                else:
                    open(cmd[1], 'a').close()
            elif cmd[0] == "color":
                if len(cmd) == 1:
                    print("color: missing operand")
                else:
                    if platform.system() == "Windows":
                        os.system("color {0}".format(cmd[1]))
                    else:
                        print("{}: command not found".format(cmd[0]))
            elif cmd[0] == "help":
                print("List of commands:")
                print("ls - list files in current directory")
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
            elif cmd[0] == "tree":
                print("." + os.sep)
                display_tree(os.getcwd(), 1)
            elif cmd[0] == "clear":
                clear_terminal()
            elif cmd[0] == "exit":
                return
            else:
                print("{}: command not found".format(cmd[0]))

if __name__ == "__main__":
    main()
