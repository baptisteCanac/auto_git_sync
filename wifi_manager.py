import subprocess
import logging

from config import *

# Configuration du fichier de logs unique
logging.basicConfig(
    filename="logs.log",  # Un seul fichier pour tous les logs
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

class WifiManager:
    def __init__(self):
        self.nom_reseau = nom_reseau
        self.mdp_reseau = mot_de_passe_reseau

    def activer_wifi(self):
        logging.info("Tentative d'activation du Wi-Fi...")
        try:
            if systeme == "Linux":
                logging.info("Système détecté: Linux")
                subprocess.run(["nmcli", "radio", "wifi", "on"], check=True)
            elif systeme == "Darwin":
                logging.info("Système détecté: MacOS")
                subprocess.run(["networksetup", "-setairportpower", "en0", "on"], check=True)
            logging.info("Wi-Fi activé avec succès.")
        except Exception as e:
            logging.error(f"Erreur lors de l'activation du Wi-Fi : {e}")

    def desactiver_wifi(self):
        logging.info("Tentative de désactivation du Wi-Fi...")
        try:
            if systeme == "Linux":
                logging.info("Système détecté: Linux")
                logging.warning("Désactivation du Wi-Fi non implémentée pour Linux.")
            elif systeme == "Darwin":
                logging.info("Système détecté: MacOS")
                subprocess.run(["networksetup", "-setairportpower", "en0", "off"], check=True)
                logging.info("Wi-Fi désactivé avec succès.")
        except Exception as e:
            logging.error(f"Erreur lors de la désactivation du Wi-Fi : {e}")

    def se_connecter(self):
        logging.info(f"Tentative de connexion au réseau : {self.nom_reseau}")
        try:
            if systeme == "Linux":
                subprocess.run(["nmcli", "dev", "wifi", "connect", self.nom_reseau, "password", self.mdp_reseau], check=True)
            elif systeme == "Darwin":
                subprocess.run(["networksetup", "-setairportnetwork", "en0", self.nom_reseau, self.mdp_reseau], check=True)
            logging.info(f"Connexion réussie au réseau : {self.nom_reseau}")
        except Exception as e:
            logging.error(f"Impossible de se connecter au réseau {self.nom_reseau} : {e}")
