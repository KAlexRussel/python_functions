"""
    En Python, les listes, les tuples et les strings sont des séquences. 
    En Python, on peut écrire une fonction qui prend différents types de variables. 
    Dans cet exercice, nous allons écrire une fonction qui prend en Entrée, une liste, un tuple ou un string et retourne une variable du même type mais avec le premier et le dernier élément de la séquence.

"""
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