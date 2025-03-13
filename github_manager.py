import os
import subprocess
import logging
from config import *

# Configuration du fichier de logs unique
logging.basicConfig(
    filename="logs.log",  
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

class GithubManager:
    def __init__(self):
        self.token = github_token
        self.repo_url = repo_url
        self.branch_name = nouvelle_branche
        self.commit_message = commit_message
        self.local_path = lien_repo_local

    def _get_authenticated_url(self):
        """Construit l'URL du dépôt avec authentification HTTPS via token."""
        return self.repo_url.replace("https://", f"https://{self.token}@")

    def clone_repository(self):
        """Clone le dépôt en local après suppression s'il existe déjà."""
        if os.path.exists(self.local_path):
            logging.info(f"Suppression du dossier existant : {self.local_path}")
            subprocess.run(["rm", "-rf", self.local_path], check=True)

        logging.info(f"Clonage du dépôt : {self.repo_url}")
        try:
            subprocess.run(["git", "clone", self._get_authenticated_url(), self.local_path], check=True)
            logging.info("Clonage réussi.")
        except subprocess.CalledProcessError as e:
            logging.error(f"Erreur lors du clonage : {e}")

    def create_branch(self):
        """Crée une nouvelle branche."""
        os.chdir(self.local_path)
        logging.info(f"Création de la branche : {self.branch_name}")
        try:
            subprocess.run(["git", "checkout", "-b", self.branch_name], check=True)
            logging.info(f"Branche '{self.branch_name}' créée avec succès.")
        except subprocess.CalledProcessError as e:
            logging.error(f"Erreur lors de la création de la branche : {e}")

    def add_and_commit_files(self):
        """Ajoute et commit les fichiers dans le dépôt."""
        logging.info("Ajout des fichiers au commit...")

        if not os.listdir(self.local_path):  
            logging.info("Le dépôt est vide, ajout d'un fichier .gitkeep")
            with open(os.path.join(self.local_path, ".gitkeep"), "w") as f:
                f.write("Fichier pour garder le dépôt non vide")

        subprocess.run(["git", "add", "."], check=True)

        # Vérifier si des fichiers ont été ajoutés avant de commit
        result = subprocess.run(["git", "status", "--porcelain"], capture_output=True, text=True)
        if result.stdout.strip():
            logging.info(f"Commit avec le message : {self.commit_message}")
            try:
                subprocess.run(["git", "commit", "-m", self.commit_message], check=True)
                logging.info("Commit effectué avec succès.")
            except subprocess.CalledProcessError as e:
                logging.error(f"Erreur lors du commit : {e}")
        else:
            logging.warning("Aucun changement détecté, commit annulé.")

    def push_branch(self):
        """Push la branche nouvellement créée sur le dépôt distant."""
        logging.info(f"Push de la branche : {self.branch_name}")
        try:
            subprocess.run(["git", "push", "--set-upstream", "origin", self.branch_name], check=True)
            logging.info("Push effectué avec succès.")
        except subprocess.CalledProcessError as e:
            logging.error(f"Erreur lors du push : {e}")

    def execute_workflow(self):
        """Exécute toutes les étapes dans l'ordre."""
        try:
            self.clone_repository()
            self.create_branch()
            self.add_and_commit_files()
            self.push_branch()
            logging.info("✅ Opérations Git terminées avec succès !")

        except subprocess.CalledProcessError as e:
            logging.error(f"❌ Erreur lors de l'exécution de Git : {e}")

        finally:
            os.chdir("..")  # Revenir au répertoire parent après l'exécution
            logging.info("Déconnexion et nettoyage terminés.")