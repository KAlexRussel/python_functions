"""
    Dans cet exercice, vous allez écrire une fonction qui prend entrée, une liste de nombre et retourne une liste contenant:

    La somme des éléments d'index pairs
    La somme des éléments d'index impairs
    somme_pair_impair([10,20,30,40,50,60])
    > [90, 120]
"""
def somme_pair_impair(lists):
    fin_list = []
    pair = 0
    impair =0

    for i in lists:
        if (lists.index(i) % 2) == 0:
            pair += i 
        else:
            impair += i 
    
    fin_list.append(pair)
    fin_list.append(impair)

    print(fin_list)
    return fin_list


somme_pair_impair([10,20,30,40,50,60])
