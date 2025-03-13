import os
import subprocess

from config import *

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
            print(f"Suppression du dossier existant : {self.local_path}")
            subprocess.run(["rm", "-rf", self.local_path], check=True)

        print(f"Clonage du dépôt : {self.repo_url}")
        subprocess.run(["git", "clone", self._get_authenticated_url(), self.local_path], check=True)

    def create_branch(self):
        """Crée une nouvelle branche."""
        os.chdir(self.local_path)
        print(f"Création de la branche : {self.branch_name}")
        subprocess.run(["git", "checkout", "-b", self.branch_name], check=True)

    def add_and_commit_files(self):
        """Ajoute et commit les fichiers dans le dépôt."""
        print("Ajout des fichiers au commit...")

        # Vérifier si le dépôt est vide, sinon ajouter un fichier placeholder
        if not os.listdir(self.local_path):  
            print("Le dépôt est vide, ajout d'un fichier .gitkeep")
            with open(os.path.join(self.local_path, ".gitkeep"), "w") as f:
                f.write("Fichier pour garder le dépôt non vide")

        subprocess.run(["git", "add", "."], check=True)

        # Vérifier si des fichiers ont été ajoutés avant de commit
        result = subprocess.run(["git", "status", "--porcelain"], capture_output=True, text=True)
        if result.stdout.strip():
            print(f"Commit avec le message : {self.commit_message}")
            subprocess.run(["git", "commit", "-m", self.commit_message], check=True)
        else:
            print("⚠️ Aucun changement détecté, commit annulé.")

    def push_branch(self):
        """Push la branche nouvellement créée sur le dépôt distant."""
        print(f"Push de la branche : {self.branch_name}")
        subprocess.run(["git", "push", "--set-upstream", "origin", self.branch_name], check=True)

    def execute_workflow(self):
        """Exécute toutes les étapes dans l'ordre."""
        try:
            self.clone_repository()
            self.create_branch()
            self.add_and_commit_files()
            self.push_branch()
            print("✅ Opérations Git terminées avec succès !")

        except subprocess.CalledProcessError as e:
            print(f"❌ Erreur lors de l'exécution de Git : {e}")

        finally:
            os.chdir("..")  # Revenir au répertoire parent après l'exécution
            print("Déconnexion et nettoyage terminés.")