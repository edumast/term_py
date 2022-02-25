#!/usr/bin/python
import os,sys,time,random
import time
from git import Repo
from databased.database import *

cwd = os.getcwd()

fixsplit="fix fix"
command_d=(fixsplit.split())
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
    os.system('tput bold') 

def color(color):
    print(color)

def rose():
    os.system("tput setaf 197")

def prin(string_print):
    print(string_print)

def clear():
    os.system("clear")

def ts2():
    os.system("tput setaf 2")

def dados_up():
    os.system('sed -i "s/in_tela=.*#end/in_tela='"'UPDATE_DADOS'"' #end/g" databased/database.py')
    os.system("./term.py")
    brek=True

def clin (clin_command):
    os.system(clin_command)

def shutdown():
    print("shutdown...")
    exit()

def exitn():
    brek=True


def inp(tp,equal,string_inp):
    if ( tp == "i" ):
        globals()[equal]=int(input(string_inp))
    elif ( tp == "s" ):
        globals()[equal]=str(input(string_inp))

def create(var,val):
    globals()[var]=val

def apps_list():
    os.system("ls softwares/software_app")

def load_file(file_load):
    os.system("."+folder_bar+file_load+"/init.sh")

def load_img(img_link):
    os.system("jp2a --color --chars=clodxkO0KXNWM img/"+img_link)

def reboot():
    os.system("./term.py")

def ini_tela():
    os.system('sed -i "s/in_tela=.*#end/in_tela='"'True'"' #end/g" databased/database.py')

def VAL(change_var,valor_new):
    os.system('sed -i "s/'+change_var+'=.*#end/'+change_var+'='+"'"+str(valor_new)+"'"+' #end/g" databased/database.py')

def down_install(folder_apps,app_in):
    os.mkdir(folder_apps+app_in)
    Repo.clone_from("https://github.com/edumast/"+str(app_in),folder_apps+str(app_in))

def change(change_var,valor_new,aspa):
    if ( change_var == "name" ):
        aspa=True

    data_eval=eval("dados."+change_var)
    type_change=(data_eval)
    if ( aspa == True ):
        type_change=("'"+type_change+"'")
        valor_new="'"+valor_new+"'"

    if ( change_var == "__err__" ):
        type_change=(__err__)
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
    #lor=["\033[1;31m","\033[1;32m"]
    m = ("welcome to termking_os %s \n" %(dados.name))
    for msg in m:
        sys.stdout.write(msg)
        sys.stdout.flush()
        time.sleep(0.06)
    print("")
    os.system("./shell/hachtag.sh")

def PROMPT():
    init_PROMPT=True
    read_file=False
    while ( init_PROMPT == True ):
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

            PROMPT_command_d=PROMPT_command.split()
        if ( PROMPT_command== " " ):
            PROMPT_command="not"
        PROMPT_command_ponto=PROMPT_command.replace(" ","(),")
        if ( PROMPT_command == "exit" ):
            init_PROMPT=False
        PROMPT_command_ponto=PROMPT_command_ponto.strip()
        PROMPT_command_ponto=PROMPT_command_ponto.replace(")()",")")
        c=(PROMPT_command_ponto)

        if ( c[-1:] == ")" ):
            escudo=True
        else:
            escudo=False

        if ( escudo == False ):
            c=(c+"()")
            print(c)
        
        eval (c)
        if ( read_file == True ):
            p=input("")
