liste = [("Pierre","Dos",10),("Paul","Brasse",13),("Léa","Crawl",6), ("Léa","Brasse",8)]
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