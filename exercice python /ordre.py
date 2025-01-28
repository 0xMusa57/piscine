## AJOUT NV INDIVIDU NOmmé MUSA  AJOUT NV INDIVIDU NOmmé MUSA  AJOUT NV INDIVIDU NOmmé MUSA






liste = [
    ("Pierre", "Dos", 10),
    ("Paul", "Brasse", 13),
    ("Léa", "Crawl", 6),
    ("Léa", "Brasse", 8),
    ("Musa", "Papillon", 15)  # Ajout du nouveau nageur avec une nouvelle nage
]
commande = ''

def cmd_ajout(liste):
    """Ajoute un évènement à la liste"""
    a = input("Qui nage ? ")
    b = input("quelle nage ? ")
    c = int(input("combien de longueur ? "))  # Conversion en entier
    liste.append((a,b,c))

def cmd_liste(liste):
    """Affiche toutes les performances des nageurs"""
    print("Prénom      |  nage   |  longueur")
    print("---------------------------------")
    for elt in liste:
        print(f" {elt[0]:11}| {elt[1]:8}|  {elt[2]}")

def cmd_nageur(liste):
    """Affiche toutes les performances d'un nageur"""
    tmp = input("Quel nageur ? ")
    print("Performances de ", tmp)
    print("  nage   |  longueur")
    print("--------------------")
    for elt in liste:
        if elt[0]== tmp:
            print(f" {elt[1]:8}|  {elt[2]}")

def cmd_nage(liste):
    """Affiche toutes les performances suivant une nage donnée"""
    tmp = input("Quel nage ? ")
    print("Nage ", tmp)
    print(" Nageur     |  longueur")
    print("------------------------")
    for elt in liste:
        if elt[1]== tmp:
            print(f" {elt[0]:11}|  {elt[2]}")

def cmd_performance(liste):
    """Gestion des performances"""
    print("\nGestion des performances:")
    print("1. Afficher les meilleures performances par nage")
    print("2. Afficher les meilleures performances par nageur")
    print("3. Afficher le record absolu")
    choix = input("Votre choix (1-3) ? ")
    
    if choix == "1":
        # Meilleures performances par nage
        nages = set(elt[1] for elt in liste)  # Ensemble unique des nages
        print("\nMeilleures performances par nage:")
        print("Nage      | Nageur      | Longueur")
        print("----------------------------------")
        for nage in nages:
            performances_nage = [(elt[0], elt[2]) for elt in liste if elt[1] == nage]
            meilleur_nageur, meilleure_perf = max(performances_nage, key=lambda x: x[1])
            print(f" {nage:9}| {meilleur_nageur:11}| {meilleure_perf}")
    
    elif choix == "2":
        # Meilleures performances par nageur
        nageurs = set(elt[0] for elt in liste)  # Ensemble unique des nageurs
        print("\nMeilleures performances par nageur:")
        print("Nageur      | Nage      | Longueur")
        print("----------------------------------")
        for nageur in nageurs:
            performances_nageur = [(elt[1], elt[2]) for elt in liste if elt[0] == nageur]
            meilleure_nage, meilleure_perf = max(performances_nageur, key=lambda x: x[1])
            print(f" {nageur:11}| {meilleure_nage:9}| {meilleure_perf}")
    
    elif choix == "3":
        # Record absolu
        meilleur_nageur, meilleure_nage, meilleure_perf = max(liste, key=lambda x: x[2])
        print("\nRecord absolu:")
        print(f"Nageur: {meilleur_nageur}")
        print(f"Nage: {meilleure_nage}")
        print(f"Longueur: {meilleure_perf}")

def cmd_exit(liste):
    tmp = input("En êtes-vous sûr ? (o)ui/(n)on ")
    if tmp == 'o':
        cmd_save(liste, 'save.backup')
        return False
    else:
        return True

def cmd_save(liste, filename):
    '''sauvegarde la BDD'''
    fichier = open(filename, 'w')
    for elt in liste:
        fichier.write(elt[0]+','+elt[1]+','+str(elt[2])+"\n")
    fichier.close()

