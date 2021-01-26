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
fairecommandeenbash("sudo install -o root -g root -m 644 packages.microsoft.gpg /usr/share/keyrings/")
fairecommandeenbash("sudo sh -c 'echo \"deb [arch=amd64 signed-by=/usr/share/keyrings/packages.microsoft.gpg] https://packages.microsoft.com/repos/vscode stable main\" > /etc/apt/sources.list.d/vscode.list'")

fairecommandeenbash("echo 'instalation de vscode' >> log.txt")

fairecommandeenbash("sudo apt-get install apt-transport-https")
fairecommandeenbash("sudo apt-get update")
fairecommandeenbash("sudo apt-get install code")

fairecommandeenbash("echo 'tout est carrer' >> log.txt")