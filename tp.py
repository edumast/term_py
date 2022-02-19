import os
from databased import database
pasta = 'databased/'
init=True
print("welcome "+database.name_usr)
while( init == True ):
    command=input("C:")
    if ( command == "change" ):
        change_info=input("what changed?:")
        if ( change_info == "age" ):
            age_new=input("age:")
            with open("databased/database.py", "r") as file:
	            x = file.read()
	
            with open("databased/database.py", "w") as file:
    
                x = x.replace("age_usr="+str(database.age_usr),"age_usr="+age_new,1)
            with open('databased/database.py', 'w') as fd:
                fd.write(x)
    elif ( command == "list" ):
        for diretorio,subpastas,arquivos in os.walk(pasta):
            for arquivo in arquivos:
                #print(os.path.join(os.path.realpath(diretorio), arquivo))
                print(arquivo)
        
