def email_gen():
    nom = input("Entre vontre nom de famille: ").lower()
    prenom = input("Entre votre prenom: ").lower()
    
    print(f"{prenom}_{nom}@pythonboss.com")
    return f"{prenom}_{nom}@pythonboss.com"

email_gen()