def cmd_load(liste, filename):
    'charge la BDD'
    fichier = open(filename, 'r')
    for line in fichier:
        line = line.strip()
        if line[-1] == '\n':
            line = line[:-1]
        if line[0]=='#':
            continue
        tmp = line.split(',')
        tmp[2] = int(tmp[2])  # Conversion en entier
        liste.append(tuple(tmp))
    fichier.close()

def get_cmd():
    '''Traitement de la commande d'entrée'''
    msg = input("Que faut-il faire ? ")
    msg = msg.lower()
    return msg

isAlive = True
while isAlive:
    commande = get_cmd()
    if commande == 'ajout':
        cmd_ajout(liste)
        continue
    if commande == 'liste':
        cmd_liste(liste)
        continue
    if commande == 'nageur':
        cmd_nageur(liste)
        continue
    if commande == 'nage':
        cmd_nage(liste)
        continue
    if commande == 'performance':
        cmd_performance(liste)
        continue
    if commande == 'save':
        cmd_save(liste, 'save.csv')
        continue
    if commande == 'load':
        cmd_load(liste, 'save.csv')
        continue
    if commande == 'exit':
        isAlive = cmd_exit(liste)
        continue
    print(f"Commande {commande} inconnue")



    ## PROCHAIN COMMIT MENU DEDIE MUSA

    liste = [
    ("Pierre", "Dos", 10),
    ("Paul", "Brasse", 13),
    ("Léa", "Crawl", 6),
    ("Léa", "Brasse", 8),
    ("Musa", "Papillon", 15)
]
commande = ''

def cmd_ajout(liste):
    """Ajoute un évènement à la liste"""
    a = input("Qui nage ? ")
    b = input("quelle nage ? ")
    c = int(input("combien de longueur ? "))
    liste.append((a,b,c))

def cmd_liste(liste):
    """Affiche toutes les performances des nageurs"""
    print("\nToutes les performances:")
    print("Prénom      |  nage   |  longueur")
    print("---------------------------------")
    for elt in liste:
        print(f" {elt[0]:11}| {elt[1]:8}|  {elt[2]}")

def cmd_nageur(liste):
    """Affiche toutes les performances d'un nageur"""
    tmp = input("Quel nageur ? ")
    print("\nPerformances de", tmp)
    print("  nage   |  longueur")
    print("--------------------")
    for elt in liste:
        if elt[0]== tmp:
            print(f" {elt[1]:8}|  {elt[2]}")

def cmd_nage(liste):
    """Affiche toutes les performances suivant une nage donnée"""
    tmp = input("Quel nage ? ")
    print("\nNage", tmp)
    print(" Nageur     |  longueur")
    print("------------------------")
    for elt in liste:
        if elt[1]== tmp:
            print(f" {elt[0]:11}|  {elt[2]}")

def cmd_visualisation(liste):
    """Menu de visualisation des performances"""
    while True:
        print("\nMenu de visualisation:")
        print("1. Voir toutes les performances")
        print("2. Voir les performances d'un nageur")
        print("3. Voir tous les nageurs par type de nage")
        print("4. Voir le résumé global")
        print("5. Retour au menu principal")
        
        choix = input("\nVotre choix (1-5) ? ")
        
        if choix == "1":
            cmd_liste(liste)
        
        elif choix == "2":
            # Afficher la liste des nageurs disponibles
            nageurs = sorted(set(elt[0] for elt in liste))
            print("\nNageurs disponibles:", ", ".join(nageurs))
            cmd_nageur(liste)
        
        elif choix == "3":
            # Afficher la liste des nages disponibles
            nages = sorted(set(elt[1] for elt in liste))
            print("\nNages disponibles:", ", ".join(nages))
            cmd_nage(liste)
        
        elif choix == "4":
            # Résumé global
            nageurs = set(elt[0] for elt in liste)
            nages = set(elt[1] for elt in liste)
            
            print("\nRésumé global:")
            print(f"Nombre total de nageurs: {len(nageurs)}")
            print(f"Nombre total de nages différentes: {len(nages)}")
            print("\nNageurs:", ", ".join(sorted(nageurs)))
            print("Nages:", ", ".join(sorted(nages)))
            
            # Meilleure performance globale
            meilleur_nageur, meilleure_nage, meilleure_perf = max(liste, key=lambda x: x[2])
            print(f"\nMeilleure performance: {meilleur_nageur} ({meilleure_nage}) - {meilleure_perf} longueurs")
        
        elif choix == "5":
            break
        
        else:
            print("Choix invalide. Veuillez réessayer.")

