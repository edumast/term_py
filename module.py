#!/usr/bin/python
import os,sys,time,random
import time
from git import Repo
from databased.database import *
from datetime import datetime
from databased.init_data import *

#################
#Edumast,inc
#################

cwd = os.getcwd()

os.system("tput setaf 2")


fixsplit="fix fix"
command_d=(fixsplit.split())
folder_apps = 'softwares/software_app/'
folder_bar = '/softwares/software_app/'
init=True
aspa=False
class_p=""
brek="nada"
read_file=False

#type
i="i"
s="s"
#type

#time

def up_time():
    timeN = datetime.now()
    time_homi=(str(timeN.hour)+":"+str(timeN.minute)+" | "+dados.name)
    return time_homi
#time

#RGB#
OK = ('\033[92m') #GREEN
WARNING = '\033[93m' #YELLOW
FAIL = '\033[91m' #RED
RESET = '\033[0m' #RESET LOR
GREEN = '\033[92m' #GREEN
YELLOW = '\033[93m' #YELLOW
RED = '\033[91m' #RED
BLUE='\33[34m' #BLUE
#RGB#

#WINDOW#
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
#WINDOW#

#update_dados
def dados_up():
    os.system('sed -i "s/init_window=.*#end/init_window=False #end/g" databased/database.py')
    os.system("./term.py")
    brek=True
#update_dados

#shell command
def clin (clin_command):
    os.system(clin_command)
#shell command

#shutdown
def shutdown():
    print("shutdown...")
    exit()
#shutdown 

#exit
def exitn():
    brek=True
#exit

#input
def inp(tp,equal,string_inp):
    if ( tp == "i" ):
        globals()[equal]=int(input(string_inp))
    elif ( tp == "s" ):
        globals()[equal]=str(input(string_inp))
#input

#create var
def create(var,val):
    globals()[var]=val
#create var

#app_list
def apps_list():
    os.system("ls softwares/software_app")
#app_list

#load_file_with_shell
def load_file(file_load):
    os.system("."+folder_bar+file_load+"/init.sh")
#load_file_with_shell

def load_img(img_link):
    os.system("jp2a --color --chars=clodxkO0KXNWM img/"+img_link)

def reboot():
    os.system("./term.py")

def ini_tela():
    os.system('sed -i "s/init_window=.*#end/init_window=True #end/g" databased/database.py')

def time_of_day():
    now = datetime.now()
    if ( now.hour >= 5 ):
        time_day="dia"
    if ( now.hour >=12 ):
        time_day="tarde"
    if ( now.hour >= 18 ):
        time_day="noite"
    return time_day

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

def print_slow(print_slow):
    m = str(print_slow)
    for msg in m:
        sys.stdout.write(msg)
        sys.stdout.flush()
        time.sleep(0.06)

def init():
    os.system("./shell/hachtag.sh")
    print(RED)
    BOLD()
    print_slow("welcome to termking_os "+dados.name)
    print("")
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
        PROMPT_command_ponto=PROMPT_command.replace("\t","(),")
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
        #if (PROMPT_command in globals()):
        eval (c)
        if ( read_file == True ):
            p=input("")
def Read_command():
    #command
    rose()
    #time.ctime
    time_homi=up_time()
    print("termking | "+str(time_homi))
    command=input(color_text+"C:")
    if ( command == "" ):
        command="fix"
    return command
    #command
