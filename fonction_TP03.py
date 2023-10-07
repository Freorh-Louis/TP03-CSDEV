""""
Hugo PRIGENT, Louis VINCENT
05/10/2023
Fonction pour le TP03
"""

import random
import tkinter


# Fonction initialisant un mot et une version affichable de ce mot à partir d'un fichier texte 
# entrée : line est la liste des lignes d'un fichier
# sortie : mot (str)(mot de référence), mot_afficher (list)(liste des lettres du mot traiter affichable)
def init(line):
    n = random.randint(1,len(line))
    mot = line[n][:-2]
    mot_afficher = []
    for e in mot:
        if e == mot[0]:
            mot_afficher.append(mot[0])
        else:
            mot_afficher.append("_")
    return(mot,mot_afficher)


# affiche un mot dans la console et demande une lettre au joueur
# entrée : mot_affichable (str) (mot à afficher)
# sortie : lettre (str) (lettre donner par le joueur)
def console(mot_afficher,L):
    print(mot_afficher,"        ",L)
    lettre = input("Entrée une lettre : ").upper()
    return(lettre)


# Transforme mes mots format liste en format string
# entrée : mot (list)
# sortie : mot_str (str)
def string(mot):
    mot_str = ""
    for e in mot:
        mot_str = mot_str + e
    return(mot_str)


lettre = ""
mot = ""
mot_afficher = []
mot_afficher_str = ""
L = []
n = 0


# Fonction testant si une lettre est dans notre mot
# entrée : lettre (str), mot(str), mot_afficher(list), L(list)(lettres utilisés), n(int)(numéro de l'essaie)
# sortie : mot_afficher(list), mot_afficher_str (str)
def test():
    global lettre, mot, mot_afficher , L, n, mot_afficher_str
    if lettre in L:
        print("Lettre deja donnée, rentré une autre lettre")
    elif lettre in mot:
        for i,e in enumerate(mot):
            if e == lettre:
                mot_afficher[i] = lettre
        L.append(lettre)
    elif lettre not in mot:
        n += 1
        L.append(lettre)
    mot_afficher_str = string(mot_afficher)
    return(mot_afficher, mot_afficher_str, n)


# Fonction lançant le jeu du pendu
# entrée : mot (str) (mot de référence), mot_afficher (list) (liste des lettres du mot affichable)
# sortie : victoire ou défaite
def jeu_console():
    global lettre,mot,mot_afficher,L,n,mot_afficher_str
    n = 0
    L = [mot[0]]
    mot_afficher_str = string(mot_afficher)
    while n < 8:
        lettre = console(mot_afficher_str,L)
        mot_afficher, mot_afficher_str, n = test()
        if mot == mot_afficher_str:
            return("Victory")
    return("Defeat, the word was",mot)


window = tkinter.Tk()

canevas = tkinter.Canvas(window, width = 300, height = 300, bg = "gray")
canevas_txt = tkinter.Canvas(window, width = 300, height = 200)

entry = tkinter.Entry(window, textvariable = lettre)

lettre_joué = canevas_txt.create_text(10,70, text = str(L))
affichage_mot = canevas_txt.create_text(10, 40, text = mot_afficher_str)
coup_restant = canevas_txt.create_text(10, 10, text = str(8 - n))
victory = tkinter.Label(window, text = "Victory !")
defeat = tkinter.Label(window,text = "Defeat...")
    
button_proposer = tkinter.Button(window, text = "Proposer", command = test)



def guess():
    global window, lettre, mot, mot_afficher , L, n, mot_afficher_str, lettre_joué, coup_restant, affichage_mot, victory, defeat
    canevas_txt.delete(lettre_joué, coup_restant, affichage_mot)
    if mot_afficher == mot_afficher_str:
        victory.pack()
    if n < 8:
        test()
        




def jeu_graphique():
    global lettre,mot,mot_afficher,L,n,mot_afficher_str
    n = 0
    L = [mot[0]]
    mot_afficher_str = string(mot_afficher)
    window = tkinter.Tk()

    canevas = tkinter.Canvas(window, width = 300, height = 300, bg = "gray")

    entry = tkinter.Entry(window, textvariable = lettre)

    lettre_joué = tkinter.Label(window, text = L)
    affichage_mot = tkinter.Label(window, text = mot_afficher_str)
    coup_restant = tkinter.Label(window, text = 8 - n)
    
    button_proposer = tkinter.Button(window, text = "Proposer", command = test)