def cmd_performance(liste):
    """Gestion des performances"""
    print("\nGestion des performances:")
    print("1. Afficher les meilleures performances par nage")
    print("2. Afficher les meilleures performances par nageur")
    print("3. Afficher le record absolu")
    choix = input("Votre choix (1-3) ? ")
    
    if choix == "1":
        nages = set(elt[1] for elt in liste)
        print("\nMeilleures performances par nage:")
        print("Nage      | Nageur      | Longueur")
        print("----------------------------------")
        for nage in nages:
            performances_nage = [(elt[0], elt[2]) for elt in liste if elt[1] == nage]
            meilleur_nageur, meilleure_perf = max(performances_nage, key=lambda x: x[1])
            print(f" {nage:9}| {meilleur_nageur:11}| {meilleure_perf}")
    
    elif choix == "2":
        nageurs = set(elt[0] for elt in liste)
        print("\nMeilleures performances par nageur:")
        print("Nageur      | Nage      | Longueur")
        print("----------------------------------")
        for nageur in nageurs:
            performances_nageur = [(elt[1], elt[2]) for elt in liste if elt[0] == nageur]
            meilleure_nage, meilleure_perf = max(performances_nageur, key=lambda x: x[1])
            print(f" {nageur:11}| {meilleure_nage:9}| {meilleure_perf}")
    
    elif choix == "3":
        meilleur_nageur, meilleure_nage, meilleure_perf = max(liste, key=lambda x: x[2])
        print("\nRecord absolu:")
        print(f"Nageur: {meilleur_nageur}")
        print(f"Nage: {meilleure_nage}")
        print(f"Longueur: {meilleure_perf}")

def cmd_exit(liste):
    tmp = input("En êtes-vous sûr ? (o)ui/(n)on ")
    if tmp == 'o':
        cmd_save(liste, 'save.backup')
        return False
    else:
        return True

def cmd_save(liste, filename):
    '''sauvegarde la BDD'''
    fichier = open(filename, 'w')
    for elt in liste:
        fichier.write(elt[0]+','+elt[1]+','+str(elt[2])+"\n")
    fichier.close()

def cmd_load(liste, filename):
    'charge la BDD'
    fichier = open(filename, 'r')
    for line in fichier:
        line = line.strip()
        if line[-1] == '\n':
            line = line[:-1]
        if line[0]=='#':
            continue
        tmp = line.split(',')
        tmp[2] = int(tmp[2])
        liste.append(tuple(tmp))
    fichier.close()

def get_cmd():
    '''Traitement de la commande d'entrée'''
    print("\nCommandes disponibles:")
    print("- ajout: Ajouter une performance")
    print("- visualisation: Voir les performances")
    print("- performance: Voir les meilleures performances")
    print("- save: Sauvegarder les données")
    print("- load: Charger les données")
    print("- exit: Quitter le programme")
    
    msg = input("\nQue faut-il faire ? ")
    msg = msg.lower()
    return msg

isAlive = True
while isAlive:
    commande = get_cmd()
    if commande == 'ajout':
        cmd_ajout(liste)
    elif commande == 'visualisation':
        cmd_visualisation(liste)
    elif commande == 'performance':
        cmd_performance(liste)
    elif commande == 'save':
        cmd_save(liste, 'save.csv')
    elif commande == 'load':
        cmd_load(liste, 'save.csv')
    elif commande == 'exit':
        isAlive = cmd_exit(liste)
    else:
        print(f"Commande {commande} inconnue")



## PROCHAIN COMMIT AJOUT DEs gestions de dates



from datetime import datetime, date

