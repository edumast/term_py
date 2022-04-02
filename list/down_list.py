number_receive=1
min_app=0
max_app=5
if ( number_receive > min_app):
    if ( number_receive < max_app):    
        app1="editor_py"
        app2="go"
        app3="mine"
        app4="cal"
        result=eval("app"+str(number_receive))
        print(result)
