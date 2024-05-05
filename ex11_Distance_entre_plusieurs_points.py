"""
    Ecrivez une fonction qui prend une liste des nombres et qui retourne une liste qui contient la distance entre les différents nombres successifs.

    Exemple

    input : [65, 54, 59]
    output : [11, 5]
"""
# Noukoundido
def dis_point(lists):
    new_lists = []
    for i in range(len(lists) - 1):
        new_lists.append(abs(lists[i] - lists[i+1])) 

    print(new_lists)
    return new_lists

pi = [40, 54, 59,60, 45]
dis_point(pi)