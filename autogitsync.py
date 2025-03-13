import tkinter as tk
import time
import logging
from wifi_manager import WifiManager
from github_manager import GithubManager

# Configuration des logs
logging.basicConfig(
    filename="logs.log",  # Fichier de log
    level=logging.INFO,  # Niveau INFO pour suivre les événements normaux
    format="%(asctime)s - %(levelname)s - %(message)s",  # Format des logs
)

def show_popup():
    global popup
    popup = tk.Tk()  # Crée une fenêtre principale
    popup.title("AutoGitSync")
    popup.geometry("300x100")
    popup.resizable(False, False)

    label = tk.Label(popup, text="""Synchronisation en cours
    veuillez patienter...""", font=("Arial", 12))
    label.pack(pady=20)

    # Lancer la fonction `main()` après un court délai (100ms)
    popup.after(100, main)

    popup.mainloop()  # Démarrer la boucle d'événements Tkinter

def close_popup():
    global popup
    if popup:
        popup.destroy()
        popup = None

def main():
    """
    Activer le wifi
    Se connecter au bon réseau
    Se connecter au bon compte GitHub
    Créer une nouvelle branche
    Se déconnecter du compte GitHub
    Oublier le réseau
    Désactiver le wifi
    """
    logging.info("🔄 Début de la synchronisation.")
    
    logging.info("Activation du WiFi...")
    WifiManager().activer_wifi()
    
    logging.info("Connexion au réseau WiFi...")
    WifiManager().se_connecter()
    
    time.sleep(10)  # Attendre la connexion au WiFi
    
    logging.info("🚀 Exécution du workflow GitHub...")
    GithubManager().execute_workflow()
    
    logging.info("📴 Désactivation du WiFi...")
    WifiManager().desactiver_wifi()
    
    logging.info("✅ Synchronisation terminée.")
    
    close_popup()

# Exemple d'utilisation
show_popup()
