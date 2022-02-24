fixsplit="fix fix"
command_d=(fixsplit.split)
from module import *

#os.system("tput setaf 2")
if ( dados.in_tela == 'True' ):
    init()
    init_w=True
BOLD()
#init_style
if ( dados.in_tela == "UPDATE_DADOS" ):
    os.system('sed -i "s/in_tela=.*#end/in_tela='"'True'"' #end/g" /database.py')
while(init_w == True ):
    
    #command
    os.system("tput setaf 197")
    print(time.ctime()+" | "+dados.name)
    command=input(GREEN+"C:")
    if ( command == "" ):
        command="fix"
    command_d=command.split()
    #command
    
    if ( command_d[0] == "PROMPT"):
        PROMPT()
        print(GREEN)

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
        os.system('sed -i "s/'+change_var+'=.*#end/'+change_var+'='+"'"+str(valor_new)+"'"+' #end/g" /database.py')
    #val

    #apps
    if ( command_d[0] == "apps" ):
        folder_apps_list="softwares/software_app/"
        os.system("ls softwares/software_app")
        os.system("tput setaf 197")
        os.system("tput bold")
    #apps    
