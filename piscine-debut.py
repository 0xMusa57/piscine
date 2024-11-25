liste = [("Pierre","Dos",10),("Paul","Brasse",13),("Léa","Crawl",6), ("Léa","Brasse",8) ]
commande = ''

def cmd_exit():
    tmp = input("en êtes-vous sur ? (o)ui/(n)on")
    if tmp == "o":
         return False
    else:
         return True

def cmd_ajout(liste):
        a = input("Qui nage ? ")
        b = input("quelle nage ? ")
        c = input("combien de longueur ? ")
        liste.append((a,b,c))
    
def cmd_liste(liste):
    print("Prénom    -  nage  -  longueur")
    print("------------------------------")
    for elt in liste:
        print(f" {elt[0]:7} / {elt[1]:7} / {elt[2]}")

def cmd_nageur(liste):
     nom_nageur = input("Qui ?")
     print("performances de", nom_nageur)
     print("  nage  -  longueur")
     print("-----------------")
     for elt in liste:
        if elt[0] == nom_nageur:
             print(f"{elt[1]:8}-  {elt[2]}")
          
     
     
          
    
            

isAlive = True 
while isAlive: 
    commande = input("Que faut-il faire ? ")
    if commande == 'ajout':
        cmd_ajout(liste)
        continue

    if commande == 'liste':
        cmd_liste(liste)
        continue
    
    if commande == 'nageur':
         cmd_nageur(liste)
         continue 

    if commande =='exit':
        isAlive = cmd_exit()
        continue 

    print (f"Command {commande} inconnue")
