"""
    A quoi ressemblerait le Français sans voyelle ? Nous allons écrire une fonction qui prend une chaine de caractères et enlève les voyelles.
"""
def rem_voyelle(word):
    list_voyelle = ["a","e","i","o","u","y"]
    new_list = ""
    for wor in word:
        if wor not in  list_voyelle:
            new_list = new_list + wor

    print(new_list)
    return new_list


a = "akexrussel"

rem_voyelle(a)