# Modification de la structure des données pour inclure les dates
liste = [
    ("Pierre", "Dos", 10, "2024-05-10"),
    ("Paul", "Brasse", 13, "2024-05-10"),
    ("Léa", "Crawl", 6, "2024-05-11"),
    ("Léa", "Brasse", 8, "2024-05-13"),
    ("Musa", "Papillon", 15, "2024-05-13")
]
commande = ''

def valider_date(date_str):
    """Valide le format de la date"""
    try:
        return bool(datetime.strptime(date_str, '%Y-%m-%d'))
    except ValueError:
        return False

def saisir_date():
    """Demande et valide la saisie d'une date"""
    while True:
        date_str = input("Date (YYYY-MM-DD) ? ")
        if valider_date(date_str):
            return date_str
        print("Format de date invalide. Utilisez YYYY-MM-DD")

def cmd_ajout(liste):
    """Ajoute un évènement à la liste"""
    a = input("Qui nage ? ")
    b = input("Quelle nage ? ")
    c = int(input("Combien de longueur ? "))
    d = saisir_date()
    liste.append((a, b, c, d))

def cmd_liste(liste):
    """Affiche toutes les performances des nageurs"""
    print("\nToutes les performances:")
    print("Prénom      |  nage   |  longueur  |  date")
    print("--------------------------------------------")
    for elt in liste:
        print(f" {elt[0]:11}| {elt[1]:8}|  {elt[2]:9} | {elt[3]}")

def cmd_nageur(liste):
    """Affiche toutes les performances d'un nageur"""
    tmp = input("Quel nageur ? ")
    print("\nPerformances de", tmp)
    print("nage    | longueur | date")
    print("------------------------------------------------")
    for elt in liste:
        if elt[0] == tmp:
            print(f"{elt[1]:8} |  {elt[2]:8} | {elt[3]}")

def cmd_nage(liste):
    """Affiche toutes les performances suivant une nage donnée"""
    tmp = input("Quelle nage ? ")
    print("\nNage", tmp)
    print("Nageur     | longueur | date")
    print("------------------------------------------------")
    for elt in liste:
        if elt[1] == tmp:
            print(f"{elt[0]:11}|  {elt[2]:8} | {elt[3]}")

def cmd_date(liste):
    """Affiche toutes les performances pour une date donnée"""
    date_recherchee = saisir_date()
    print(f"\nPerformances du {date_recherchee}:")
    print("Nageur     | nage    | longueur")
    print("--------------------------------")
    performances_trouvees = False
    for elt in liste:
        if elt[3] == date_recherchee:
            print(f"{elt[0]:11}| {elt[1]:8}|  {elt[2]}")
            performances_trouvees = True
    if not performances_trouvees:
        print("Aucune performance enregistrée à cette date.")

def cmd_visualisation(liste):
    """Menu de visualisation des performances"""
    while True:
        print("\nMenu de visualisation:")
        print("1. Voir toutes les performances")
        print("2. Voir les performances d'un nageur")
        print("3. Voir tous les nageurs par type de nage")
        print("4. Voir les performances par date")
        print("5. Voir le résumé global")
        print("6. Retour au menu principal")
        
        choix = input("\nVotre choix (1-6) ? ")
        
        if choix == "1":
            cmd_liste(liste)
        elif choix == "2":
            nageurs = sorted(set(elt[0] for elt in liste))
            print("\nNageurs disponibles:", ", ".join(nageurs))
            cmd_nageur(liste)
        elif choix == "3":
            nages = sorted(set(elt[1] for elt in liste))
            print("\nNages disponibles:", ", ".join(nages))
            cmd_nage(liste)
        elif choix == "4":
            cmd_date(liste)
        elif choix == "5":
            # Résumé global
            nageurs = set(elt[0] for elt in liste)
            nages = set(elt[1] for elt in liste)
            dates = sorted(set(elt[3] for elt in liste))
            
            print("\nRésumé global:")
            print(f"Nombre total de nageurs: {len(nageurs)}")
            print(f"Nombre total de nages différentes: {len(nages)}")
            print(f"Période: du {dates[0]} au {dates[-1]}")
            print("\nNageurs:", ", ".join(sorted(nageurs)))
            print("Nages:", ", ".join(sorted(nages)))
            
            # Meilleure performance globale
            meilleur_nageur, meilleure_nage, meilleure_perf, date_perf = max(liste, key=lambda x: x[2])
            print(f"\nMeilleure performance: {meilleur_nageur} ({meilleure_nage}) - {meilleure_perf} longueurs")
            print(f"Date: {date_perf}")
        elif choix == "6":
            break
        else:
            print("Choix invalide. Veuillez réessayer.")

