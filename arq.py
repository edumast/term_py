import os,sys,time,random
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


def print(string_print):
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
