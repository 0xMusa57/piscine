import random 
#générer un nombre alétoire en 0 et 100
nombre_aleatoire = random.randint(0,100)
tentative = 0
nbr = 0
while nombre_aleatoire != nbr:
    nbr = int(input("donne moi un nombre aléatoire en 0 et 100"))
    tentative = tentative +1
    if nbr > nombre_aleatoire: 
        print("-") 
    elif nbr < nombre_aleatoire:
        print("+")
    else:
        print(f"gagné, il vous a fallu {tentative} coups")
