import subprocess

from config import *

class WifiManager:
    def __init__(self):
        pass

    def activer_wifi(self):
        print("activation du wifi en cours")
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