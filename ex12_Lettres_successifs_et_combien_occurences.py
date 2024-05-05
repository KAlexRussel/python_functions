"""
    Ecrivez une fonction qui prend en input une chaine de caractères contenant des lettres et retourne une liste de tuple qui contient successivement chaque lettre et le nombre d'occurences successives. Exemple :

    input : 'aaaccdaad"
    output : [(a,3), (c, 2), (d, 1), (a,2), (d, 1)]
"""

def lett_succ(strings):
    lis_tuples = []
    already = []
    a=""
    ind =0
    for i in strings:
        
        if a != i:
            already =[]

        a=i


        if i not in already:

            already.append(i)
            lis = []
            lis.append(i)
            val=0
            for j in strings[ind:]:
                if j == i:
                    val += 1
            lis.append(val) 
            # print(lis)
 
            lis_tuples.append(tuple(lis))
        ind += 1

    print(lis_tuples)
    return lis_tuples

lett_succ("aaaccdaad")


            
 





