#!/bin/bash

#sudo apt-get remove git code python3.8
echo "UBUNTU POST-INSTALL SCRIPT" > log.txt

echo "mise a jour de apt et apt-get" >> log.txt
sudo apt update && sudo apt upgrade 
sudo apt-get update && sudo apt-get upgrade

echo "Installation de git curl et python" >> log.txt

sudo apt-get install --yes git git-extras build-essential python3-pip htop glances git python3.6 curl

echo "Ajout de la clé PGP et du PPA d microsoft" >> log.txt

curl https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor > packages.microsoft.gpg

echo "instalation de vscode" >> log.txt

sudo apt-get install apt-transport-https
sudo apt-get update
sudo apt-get install code

echo "tout est carrer" >> log.txt
