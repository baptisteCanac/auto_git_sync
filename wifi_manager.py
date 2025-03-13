import subprocess

from config import *

class WifiManager:
    def __init__(self):
        self.nom_reseau = nom_reseau
        self.mpd_reseau = mot_de_passe_reseau

    def activer_wifi(self):
        print("Activation du wifi en cours")
        try:
            if systeme == "Linux":
                print("Système détecté: Linux")
                subprocess.run(["nmcli", "radio", "wifi", "on"], check=True)
                print("wifi activé")
            elif systeme == "Darwin":
                print("Système détecté: MacOs")
                subprocess.run(["networksetup", "-setairportpower", "en0", "on"], check=True)
                print("wifi activé")
        except:
            print("Erreur: impossible d'activer le wifi")
    
    def desactiver_wifi(self):
        print("Désactivation du wifi")
        try:
            if systeme == "Linux":
                print("Systeme détecté: Linux")
                print("fonction pas encore implémentée pour linux")
            elif systeme == "Darwin":
                print("Système détecté: MacOs")
                subprocess.run(["networksetup", "-setairportpower", "en0", "off"])
                print("Wifi désactivé avec succès")
        except:
            print("Erreur: impossible de désactiver le wifi")
    
    def se_connecter(self):
        print("Connexion au wifi")
        try:
            if systeme == "Linux":
                subprocess.run(["nmcli", "dev", "wifi", "connect", self.nom_reseau, "password", self.mdp_reseau])
                print("Connection au réseau effectuée avec succès")
            elif systeme == "Darwin":
                subprocess.run(["networksetup", "-setairportnetwork", "en0", self.nom_reseau, self.mdp_reseau])
                print("Connection au réseau effectuée avec succès")
        except:
            print("Impossible de se connecter au réseau\nLe réseau est peut être déja connecté sinon votre fichier de config possede une erreur")