def cmd_save(liste, filename):
    '''sauvegarde la BDD'''
    fichier = open(filename, 'w')
    for elt in liste:
        fichier.write(f"{elt[0]},{elt[1]},{str(elt[2])},{elt[3]}\n")
    fichier.close()

def cmd_load(liste, filename):
    'charge la BDD'
    fichier = open(filename, 'r')
    for line in fichier:
        line = line.strip()
        if line[-1] == '\n':
            line = line[:-1]
        if line[0] == '#':
            continue
        tmp = line.split(',')
        tmp[2] = int(tmp[2])
        liste.append(tuple(tmp))
    fichier.close()

def cmd_exit(liste):
    tmp = input("En êtes-vous sûr ? (o)ui/(n)on ")
    if tmp == 'o':
        cmd_save(liste, 'save.backup')
        return False
    return True

def get_cmd():
    '''Traitement de la commande d'entrée'''
    print("\nCommandes disponibles:")
    print("- ajout: Ajouter une performance")
    print("- visualisation: Voir les performances")
    print("- save: Sauvegarder les données")
    print("- load: Charger les données")
    print("- exit: Quitter le programme")
    
    msg = input("\nQue faut-il faire ? ")
    msg = msg.lower()
    return msg

isAlive = True
while isAlive:
    commande = get_cmd()
    if commande == 'ajout':
        cmd_ajout(liste)
    elif commande == 'visualisation':
        cmd_visualisation(liste)
    elif commande == 'save':
        cmd_save(liste, 'save.csv')
    elif commande == 'load':
        cmd_load(liste, 'save.csv')
    elif commande == 'exit':
        isAlive = cmd_exit(liste)
    else:
        print(f"Commande {commande} inconnue")



## PROCHAIN COMMIT AJOUT DE GET VALUE 

from datetime import datetime, date

def get_int_value(message="Valeur ? "):
    """
    Fonction qui vérifie que la saisie est bien un nombre entier
    """
    while True:
        try:
            msg = int(input(message))
            return msg
        except:
            print("Indiquez bien une valeur numérique")

# Modification de la structure des données pour inclure les dates
liste = [
    ("Pierre", "Dos", 10, "2024-05-10"),
    ("Paul", "Brasse", 13, "2024-05-10"),
    ("Léa", "Crawl", 6, "2024-05-11"),
    ("Léa", "Brasse", 8, "2024-05-13"),
    ("Musa", "Papillon", 15, "2024-05-13")
]
commande = ''

def valider_date(date_str):
    """Valide le format de la date"""
    try:
        return bool(datetime.strptime(date_str, '%Y-%m-%d'))
    except ValueError:
        return False

def saisir_date():
    """Demande et valide la saisie d'une date"""
    while True:
        date_str = input("Date (YYYY-MM-DD) ? ")
        if valider_date(date_str):
            return date_str
        print("Format de date invalide. Utilisez YYYY-MM-DD")

def cmd_ajout(liste):
    """Ajoute un évènement à la liste"""
    a = input("Qui nage ? ")
    b = input("Quelle nage ? ")
    c = get_int_value("Combien de longueur ? ")  # Utilisation de get_int_value ici
    d = saisir_date()
    liste.append((a, b, c, d))

def cmd_liste(liste):
    """Affiche toutes les performances des nageurs"""
    print("\nToutes les performances:")
    print("Prénom      |  nage   |  longueur  |  date")
    print("--------------------------------------------")
    for elt in liste:
        print(f" {elt[0]:11}| {elt[1]:8}|  {elt[2]:9} | {elt[3]}")

