import os

def fairecommandeenbash(commande):
    os.system(commande)

fairecommandeenbash("echo 'UBUNTU POST-INSTALL SCRIPT' > log.txt")


fairecommandeenbash("echo 'mise a jour de apt et apt-get' >> log.txt")
fairecommandeenbash("sudo apt update && sudo apt upgrade") 
fairecommandeenbash("sudo apt-get update && sudo apt-get upgrade")

fairecommandeenbash("echo 'Installation de git curl et python' >> log.txt")

fairecommandeenbash("sudo apt-get install --yes git git-extras build-essential python3-pip htop glances git python3.6 curl")

fairecommandeenbash("echo 'Ajout de la clé PGP et du PPA d microsoft' >> log.txt")

fairecommandeenbash("curl https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor > packages.microsoft.gpg")

fairecommandeenbash("echo 'instalation de vscode' >> log.txt")

fairecommandeenbash("sudo apt-get install apt-transport-https")
fairecommandeenbash("sudo apt-get update")
fairecommandeenbash("sudo apt-get install code")

fairecommandeenbash("echo 'tout est carrer' >> log.txt")