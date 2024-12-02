# Liste initiale des nageurs avec leur type de nage et le nombre de longueurs
liste = [("Pierre","Dos",10),("Paul","Brasse",13),("Léa","Crawl",6), ("Léa","Brasse",8) ]
commande = ''  # Variable pour stocker la commande de l'utilisateur

# Chargement des données depuis le fichier CSV
def load(liste, filaname):
    fichier = open('save.csv', 'r')  # Ouvre le fichier en mode lecture
    for line in fichier:
        line = line.strip()  # Supprime les espaces ou sauts de ligne en début/fin de ligne
        if line[0] == '#':  # Ignore les lignes de commentaire commençant par '#'
            continue
        tmp = line.split(',')  # Divise la ligne en plusieurs parties séparées par des virgules
        liste.append(tuple(tmp))  # Ajoute chaque ligne comme un tuple dans la liste
    fichier.close()  # Ferme le fichier après lecture

""" Création de toutes les fonctions pour effectuer des actions sur la liste """

def sauvegarder(liste,):
    """Sauvegarde les données dans un fichier CSV"""
    # Ouvre le fichier en mode écriture et sauvegarde chaque nageur sous forme de texte
    with open('save.csv', 'w') as fichier:
        for elt in liste:
            # Ecrit chaque tuple dans une ligne du fichier CSV, séparée par des virgules
            fichier.write(elt[0]+','+elt[1]+','+str(elt[2])+"\n")

def cmd_exit():
    """Commande pour quitter le programme"""
    tmp = input("en êtes-vous sûr ? (o)ui/(n)on")  # Confirme la sortie avec l'utilisateur
    if tmp == "o":
        sauvegarder(liste)  # Sauvegarde les données avant de quitter
        return False  # Change l'état de la boucle pour arrêter le programme
    else:
        return True  # Continue l'exécution du programme

def cmd_ajout(liste):
    """Commande pour ajouter un nageur à la liste"""
    # Demande les informations du nageur : nom, type de nage, et nombre de longueurs
    a = input("Qui nage ? ")
    b = input("quelle nage ? ")
    c = input("combien de longueur ? ")
    liste.append((a, b, c))  # Ajoute les informations comme un tuple dans la liste

def cmd_liste(liste):
    """Affichage de la liste entière de tous les nageurs enregistrés"""
    print("Prénom    -  nage  -  longueur")  # En-tête de tableau
    print("------------------------------")  # Ligne de séparation
    for elt in liste:
        # Affiche chaque nageur avec une mise en forme propre
        print(f" {elt[0]:7} / {elt[1]:7} / {elt[2]}")

def cmd_nageur(liste):
    """Affiche toutes les performances d'un nageur donné"""
    nom_nageur = input("Qui ?")  # Demande le nom du nageur à rechercher
    print("performances de", nom_nageur)  # Titre de l'affichage
    print("  nage  -  longueur")
    print("-----------------")  # Ligne de séparation
    for elt in liste:
        if elt[0] == nom_nageur:  # Filtre les entrées correspondant au nageur donné
            print(f"{elt[1]:8}-  {elt[2]}")  # Affiche la nage et la longueur

def cmd_nage(liste):
    """Affiche toutes les performances selon un type de nage donné"""
    nom_nage = input("Quel nage ?")  # Demande le type de nage à rechercher
    print("nage", nom_nage)  # Titre de l'affichage
    print("  nageur -  longueur")
    print("-----------------")  # Ligne de séparation
    for elt in liste:
        if elt[1] == nom_nage:  # Filtre les entrées correspondant à la nage donnée
            print(f"{elt[0]:8}-  {elt[2]}")  # Affiche le nageur et la longueur

""" Exécution de toutes les fonctions créées auparavant """
isAlive = True  # Variable de contrôle pour exécuter la boucle principale
while isAlive: 
    commande = input("Que faut-il faire ? ")  # Demande à l'utilisateur une commande
    if commande == 'ajout':
        cmd_ajout(liste)  # Ajoute un nageur
        continue

    if commande == 'liste':
        cmd_liste(liste)  # Affiche tous les nageurs
        continue

    if commande == 'save':
        sauvegarder(liste) # Permet de sauvegarder la liste.
        continue
    
    if commande == 'load': # Permet de charger les données de la bdd
        load(liste)
        continue

    if commande == 'nageur':
        cmd_nageur(liste)  # Affiche les performances d'un nageur donné
        continue 

    if commande == 'exit':
        isAlive = cmd_exit()  # Gère la sortie du programme
        continue 

    if commande == 'nage':
        cmd_nage(liste)  # Affiche les performances d'une nage spécifique
        continue
    
    # Message d'erreur pour les commandes inconnues
    print(f"Command {commande} inconnue")