def cmd_nageur(liste):
    """Affiche toutes les performances d'un nageur"""
    tmp = input("Quel nageur ? ")
    print("\nPerformances de", tmp)
    print("nage    | longueur | date")
    print("------------------------------------------------")
    for elt in liste:
        if elt[0] == tmp:
            print(f"{elt[1]:8} |  {elt[2]:8} | {elt[3]}")

def cmd_nage(liste):
    """Affiche toutes les performances suivant une nage donnée"""
    tmp = input("Quelle nage ? ")
    print("\nNage", tmp)
    print("Nageur     | longueur | date")
    print("------------------------------------------------")
    for elt in liste:
        if elt[1] == tmp:
            print(f"{elt[0]:11}|  {elt[2]:8} | {elt[3]}")

def cmd_date(liste):
    """Affiche toutes les performances pour une date donnée"""
    date_recherchee = saisir_date()
    print(f"\nPerformances du {date_recherchee}:")
    print("Nageur     | nage    | longueur")
    print("--------------------------------")
    performances_trouvees = False
    for elt in liste:
        if elt[3] == date_recherchee:
            print(f"{elt[0]:11}| {elt[1]:8}|  {elt[2]}")
            performances_trouvees = True
    if not performances_trouvees:
        print("Aucune performance enregistrée à cette date.")

def cmd_visualisation(liste):
    """Menu de visualisation des performances"""
    while True:
        print("\nMenu de visualisation:")
        print("1. Voir toutes les performances")
        print("2. Voir les performances d'un nageur")
        print("3. Voir tous les nageurs par type de nage")
        print("4. Voir les performances par date")
        print("5. Voir le résumé global")
        print("6. Retour au menu principal")
       
        choix = input("\nVotre choix (1-6) ? ")
       
        if choix == "1":
            cmd_liste(liste)
        elif choix == "2":
            nageurs = sorted(set(elt[0] for elt in liste))
            print("\nNageurs disponibles:", ", ".join(nageurs))
            cmd_nageur(liste)
        elif choix == "3":
            nages = sorted(set(elt[1] for elt in liste))
            print("\nNages disponibles:", ", ".join(nages))
            cmd_nage(liste)
        elif choix == "4":
            cmd_date(liste)
        elif choix == "5":
            # Résumé global
            nageurs = set(elt[0] for elt in liste)
            nages = set(elt[1] for elt in liste)
            dates = sorted(set(elt[3] for elt in liste))
           
            print("\nRésumé global:")
            print(f"Nombre total de nageurs: {len(nageurs)}")
            print(f"Nombre total de nages différentes: {len(nages)}")
            print(f"Période: du {dates[0]} au {dates[-1]}")
            print("\nNageurs:", ", ".join(sorted(nageurs)))
            print("Nages:", ", ".join(sorted(nages)))
           
            # Meilleure performance globale
            meilleur_nageur, meilleure_nage, meilleure_perf, date_perf = max(liste, key=lambda x: x[2])
            print(f"\nMeilleure performance: {meilleur_nageur} ({meilleure_nage}) - {meilleure_perf} longueurs")
            print(f"Date: {date_perf}")
        elif choix == "6":
            break
        else:
            print("Choix invalide. Veuillez réessayer.")

def cmd_save(liste, filename):
    '''sauvegarde la BDD'''
    fichier = open(filename, 'w')
    for elt in liste:
        fichier.write(f"{elt[0]},{elt[1]},{str(elt[2])},{elt[3]}\n")
    fichier.close()

def cmd_load(liste, filename):
    'charge la BDD'
    fichier = open(filename, 'r')
    for line in fichier:
        line = line.strip()
        if line[-1] == '\n':
            line = line[:-1]
        if line[0] == '#':
            continue
        tmp = line.split(',')
        tmp[2] = int(tmp[2])
        liste.append(tuple(tmp))
    fichier.close()

def cmd_exit(liste):
    tmp = input("En êtes-vous sûr ? (o)ui/(n)on ")
    if tmp == 'o':
        cmd_save(liste, 'save.backup')
        return False
    return True

