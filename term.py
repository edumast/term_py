import os,sys,time,random
import time
from git import Repo
from databased import database
pasta = 'softwares/software_app/' 
pasta_bar = '/softwares/software_app/'
init=True
aspa=False
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
while( init == True ):
    command="nada"
    print(time.ctime()+" | "+database.name_usr)
    command=input("C:")
    command_d=command.split()

    if ( command_d[0] == "enter" ):
        os.system("."+pasta_bar+command_d[1]+"/init.sh")
    
    if ( command_d[0] == "down" ):
        if ( command_d[1] == "install" ):
            os.mkdir(pasta+command_d[2])
            Repo.clone_from("https://github.com/edumast/"+str(command_d[2]), pasta+command_d[2])    



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
        with open("databased/database.py", "r") as file:
	        x = file.read()
        with open("databased/database.py", "w") as file:
            x = x.replace(str(change_var)+"="+str(type_change),str(change_var)+"="+valor_new,1)
        with open('databased/database.py', 'w') as fd:
            fd.write(x)


    elif ( command == "list" ):
        for diretorio,subpastas,arquivos in os.walk(pasta):
            for arquivo in arquivos:
                #print(os.path.join(os.path.realpath(diretorio), arquivo))
                print(arquivo)
        
