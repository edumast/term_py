#!/usr/bin/python
import os,sys,time,random
import time
from git import Repo
from databased import database

cwd = os.getcwd()

folder_apps = 'softwares/software_app/' 
folder_bar = '/softwares/software_app/'
init=True
aspa=False
class_p="co"
brek="nada"

class RGB:
    OK = ('\033[92m') #GREEN
    WARNING = '\033[93m' #YELLOW
    FAIL = '\033[91m' #RED
    RESET = '\033[0m' #RESET COLOR
    GREEN = '\033[92m' #GREEN
    YELLOW = '\033[93m' #YELLOW
    RED = '\033[91m' #RED
    BLUE='\33[34m' #BLUE
    def BOLD():
        os.system('tput bold') #BOLD

class co():

    def clear():
            os.system("clear")
    def ts2():
        os.system("tput setaf 2")
    def dados_up():
        os.system('sed -i "s/in_tela=.*#end/in_tela='"'UPDATE_DADOS'"' #end/g" databased/database.py')
        os.system("./term.py")
        brek=True

#init_style
if ( database.dados.in_tela == 'True' ):
    os.system("./shell/hachtag.sh")
    print(RGB.RED)
    RGB.BOLD()
    color=["\033[1;31m","\033[1;32m"]
    m = ("welcome to termking_os %s \n" %(database.dados.name))
    for msg in m:
        sys.stdout.write(msg)
        sys.stdout.flush()
        time.sleep(0.06)
    print("")
    os.system("./shell/hachtag.sh")
#RGB.OK
#os.system("tput setaf 2")
RGB.BOLD()
#init_style
if ( database.dados.in_tela == "UPDATE_DADOS" ):
    os.system('sed -i "s/in_tela=.*#end/in_tela='"'True'"' #end/g" databased/database.py')
while( init == True ):

    if ( brek == True ):
        break
        break
    
    #command
    os.system("tput setaf 197")
    print(time.ctime()+" | "+database.dados.name)
    command=input(RGB.GREEN+"C:")
    if ( command == "" ):
        command="fix"
    command_d=command.split()
    #command
    
    while ( command_d[0] == "PROMPT"):
        PROMPT_command=input(RGB.GREEN+class_p+"/"+"C:")
        PROMPT_command_d=PROMPT_command.split()
        if (PROMPT_command_d[0] == "" ):
            PROMPT_command_d[0]="not"
        PROMPT_command_ponto=PROMPT_command.replace(" ",".")
        if ( PROMPT_command_d[0] == "exit" ):
            command_d[0]="nada."
        c=(class_p+"."+(PROMPT_command_ponto)+"()")
        if ( PROMPT_command_d[0] == "ch" ):
            class_p=PROMPT_command_d[1]
        else:
            eval (c)
    if ( command_d[0] == "upd"):
        co.dados_up()


    if ( command_d[0] == "clear" ):
        co.clear()
           
    if ( command_d[0] == "shutdown" ):
        print("shutdown...")
        break

    if ( command_d[0] == "reboot" ):
        co.clear()
        os.system("./term.py")
        break

    #comman
    if ( command_d[0] == "comman" ):
        print("enter | down | apps | change | VAL")
    #comman

    #enter
    if ( command_d[0] == "enter" ):
        co.ts2()
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
            change_var="age"
        
        if ( change_info == "name" ):
            change_var="name"
            aspa=True

        data_eval=eval("database.dados."+change_var)
        type_change=(data_eval)
        if ( aspa == True ):
            type_change=("'"+type_change+"'")
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

    #val 
    if ( command_d[0] == "VAL" ):
        change_var=command_d[1] 
        valor_new=command_d[2]
        os.system('sed -i "s/'+change_var+'=.*#end/'+change_var+'='+"'"+str(valor_new)+"'"+' #end/g" databased/database.py')
    #val

    #apps
    if ( command_d[0] == "apps" ):
        folder_apps_list="softwares/software_app/"
        os.system("ls softwares/software_app")
        os.system("tput setaf 197")
        os.system("tput bold")
    #apps    