def get_cmd():
    '''Traitement de la commande d'entrée'''
    print("\nCommandes disponibles:")
    print("- ajout: Ajouter une performance")
    print("- visualisation: Voir les performances")
    print("- save: Sauvegarder les données")
    print("- load: Charger les données")
    print("- exit: Quitter le programme")
   
    msg = input("\nQue faut-il faire ? ")
    msg = msg.lower()
    return msg

isAlive = True
while isAlive:
    commande = get_cmd()
    if commande == 'ajout':
        cmd_ajout(liste)
    elif commande == 'visualisation':
        cmd_visualisation(liste)
    elif commande == 'save':
        cmd_save(liste, 'save.csv')
    elif commande == 'load':
        cmd_load(liste, 'save.csv')
    elif commande == 'exit':
        isAlive = cmd_exit(liste)
    else:
        print(f"Commande {commande} inconnue")



## PROCHAIN COMMIT FORMATAGE CORRIGE

from datetime import datetime, date

def get_int_value(message="Valeur ? "):
    """
    Fonction qui vérifie que la saisie est bien un nombre entier
    """
    while True:
        try:
            msg = int(input(message))
            return msg
        except:
            print("Indiquez bien une valeur numérique")

# Modification de la structure des données pour inclure les dates
liste = [
    ("Pierre", "Dos", 10, "2024-05-10"),
    ("Paul", "Brasse", 13, "2024-05-10"),
    ("Léa", "Crawl", 6, "2024-05-11"),
    ("Léa", "Brasse", 8, "2024-05-13"),
    ("Musa", "Papillon", 15, "2024-05-13")
]
commande = ''

def valider_date(date_str):
    """Valide le format de la date"""
    try:
        return bool(datetime.strptime(date_str, '%Y-%m-%d'))
    except ValueError:
        return False

def saisir_date():
    """Demande et valide la saisie d'une date"""
    while True:
        date_str = input("Date (YYYY-MM-DD) ? ")
        if valider_date(date_str):
            return date_str
        print("Format de date invalide. Utilisez YYYY-MM-DD")

def cmd_ajout(liste):
    """Ajoute un évènement à la liste"""
    a = input("Qui nage ? ")
    b = input("Quelle nage ? ")
    c = get_int_value("Combien de longueur ? ")  # Utilisation de get_int_value ici
    d = saisir_date()
    liste.append((a, b, c, d))

def cmd_liste(liste):
    """Affiche toutes les performances des nageurs"""
    print("\nToutes les performances:")
    print("Prénom      |  nage   |  longueur  |  date")
    print("--------------------------------------------")
    for elt in liste:
        print(f" {elt[0]:11}| {elt[1]:8}|  {elt[2]:9} | {elt[3]}")

def cmd_nageur(liste):
    """Affiche toutes les performances d'un nageur avec statistiques"""
    tmp = input("Quel numéro de nageur ? ")
    print("\nPerformances")
    print(f"de {tmp}")
    print("\nnage | longueur")
    print("--------------------")
   
    # Liste pour stocker les performances du nageur
    performances = []
   
    # Affichage des performances et collecte des données
    for elt in liste:
        if elt[0] == tmp:
            print(f"{elt[1]}")
            print(f"| {elt[2]}")
            performances.append(elt[2])
   
    # Calcul et affichage des statistiques si des performances existent
    if performances:
        max_perf = max(performances)
        min_perf = min(performances)
        moy_perf = sum(performances) / len(performances)
       
        print("\nMinimum")
        print(f": {min_perf}")
        print("\nMaximum")
        print(f": {max_perf}")
        print("\nMoyenne")
        print(f": {moy_perf:.1f}")
    else:
        print(f"\nAucune performance enregistrée pour {tmp}")

def cmd_nage(liste):
    """Affiche toutes les performances suivant une nage donnée"""
    tmp = input("Quelle nage ? ")
    print("\nNage", tmp)
    print("Nageur     | longueur | date")
    print("------------------------------------------------")
    for elt in liste:
        if elt[1] == tmp:
            print(f"{elt[0]:11}|  {elt[2]:8} | {elt[3]}")

