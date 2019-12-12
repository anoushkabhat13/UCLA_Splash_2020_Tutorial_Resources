from os import getcwd, listdir, chdir, system

d_list = listdir(getcwd())

d_list = d_list[2:5]

for d in d_list:
    chdir(f"{d}/tutorial_name/images")
    system("touch my_file.py")
    chdir("../../..")
    
