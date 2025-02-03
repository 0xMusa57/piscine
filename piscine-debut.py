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
    ("Léa", "Crawl", 6, "2024-02-11"),
    ("Léa", "Brasse", 8, "2024-06-13"),
    ("Musa", "Papillon", 15, "2024-06-13")
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
    '''Sauvegarde la BDD'''
    try:
        with open(filename, 'w', encoding='utf-8') as fichier:
            for elt in liste:
                fichier.write(f"{elt[0]},{elt[1]},{elt[2]},{elt[3]}\n")
        print(f"✅ Données sauvegardées dans {filename}")
    except Exception as e:
        print(f"❌ Erreur lors de la sauvegarde : {e}")

def cmd_load(liste, filename):
    '''Charge la BDD'''
    try:
        with open(filename, 'r', encoding='utf-8') as fichier:
            liste.clear()  # Efface l'ancienne liste pour éviter les doublons
            for line in fichier:
                line = line.strip()
                if not line or line.startswith('#'):
                    continue  # Ignore les lignes vides et les commentaires
                
                tmp = line.split(',')
                if len(tmp) != 4:
                    print(f"⚠️ Ligne mal formatée ignorée: {line}")
                    continue
                
                try:
                    tmp[2] = int(tmp[2])  # Conversion en entier
                    liste.append(tuple(tmp))
                except ValueError:
                    print(f"⚠️ Erreur de conversion ignorée: {line}")
        
        print(f"✅ Données chargées depuis {filename}")
    except FileNotFoundError:
        print(f"❌ Fichier {filename} introuvable.")
    except Exception as e:
        print(f"❌ Erreur lors du chargement : {e}")

def cmd_exit(liste):
    tmp = input("En êtes-vous sûr ? (o)ui/(n)on ")
    if tmp == 'o':
        cmd_save(liste, 'savebackup.csv')
        return False
    return True

def get_cmd():
    '''Traitement de la commande d'entrée'''
    print("\nCommandes disponibles:")
    print("1 - Ajouter une performance")
    print("2 - Voir les performances")
    print("3 - Sauvegarder les données")
    print("4 - Charger les données")
    print("5 - Quitter le programme")
   
    msg = input("\nQue faut-il faire ? ")
    msg = msg.lower()
    return msg

isAlive = True
while isAlive:
    commande = get_cmd()
    if commande == '1':
        cmd_ajout(liste)
    elif commande == '2':
        cmd_visualisation(liste)
    elif commande == '3':
        cmd_save(liste, 'save.csv')
    elif commande == '4':
        cmd_load(liste, 'save.csv')
    elif commande == '5':
        isAlive = cmd_exit(liste)
    else:
        print(f"Commande {commande} inconnue")