def cmd_date(liste):
    """Affiche toutes les performances pour une date donnée"""
    date_recherchee = saisir_date()
    print(f"\nPerformances du {date_recherchee}:")
    print("Nageur     | nage    | longueur")
    print("--------------------------------")
    performances_trouvees = False
    for elt in liste:
        if elt[3] == date_recherchee:
            print(f"{elt[0]:11}| {elt[1]:8}|  {elt[2]}")
            performances_trouvees = True
    if not performances_trouvees:
        print("Aucune performance enregistrée à cette date.")

def cmd_visualisation(liste):
    """Menu de visualisation des performances"""
    while True:
        print("\nMenu de visualisation:")
        print("1. Voir toutes les performances")
        print("2. Voir les performances d'un nageur")
        print("3. Voir tous les nageurs par type de nage")
        print("4. Voir les performances par date")
        print("5. Voir le résumé global")
        print("6. Retour au menu principal")
       
        choix = input("\nVotre choix (1-6) ? ")
       
        if choix == "1":
            cmd_liste(liste)
        elif choix == "2":
            nageurs = sorted(set(elt[0] for elt in liste))
            print("\nNageurs disponibles:", ", ".join(nageurs))
            cmd_nageur(liste)
        elif choix == "3":
            nages = sorted(set(elt[1] for elt in liste))
            print("\nNages disponibles:", ", ".join(nages))
            cmd_nage(liste)
        elif choix == "4":
            cmd_date(liste)
        elif choix == "5":
            # Résumé global
            nageurs = set(elt[0] for elt in liste)
            nages = set(elt[1] for elt in liste)
            dates = sorted(set(elt[3] for elt in liste))
           
            print("\nRésumé global:")
            print(f"Nombre total de nageurs: {len(nageurs)}")
            print(f"Nombre total de nages différentes: {len(nages)}")
            print(f"Période: du {dates[0]} au {dates[-1]}")
            print("\nNageurs:", ", ".join(sorted(nageurs)))
            print("Nages:", ", ".join(sorted(nages)))
           
            # Meilleure performance globale
            meilleur_nageur, meilleure_nage, meilleure_perf, date_perf = max(liste, key=lambda x: x[2])
            print(f"\nMeilleure performance: {meilleur_nageur} ({meilleure_nage}) - {meilleure_perf} longueurs")
            print(f"Date: {date_perf}")
        elif choix == "6":
            break
        else:
            print("Choix invalide. Veuillez réessayer.")

def cmd_save(liste, filename):
    '''sauvegarde la BDD'''
    fichier = open(filename, 'w')
    for elt in liste:
        fichier.write(f"{elt[0]},{elt[1]},{str(elt[2])},{elt[3]}\n")
    fichier.close()

def cmd_load(liste, filename):
    'charge la BDD'
    fichier = open(filename, 'r')
    for line in fichier:
        line = line.strip()
        if line[-1] == '\n':
            line = line[:-1]
        if line[0] == '#':
            continue
        tmp = line.split(',')
        tmp[2] = int(tmp[2])
        liste.append(tuple(tmp))
    fichier.close()

def cmd_exit(liste):
    tmp = input("En êtes-vous sûr ? (o)ui/(n)on ")
    if tmp == 'o':
        cmd_save(liste, 'save.backup')
        return False
    return True

def get_cmd():
    '''Traitement de la commande d'entrée'''
    print("\nCommandes disponibles:")
    print("- ajout: Ajouter une performance")
    print("- visualisation: Voir les performances")
    print("- save: Sauvegarder les données")
    print("- load: Charger les données")
    print("- exit: Quitter le programme")
   
    msg = input("\nQue faut-il faire ? ")
    msg = msg.lower()
    return msg

isAlive = True
while isAlive:
    commande = get_cmd()
    if commande == 'ajout':
        cmd_ajout(liste)
    elif commande == 'visualisation':
        cmd_visualisation(liste)
    elif commande == 'save':
        cmd_save(liste, 'save.csv')
    elif commande == 'load':
        cmd_load(liste, 'save.csv')
    elif commande == 'exit':
        isAlive = cmd_exit(liste)
    else:
        print(f"Commande {commande} inconnue")
