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
class_p=""
brek="nada"
read_file=False

OK = ('\033[92m') #GREEN
WARNING = '\033[93m' #YELLOW
FAIL = '\033[91m' #RED
RESET = '\033[0m' #RESET LOR
GREEN = '\033[92m' #GREEN
YELLOW = '\033[93m' #YELLOW
RED = '\033[91m' #RED
BLUE='\33[34m' #BLUE
def BOLD():
    os.system('tput bold') #BOLD


def prin(string_print):
    print(string_print)
def clear():
    os.system("clear")
def ts2():
    os.system("tput setaf 2")
def dados_up():
    os.system('sed -i "s/in_tela=.*#end/in_tela='"'UPDATE_DADOS'"' #end/g" databased/database')
    os.system("./term.py")
    brek=True
def shutdown():
    print("shutdown...")
def exit():
    print("os")
    brek=True

def change(change_var,valor_new,aspa):
    if ( change_info == "name" ):
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
   
#init_style
def init():
    os.system("./shell/hachtag.sh")
    print(RED)
    BOLD()
    lor=["\033[1;31m","\033[1;32m"]
    m = ("welcome to termking_os %s \n" %(database.dados.name))
    for msg in m:
        sys.stdout.write(msg)
        sys.stdout.flush()
        time.sleep(0.06)
    print("")
    os.system("./shell/hachtag.sh")
#OK
#os.system("tput setaf 2")
if ( database.dados.in_tela == 'True' ):
    init()
    init_w=True
BOLD()
#init_style
if ( database.dados.in_tela == "UPDATE_DADOS" ):
    os.system('sed -i "s/in_tela=.*#end/in_tela='"'True'"' #end/g" databased/database.py')
while(init_w == True ):
    
    #command
    os.system("tput setaf 197")
    print(time.ctime()+" | "+database.dados.name)
    command=input(GREEN+"C:")
    if ( command == "" ):
        command="fix"
    command_d=command.split()
    #command
    
    if ( command_d[0] == "PROMPT"):
        print(GREEN)

    while ( command_d[0] == "PROMPT"):
        if ( brek == True ):
            break
        if ( read_file == False ):
            PROMPT_command=input("C:")
            if ( PROMPT_command == "file" ):
                read_file=True
                PROMPT_command="ch"
        
        if ( read_file == True ):
            os.system("./compiler.sh")
            meuArquivo = open('tt.py')
            nomes = meuArquivo.read()
            PROMPT_command=str(nomes)
            print(PROMPT_command)
            PROMPT_command_d=PROMPT_command.split()
        if ( PROMPT_command== " " ):
            PROMPT_command="not"

        PROMPT_command_ponto=PROMPT_command.replace(" ","(),")
        
        if ( PROMPT_command == "exit" ):
            command="nada."
        PROMPT_command_ponto=PROMPT_command_ponto.strip()
        PROMPT_command_ponto=PROMPT_command_ponto.replace(")()",")")
        c=(PROMPT_command_ponto)
        print(c)
        if ( c[-1:] == ")" ):
            escudo=True
        else:
            escudo=False
       
        if ( escudo == False ):           
            c=(c+"()")
            print(c)
        if ( PROMPT_command_d[0] == "ch" ):
            class_p=" "
        else:
            print(c)
            eval (c)
        if ( read_file == True ):
            p=input("")
    if ( command_d[0] == "upd"):
        dados_up()


    if ( command_d[0] == "clear" ):
        clear()
           
    if ( command_d[0] == "shutdown" ):
        shutdown()
        exit()
     
    if ( brek == True ):
        break

    if ( command_d[0] == "reboot" ):
        clear()
        os.system("./term.py")
        break

    #mman
    if ( command_d[0] == "comman" ):
        print("enter | down | apps | change | VAL")
    #mman

    #enter
    if ( command_d[0] == "enter" ):
        ts2()
        os.system("."+folder_bar+command_d[1]+"/init.sh")
    #enter

    #down
    if ( command_d[0] == "down" ):
        if ( command_d[1] == "install" ):
            os.mkdir(folder_apps+command_d[2])
            Repo.clone_from("https://github.m/edumast/"+str(cocommand_d[2]), folder_apps+command_d[2])    
    #down

    #change
    if ( command_d[0] == "change" ):
        change_var="__err__"
        change_info=command_d[1]
        valor_new=command_d[2]
        change_var=change_info
        change(change_var,valor_new,aspa)

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
