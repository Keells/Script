#!/bin/python
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

def maj():
    # Cette métode met à jour la liste des paquets entière
    print("*******************************************************")
    print("Mise à jour en cours")
    update = os.system('sudo yum -qq update -y')
    print("*******************************************************")
    if update == 0:
        logging.info("La mise à jour a était faite")
    else:
        logging.error("Il y a eu une erreur lors de la mise à jour")

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
            os.system('sudo rpm -i '+ progInstall+'.rpm')
            print("******************* \n Le mot a était trouvé dans la liste \n Le programme "+ progInstall +" est installé \n******************* \n")
            logging.info("Le paquet " + progInstall +" est installé")
        else:
            print("******************* \n Le mot n'a pas était trouvé dans la liste \n Le programme " + progInstall + " n'est donc pas installé \n********************")
            logging.info("Le paquet " + progInstall +" n'est pas installé")

def check():
    test = True
    check_files()
    installable = os.system("sudo yum list --all |grep '^"+progInstall+"'")
    if installable == 256:
        logging.error("Le paquet "+ progInstall +" n'existe pas, ou ne porte pas exactement ce nom")
    if installable == 0:
        os.system("sudo yum -qq install "+progInstall+" -y")
        print("Installation en cours")
        logging.info("Le programme "+progInstall+" est installé")
    elif test == True:
        listCheck()
    else:
        print("Le paquet n'est pas trouvable ou le fichier list_check n'existe pas")

logging.info('Démarrage')

maj()

boucle = True
while boucle == True:
    progInstall = str(input("Rentrer le nom du logiciel à installer :"))
    check()
    continuer = input("Voulez vous continuer ? (O/N) :")
    if continuer not in ('O','o','oui','OUI','ok'):
        boucle = False
        logging.info("Sorti de la boucle")

maj()

logging.info('Fini')
