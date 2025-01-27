# Exo 1
mot = "blablabla"

nbr = 0

for elt in mot: 
    print(elt)  

    if "a" == elt:  
        nbr += 1

print("Nombre de 'a' :", nbr)

#Exo 2 


notes_et_coefficients = [(15, 2), (9, 1), (12, 3)]

somme_notes = 0
somme_coefficients = 0

for note, coefficient in notes_et_coefficients:
    somme_notes += note * coefficient
    somme_coefficients += coefficient

moyenne = somme_notes / somme_coefficients

print(f"La moyenne pondérée est : {moyenne}")

#EXO 3

tab = [0, 1, 4, 2, -2, 9, 3, 1, 7,1]

petit = min(tab)
grand = max(tab)

print(f"Le plus petit chiffre est : {petit}")
print(f"Le plus grand chiffre est : {grand}")

#EXO 4 
T=(1,2,3,4,5,6,7,8,9,10) 
def conv_bin(n): 

#EXO 6

6 eleves_notes = [ ("Musa", 12, 15, 14), ("Nizam", 10, 8, 9), ("Yasin", 16, 17, 18) ] 
def calculer_moyenne_par_eleve(eleves_notes): 
    moyennes = [] 
for eleve in eleves_notes: 
    nom = eleve[0] 
    notes = eleve[1:] moyenne = sum(notes) / len(notes) 
    moyennes.append((nom, moyenne)) return moyennes 
    moyennes = calculer_moyenne_par_eleve(eleves_notes) for eleve, moyenne in moyennes: 
    print(f"L'élève {eleve} a une moyenne de {moyenne}") 
    
#EXO 7 
compteur=0 
tab=(1,8,9,8,7,1,1,8,9,9) 
nb_repetition=(1) 
for elt in tab: 
    if elt==lettre: