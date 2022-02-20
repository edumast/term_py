import os,sys,time,random
import time
from git import Repo
from databased import database

cwd = os.getcwd()

folder_apps = 'softwares/software_app/' 
folder_bar = '/softwares/software_app/'
init=True
aspa=False

#init_style
if ( database.in_tela == 'True' ):
    os.system("./shell/hachtag.sh")
    print("")
    os.system("tput setaf 1")
    os.system("tput bold")
    color=["\033[1;31m","\033[1;32m"]
    m = ("welcome to termking_os %s \n" %(database.name_usr))
    for msg in m:
        sys.stdout.write(msg)
        sys.stdout.flush()
        time.sleep(0.06)
    print("")
    os.system("./shell/hachtag.sh")
os.system("tput setaf 2")
os.system("tput bold")
#init_style

while( init == True ):
    
    #fix
    command="__nothing__"
    #fix

    #command
    print(time.ctime()+" | "+database.name_usr)
    command=input("C:")
    command_d=command.split()
    #command
    #enter
    if ( command_d[0] == "enter" ):
        os.system("."+folder_bar+command_d[1]+"/init.sh")
    #enter

    #down
    if ( command_d[0] == "down" ):
        if ( command_d[1] == "install" ):
            os.mkdir(folder_apps+command_d[2])
            Repo.clone_from("https://github.com/edumast/"+str(command_d[2]), folder_apps+command_d[2])    
    #down

    #change
    if ( command_d[0] == "change" ):
        change_var="__err__"
        change_info=command_d[1]
        valor_new=command_d[2]
        
        if ( change_info == "age" ):
            change_var="age_usr"
            type_change=(database.age_usr)
        
        if ( change_info == "name" ):
            change_var="name_usr"
            type_change=("'"+database.name_usr+"'")
            aspa=True
        
        if ( aspa == True ):
            valor_new="'"+valor_new+"'"
        
        if ( change_var == "__err__" ):
            type_change=(database.__err__)
            valor_new='err'
        data_ex='True'
        with open("databased/database.py", "r") as file:
	        x = file.read()
        with open("databased/database.py", "w") as file:
            x = x.replace(str(change_var)+"="+str(type_change),str(change_var)+"="+valor_new,1)
        with open('databased/database.py', 'w') as fd:
            fd.write(x)
        data_ex=False
    #change
    if ( command_d[0] == "VAL" ):
        change_var=command_d[1] 
	    
        valor_new=command_d[2]
        os.system('sed -i "s/'+change_var+'=.*#end/'+change_var+'='+"'"+str(valor_new)+"'"+' #end/g" databased/database.py')
    #apps
    if ( command_d[0] == "apps" ):
        folder_apps_list="softwares/software_app/"
        os.system("ls softwares/software_app")
        os.system("tput setaf 2")
        os.system("tput bold")
    #apps    
