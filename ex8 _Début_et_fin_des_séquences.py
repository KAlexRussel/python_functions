def Beg_end(var):
    vars =list(var)
    new_var =[]
    new_var.append(vars[0])
    new_var.append(vars[-1])

    if isinstance(var, list):
        print(new_var)

    elif isinstance(var, tuple):
        print(tuple(new_var))   

    elif isinstance(var, str):
        srr=""
        for news_var in new_var:
            srr = srr + news_var
        print(srr)

    else :
        print("Wrong type of variable")     

a = "aaaaaaaaaalasmd"

Beg_end(a)