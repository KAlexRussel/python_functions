"""
    Dans cet exercice, vous allez écrire une fonction ordonne_str qui prend une chaîne de caractères (string) et retourne ce même string mais en l'ordonnant par ordre alphabétique.
"""
def ordonne_str(st):
    lettre_alphabet=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    new_str = ""
    for i in range(len(lettre_alphabet)):
        if lettre_alphabet[i] in st.lower():
            new_str = new_str + lettre_alphabet[i]
    print(new_str)
    
    return new_str

ordonne_str('Python')
