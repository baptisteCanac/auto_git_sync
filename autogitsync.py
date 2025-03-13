import tkinter as tk

import time

from wifi_manager import WifiManager
from github_manager import GithubManager

def show_popup():
    global popup
    popup = tk.Tk()  # Crée une fenêtre principale
    popup.title("AutoGitSync")
    popup.geometry("300x100")
    popup.resizable(False, False)

    label = tk.Label(popup, text="Synchronisation en cours, veuillez patienter...", font=("Arial", 12))
    label.pack(pady=20)

    # Lancer la fonction `test()` après un court délai (100ms)
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
    se connecter au bon réseau

    se connecter au bon compte github
    créer une nouvelle branche
    se déconnecter du compte github

    oublier le réseau
    Désactiver le wifi
    """
    
    WifiManager().activer_wifi()

    WifiManager().se_connecter()

    time.sleep(10)

    GithubManager().execute_workflow()

    #WifiManager().desactiver_wifi()

    # Fermer la pop-up une fois `test()` terminé
    close_popup()

# Exemple d'utilisation
show_popup()