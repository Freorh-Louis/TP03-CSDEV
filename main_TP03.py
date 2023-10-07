"""
Hugo PRIGENT, Louis VINCENT
05/10/2023
main du TP03
"""

import random
import fonction_TP03

fichier = open("dictionnaire.txt","r")
line = fichier.readlines()


play = True
while play:
    fonction_TP03.mot, fonction_TP03.mot_afficher = fonction_TP03.init(line)
    print(fonction_TP03.jeu_console())
    again = input("Play again ? (yes or no) : ")
    if again == "no":
        play = False
        fichier.close()
    

