from datetime import date
import os

test = 0
#--------Inputs--------#
def get_file_location():
    global Files_location
    Files_location = input("Path you want for Driver files : ")
get_file_location()
while (test == 0):
    try:
        os.chdir(Files_location)
    except OSError:
        print("Invalid path !!")
        get_file_location()
        test = 0
    else:
        test = 1
        Driver_Name = input("Driver Name : ")
        Author_Name = input("Author Name : ")

        Date = str(date.today())


        #--------Interface file--------# 
        Interface_file = open(Driver_Name+"_interface.h",'w')
        Interface_file.write("/**********************************************/\n")
        Interface_file.write("/* Author   : "+Author_Name+" "*(32-len(Author_Name))+"*/\n")
        Interface_file.write("/* Date     : "+Date+" "*(32-len(Date))+"*/\n")
        Interface_file.write("/* Version  : V01                             */\n")
        Interface_file.write("/**********************************************/\n")
        Interface_file.write("#ifndef "+Driver_Name.upper()+"_INTERFACE_H\n")
        Interface_file.write("#define "+Driver_Name.upper()+"_INTERFACE_H\n\n")
        Interface_file.write("#endif")

        Interface_file.close()

        #--------Private file--------# 
        Private_file = open(Driver_Name+"_private.h",'w')
        Private_file.write("/**********************************************/\n")
        Private_file.write("/* Author   : "+Author_Name+" "*(32-len(Author_Name))+"*/\n")
        Private_file.write("/* Date     : "+Date+" "*(32-len(Date))+"*/\n")
        Private_file.write("/* Version  : V01                             */\n")
        Private_file.write("/**********************************************/\n")
        Private_file.write("#ifndef "+Driver_Name.upper()+"_PRIVATE_H\n")
        Private_file.write("#define "+Driver_Name.upper()+"_PRIVATE_H\n\n")
        Private_file.write("#endif")

        Private_file.close()

        #--------Config file--------# 
        Config_file = open(Driver_Name+"_config.h",'w')
        Config_file.write("/**********************************************/\n")
        Config_file.write("/* Author   : "+Author_Name+" "*(32-len(Author_Name))+"*/\n")
        Config_file.write("/* Date     : "+Date+" "*(32-len(Date))+"*/\n")
        Config_file.write("/* Version  : V01                             */\n")
        Config_file.write("/**********************************************/\n")
        Config_file.write("#ifndef "+Driver_Name.upper()+"_CONFIG_H\n")
        Config_file.write("#define "+Driver_Name.upper()+"_CONFIG_H\n\n")
        Config_file.write("#endif")

        Config_file.close()

        #--------Prog file--------# 
        Prog_file = open(Driver_Name+"_program.c",'w')
        Prog_file.write("/**********************************************/\n")
        Prog_file.write("/* Author   : "+Author_Name+" "*(32-len(Author_Name))+"*/\n")
        Prog_file.write("/* Date     : "+Date+" "*(32-len(Date))+"*/\n")
        Prog_file.write("/* Version  : V01                             */\n")
        Prog_file.write("/**********************************************/\n")
        Prog_file.write("#include "+' "'+Driver_Name+'_interface.h"\n')
        Prog_file.write("#include "+' "'+Driver_Name+'_config.h"\n')
        Prog_file.write("#include "+' "'+Driver_Name+'_private.h"\n')

        Prog_file.close()

        print("Done !!")

