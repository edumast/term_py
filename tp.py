import os,sys,time,random
from databased import database
pasta = 'databased/'
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
    command=input("C:")
    if ( command == "change" ):
        change_info="__er!n__"
        change_info=input("what changed?:")
        valor_new=input("valor:")
        if ( change_info == "age" ):
            change_var="age_usr"
            type_change=(database.age_usr)
        if ( change_info == "name" ):
            change_var="name_usr"
            type_change=("'"+database.name_usr+"'")
            aspa=True
        if ( aspa == True ):
            valor_new="'"+valor_new+"'"
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
        
