#I have tested this code for winows and it works please chech it for other systems
#
# where ever you see C:\\Users\\Nathaniel\\Dropbox\\code change it and put the path to your dropbox
#
# this was the path for my dropox therefor it may not work for you
#
#i have a common place where i store all my projects locally that location is E:\\code\\codes\\" 
#
#please replace that location with your computer
#
#
#
#
#
#
#
#

import os
import shutil



print("import \nexport \nexit")
choice=input()




while(choice != "exit"):
    if(choice == "import"):
        
        os.system("cls")
        dir_dst = "C:\\Users\\Nathaniel\\Dropbox\\code"

        project_name = input("project name:- ")

        if(project_name == "exit()"):

            exit()

        temp_dir_src = "E:\\code\\codes\\"

        dir_src = temp_dir_src + project_name

        dest_folder_name = "C:\\Users\\Nathaniel\\Dropbox\\code\\" + project_name

        os.mkdir(dest_folder_name)

        for file in os.listdir(dir_src):
            print(file)# testing
            src_file = os.path.join(dir_src, file)
            dst_file = os.path.join(dir_dst, file)
            shutil.move(src_file, dest_folder_name)

        print("transfer complete")
        
        print("import \nexport \nexit")
        choice=input()

    #
    #dir_src = the initial places where the file is located along with the project name 
    #dir_dst = has the directory destination without the project name
    #dest_folder_name = has te destanation path along with the project name

    def trans(src_dir, dest_dir , dest_dir_pro):


        src_dir = dir_src
        dest_dir= dir_dst
        dest_dir_pro = dest_folder_name

        os.mkdir(dest_folder_name)
        for file in os.listdir(dir_src):
            print(file)# testing
            src_file = os.path.join(dir_src, file)
            dst_file = os.path.join(dir_dst, file)
            shutil.move(src_file, dest_folder_name)
        print("transfer complete")

    #
    #
    #if(choice == "export"):
    #    os.system("cls")
    #    dir_dst = "C:\\Users\\Nathaniel\\Dropbox\\code"
    #    project_name = input("project name:- ")
    #    temp_dir_src = "E:\\code\\codes\\"
    #    dir_src = temp_dir_src + project_name
    #    dest_folder_name = "C:\\Users\\Nathaniel\\Dropbox\\code\\" + project_name
    #    os.mkdir(dest_folder_name)
    #    for file in os.listdir(dir_src):
    #        print(file)# testing
    #        src_file = os.path.join(dir_src, file)
    #        dst_file = os.path.join(dir_dst, file)
    #        shutil.move(src_file, dest_folder_name)
    #    print("transfer complete")
    #
    #
    #    os.system("cls")
    #    project_name = input("Project name:- ")
    #    temp_dir_dest = "E:\\code\\codes\\" + project_name
    #    os.mkdir(temp_dir_dest)
    #
    #
    #    src_folder_name = "C:\\Users\\Nathaniel\\Dropbox\\code\\" + project_name
    #    for file in os.listdir(dir_src):
    #        print(file)# testing
    #        src_file = os.path.join(dir_src, file)
    #        dst_file = os.path.join(dir_dst, file)
    #        shutil.move(src_file, dest_folder_name)
    #    print("transfer complete")
    #
    #if(choice == "export"):
       # os.system("cls")
       # project_name = input("project name:- ")
       # dir_src = "C:\\Users\\Nathaniel\\Dropbox\\code"
       # temp_dir_dst = "E:\\code\\codes\\"
       # dir_dest = "E:\\code\\codes\\" + project_name
       # os.mkdir(dir_dest)
    #
       # 
       # #dir_src = temp_dir_src + project_name
       # #dest_folder_name = "C:\\Users\\Nathaniel\\Dropbox\\code\\" + project_name
       # #os.mkdir(dir_dest)
       # for file in os.listdir(dir_src):
       #     print(file)# testing
       #     src_file = os.path.join(dir_src, file)
       #     dst_file = os.path.join(dir_dst, file)
       #     shutil.move(src_file, dir_dest)
       # print("transfer complete")


    if(choice=="export"):
        os.system("cls")
        project_name = input("Project name:- ")
        if(project_name == "exit()"):
            exit()
        dir_src = "C:\\Users\\Nathaniel\\Dropbox\\code\\" + project_name
        dir_dst  = "E:\\code\\codes\\" 
        dest_folder_name = "E:\\code\\codes\\" + project_name
        #trans(src_dir,dest_dir,dest_dir_pro)




        os.mkdir(dest_folder_name)
        for file in os.listdir(dir_src):
            print(file)# testing
            src_file = os.path.join(dir_src, file)
            dst_file = os.path.join(dir_dst, file)
            shutil.move(src_file, dest_folder_name)
        print("transfer complete")

        print("import \nexport \nexit")
        choice=input()






