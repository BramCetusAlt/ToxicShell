import subprocess, os


run = True

while run == True:
    try:
        command = str(input("ToxicShell:>"))
        if command == "exit" or command == "Exit":
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
    
    
