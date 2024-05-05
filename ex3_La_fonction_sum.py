"""
    En Python, la fonction sum te permet de faire la somme des nombres d'une liste. Par exemple:

    nombres = [5,2,6,8,9,4]
    sum(nombres)
    Dans cet exercice, nous allons réecrire cette fonction mais nous la nommerons somme. 
    La fonction somme prend en entrée une liste de nombres et renvoie la somme de ces nombres. 
    Ici, vous n'avez pas le droit d'utiliser la fonction sum de Python.
    Le but de cet exercice est d'apprendre à implémenter une fonction qui existe déjà et gagner en confiance sur nos capacités à faire des choses que d'autres programmeurs plus expérimentés ont déjà fait.
"""

def somme(lists):
    som = 0
    for list in lists:
        som += list
    return som

a=[2,3,4,5,5,5,6]

print(f"the sum of numbers in the list a is {somme(a)}")