import subprocess

from config import *

class WifiManager:
    def __init__(self):
        pass

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