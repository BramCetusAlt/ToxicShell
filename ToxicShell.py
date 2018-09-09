import subprocess, os, re


run = True

while run == True:
    try:
        print("Type 'exit' to exit the shell")
        command = str(input("ToxicShell:>"))
        if re.search("exit", command, re.IGNORECASE):
            run = False
        elif command[:2] == "cd":
            os.chdir(command[3:])
        else:
            process = subprocess.Popen(command[:], stdout = subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE, shell=True)
            output = process.stdout.read() + process.stderr.read()
            output_string = str(output)
            print(output_string)
    except Exception as msg:
        print("An error occured! ", str(msg))
