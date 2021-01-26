#!/bin/bash

#sudo apt-get remove git code // permet de supprimer git et vscode si par exemple ce ne sont pas les versions que je veux
echo "UBUNTU POST-INSTALL SCRIPT" > log.txt

#################### Mise à jour de apt et apt-get #################################
# ce sont des gestionnaire de package###############################################
echo "mise a jour de apt et apt-get" >> log.txt
sudo apt update && sudo apt upgrade 
sudo apt-get update && sudo apt-get upgrade
####################################################################################

echo "Installation de git curl et python" >> log.txt

############" Installation de Curl, et des dépendances essentielles pour git et python" ###############
sudo apt-get install --yes git git-extras build-essential python3-pip htop glances git python3.6 curl
#######################################################################################################

echo "Ajout de la clé PGP et du PPA d microsoft" >> log.txt

##################### Ajout de la clé PGP de microsoft pour etre sur de bien installé leur version de VSCODE ################
# Avec curl qui est un autre gestionnaire de paquet ########################################
curl https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor > packages.microsoft.gpg
sudo install -o root -g root -m 644 packages.microsoft.gpg /usr/share/keyrings/
sudo sh -c 'echo "deb [arch=amd64 signed-by=/usr/share/keyrings/packages.microsoft.gpg] https://packages.microsoft.com/repos/vscode stable main" > /etc/apt/sources.list.d/vscode.list'
######################################################################################################################################

echo "instalation de vscode" >> log.txt
##################### Installation de VSCode ###################
sudo apt-get install apt-transport-https
sudo apt-get update
sudo apt-get install code
############################################################

###########on a fini###################################
echo "tout est carrer" >> log.txt
#######################################################