##################################################
##                                              ##
##          Louise Adonel                       ##
##          Avril 2020                          ##
##                                              ##
##################################################
#-*- coding: utf-8 -*-
import re, os, logging, sys
from os import path

logging.basicConfig(filename='Installation_base.log', level=logging.INFO)

def debut():
    # Cette métode met à jour la liste des paquets entière
    print("*******************************************************")
    update = os.system('Get-WindowsUpdate')
    print("*******************************************************")
    if update == 0:
        logging.info("La liste des paquets à était mise à jour")
    else:
        logging.error("Il y a eu une erreur lors de la mise à jour de la liste des paquets")

def fin():
    # Cette méthode met à jour les paquets installés
    print("*******************************************************")
    upgrade = os.system('Install-WindowsUpdate')
    print("*******************************************************")
    if upgrade == 0:
        logging.info("La liste des paquets installés est mise à jour")
    else:
        logging.error("Il y a eu une erreur lors de la mise à jour des paquets installés")

def check_files():
# Cette méthode va vérifier que le fichier avec tout les binaires à installer
# et bien présent
    if path.exists("list_check.txt") == True:
        logging.info("Le fichier list_check existe")
        test = True
    else:
        logging.warning("Le fichier list_check n'existe pas")
        test = False

def listCheck():
# Cette méthode vérifie que l'entrée est bien dans la liste de binaire
    with open('list_check.txt') as file:
        contents = file.read()
        if progInstall in contents:
            os.system('sudo dpkg -i '+ progInstall+'.deb')
            print("******************* \n Le mot a était trouvé dans la liste \n Le programme "+ progInstall +" est installé \n******************* \n")
            logging.info("Le paquet " + progInstall +" est installé")
        else:
            print("******************* \n Le mot n'a pas était trouvé dans la liste \n Le programme " + progInstall + " n'est donc pas installé \n********************")
            logging.info("Le paquet " + progInstall +" n'est pas installé")

def check():
    test = True
    check_files()
    installable = os.system("choco search --by-id-only "+progInstall+"")
    if installable == 256:
        logging.error("Le paquet "+ progInstall +" n'existe pas, ou ne porte pas exactement ce nom")
    if installable == 0:
        print("j'aurais bien installer"+progInstall)
        logging.info("Le programme "+progInstall+" est installé")
    elif test == True:
    #    listCheck()
    else:
        print("Le paquet n'est pas trouvable ou le fichier list_check n'existe pas")

logging.info('Démarrage')

debut()

boucle = True
while boucle == True:
    progInstall = str(input("Rentrer le nom du logiciel à installer :"))
    check()
    continuer = input("Voulez vous continuer ? (O/N) :")
    if continuer not in ('O','o','oui','OUI','ok'):
        boucle = False
        logging.info("Sorti de la boucle")

fin()

logging.info('Fini')
