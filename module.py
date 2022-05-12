#!/usr/bin/python
import os,sys,time,random
import time
from git import Repo
from databased.database import *
from datetime import datetime
from databased.init_data import *

#################
#Edumast,inc.
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
    time_homi=(str(timeN.hour)+":"+str(timeN.minute)+" | "+name)
    return time_homi
#time

#RGB#
OK = ('\033[92m') #GREEN
WARNING = '\033[93m' #YELLOW
FAIL = '\033[91m' #RED
RESET = '\033[0m' #RESET COLOR
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

#space_input
def space():
    space=input("")
#space_input

#update_dados
def up():
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
    print("~×~")
    os.system("ls softwares/software_app")
    os.system("tput bold")
    print(color_text+"~×~")
#app_list

#load_file_with_shell
def load_file(file_load):
    if ( file_load == "//" ):
        file_load=number_list_app(file_load)
        file_load=str(file_load)
    os.system("."+folder_bar+file_load+"/init.sh")
#load_file_with_shell

#load_img
def load_img(img_link):
    os.system("jp2a --color --chars=clodxkO0KXNWM img/"+img_link)
#load_img

#reboot_system
def reboot():
    os.system("./term.py")
#reboot_system

def number_list_app(number_receive): 
    min_app=0
    max_app=5
    print("OK")
    number_receive=int(number_receive)
    if ( number_receive > min_app):
        if ( number_receive < max_app):
            app1="editor_py"
            app2="go"
            app3="mine"
            app4="cal"
            result=eval("app"+str(number_receive))
            print(result)

#init_window_True_upd
def ini_tela():
    os.system('sed -i "s/init_window=.*#end/init_window=True #end/g" databased/database.py')
#init_window_True_upd

#set_time_day
def time_of_day():
    time=definy_time()
    if ( time.hour >= 5 ):
        time_day="dia"
    if ( time.hour >=12 ):
        time_day="tarde"
    if ( time.hour >= 18 ):
        time_day="noite"
    return time_day
#set_time_day

def definy_time():
    time = datetime.now()
    return time

def print_time():
    print(definy_time())

#change_var_sed
def VAL(change_var,valor_new):
    os.system('sed -i "s/'+change_var+'=.*#end/'+change_var+'='+"'"+str(valor_new)+"'"+' #end/g" databased/database.py')
#change_var_sed

#down_install_git_clone
def down_install(folder_apps,app_in):
    os.mkdir(folder_apps+app_in)
    Repo.clone_from("https://github.com/edumast/"+str(app_in),folder_apps+str(app_in))
#down_install_git_clone

#change_var_python_open
def change(change_var,valor_new,aspa):
    if ( change_var == "name" ):
        aspa=True

    data_eval=eval(""+change_var)
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
#change_var_python_open

#print_slow
def print_slow(print_slow):
    m = str(print_slow)
    for msg in m:
        sys.stdout.write(msg)
        sys.stdout.flush()
        time.sleep(0.06)
#print_slow

#print_slow_time
def print_slow_time(print_slow,time_slow_print):
    m = str(print_slow)
    for msg in m:
        sys.stdout.write(msg)
        sys.stdout.flush()
        time.sleep(time_slow_print)
#print_slow_time

#init_window
def init():
    os.system("./shell/hachtag.sh")
    print(RED)
    BOLD()
    print_slow("welcome to termking_os "+name)
    print("")
    print("")
    os.system("./shell/hachtag.sh")
#init_window

#Not_found
def Not_found():
    print("Not_found")
#Not_found

#PROMPT_function
def PROMPT():
    init_PROMPT=True
    read_file=False
    while ( init_PROMPT == True ):
        if ( brek == True ):
            break
        if ( read_file == False ):
            PROMPT_command=input("C:")
        if ( PROMPT_command == "file" ):
            os.system("./compiler.sh")
            os.system("./tt.py")
        if ( PROMPT_command == "file1" ):
            read_file=True
            PROMPT_command="ch"

        #old_compiler
        if ( read_file == True ):
            os.system("./compiler.sh")
            meuArquivo = open('tt.py')
            nomes = meuArquivo.read()
            PROMPT_command=str(nomes)
            PROMPT_command_d=PROMPT_command.split()
        #old_compiler

        if ( PROMPT_command== " " ):
            PROMPT_command="not"
        PROMPT_command_ponto=PROMPT_command.replace("\t","(),")
        PROMPT_command_ponto=PROMPT_command_ponto.replace("|","(),")
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
        c=c.replace(";(),","\n")
        c=c.replace(";;","\n")
        #if (PROMPT_command in globals()):
        if ( c == "()" ):
            c="Not_found()"
        eval (c)
        if ( read_file == True ):
            p=input("")
#PROMPT_function

def blue_window(tp):
    if ( tp == "info" ):
        os.system("wh_tela='true' tp_info='info' ./blue_window.sh")
    if( tp == "change" ):
        os.system("wh_tela='true' tp_info='change' ./blue_window.sh")

#command_read
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
#command_read
