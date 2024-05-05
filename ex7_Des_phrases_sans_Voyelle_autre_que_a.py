"""
    Modifie la précedente fonction pour quelle prenne desormais en entrée une phrase, c'est à dire des mots séparés par des espaces.
    Il enlève toutes les voyelles sauf la lettre a.
"""

def rem_voyelle(word):
    list_voyelle = ["e","i","o","u","y"]
    new_list = ""
    for wor in word:
        if wor not in  list_voyelle:
            new_list = new_list + wor

    print(new_list)
    return new_list


a = "alex russel est un mignon garcon"

rem_voyelle(a)