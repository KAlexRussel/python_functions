"""
    Dans cet exercice, tu es appélé à écrire une fonction mot_lettre_repetee qui prend en entrée, une liste de mots. 
    Pour chaque mot, trouve la lettre qui se répète le plus. 
    La focntion retourne alors le mot ayant une lettre qui se répète le plus de fois (dans ce même mot, bien sûr).

    mot_lettre_repetee(["On", "a", "effectuee", "plusieurs", "tests", "elementaire", "ce", "matin"])
    > "elementaire"
    En cas d'égalité, n'importe quelle option vraie est juste.
"""

from collections import Counter
def mot_lettre_repetee(lists):
    greatest =""
    p=0
    for i in lists:
        counter = Counter(i)
        most_common = counter.most_common(1)
        letter, count = most_common[0]

        if count > p:
            p = count
            greatest = i

    print(greatest)
    return greatest, letter


mot_lettre_repetee(["On", "a", "effectuee", "plusieurs", "tests", "elementaire", "ce", "matin"])