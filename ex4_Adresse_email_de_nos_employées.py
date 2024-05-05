"""
    Vous êtes chargé d'octroyer les emails des nouveaux employés de votre entreprise. 
    Vous travaillez chez PythonBoss.
    L'adresse email de vos employés est sous le format prenom_nom@pythonboss.com. 
    Vous souhaitez écrire un programme pour automatiser cela. La programme demande à un utilisateur son prenom, puis son nom et affiche son adresse email.
    Par exemple Kevin Degila aura comme adresse email : kevin_degila@pythonboss.com . 
    Ici vous devrez remarquer que l'adresse email ne contient que des lettres miniscules: C'est la préférence du directeur de PythonBoss.
    Vous avez intérêt à le satisfaire.
"""
def email_gen():
    nom = input("Entre vontre nom de famille: ").lower()
    prenom = input("Entre votre prenom: ").lower()
    
    print(f"{prenom}_{nom}@pythonboss.com")
    return f"{prenom}_{nom}@pythonboss.com"

email_gen()