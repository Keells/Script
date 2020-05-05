#!/usr/bin/env bash
##################################################
##                                              ##
##          Louise Adonel                       ##
##          Avril 2020                          ##
##                                              ##
##################################################
# set -x

echo "Début du script d'installation"

if [[ -f "/etc/debian_version" ]]; then
  echo "C'est un linux dérivé de débian"
  echo "Lance le script d'installation spéciale débian"
  sudo apt -qq install python3 -y
  python3 deb_installation.py
elif cat /etc/os-release |grep REDHAT; then
  echo "C'est un linux dérivé de redhat"
  echo "Lance le script d'installation spéciale redhat edition"
  sudo yum -qq install python3 -y
  python3 red_installation.py
else
  echo "Ce n'est pas reconnu"
fi

echo "Fin du script d'installation"
