import os
import sys

SELECT_ONE = "Select the file you want to compile: "
SELECT_MAIN = "Select the main file: "
SELECT_DEPENDENCIES = "Select the files you want to make dependencies: "

def get_c_files():
    c_files = []
    files = os.listdir()
    for file in files:
        if file.endswith(".c"):
            c_files.append(file) 
    return c_files

def select_dependencies(c_files):
    print("Select the files you want to make dependencies")
    for i in range(len(c_files)):
        print(f"{i+1}. {c_files[i]}")
    print("Enter the numbers separated by a space: ")
    selected_files = list(map(int, input().split()))
    return [c_files[i-1] for i in selected_files]

def select_c_file(c_files, msg=SELECT_ONE):
    print(msg)
    for i in range(len(c_files)):
        print(f"{i+1}. {c_files[i]}")
    selection = input("Enter the number: ")
    return c_files[int(selection)-1]

def generate_makefile(selected_files):
    with open("makefile", "w") as f:
        for file in selected_files:
            print(file)
            f.write(f"{file.split('.')[0]}: {file.split('.')[0]}.o\n")
            f.write(f"\tgcc -o {file.split('.')[0]} {file.split('.')[0]}.o\n")
        f.write("clean:\n")
        for file in selected_files:
            f.write(f"\trm -f {file.split('.')[0]} {file.split('.')[0]}.o\n")
    
c_list = get_c_files()

if "--one" in sys.argv:
    selected_file = select_c_file(c_list)
    generate_makefile([selected_file])
elif "--all" in sys.argv:
    generate_makefile(c_list)
elif "--select" in sys.argv:
    main = select_c_file(c_list, SELECT_MAIN)
    dependencies = select_dependencies(c_list)
    print(main, dependencies)