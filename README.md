# **Note de cadrage : auto_git_sync**

## **1. Contexte et objectifs**
auto_git_sync est un script d'automatisation qui assure la sauvegarde et la synchronisation de fichiers sur un dépôt GitHub en activant temporairement le Wi-Fi. L'objectif est de permettre des sauvegardes automatiques et sécurisées tout en minimisant l'exposition du système à Internet.

### **Objectifs spécifiques :**
- Activer le Wi-Fi sur Linux/macOS.
- Se connecter à un réseau Wi-Fi préconfiguré.
- Vérifier l'état du dépôt Git et effectuer un commit/push des fichiers mis à jour.
- Se déconnecter du Wi-Fi après l'opération.
- Générer des logs pour suivre l'exécution du script.

## **2. Périmètre du projet**
### **Inclusions :**
✅ Connexion/déconnexion automatique au Wi-Fi.
✅ Gestion des opérations Git (commit, merge, push).
✅ Configuration simple via un fichier dédié.
✅ Exécution automatique selon une fréquence définie.
✅ Journalisation des opérations.

### **Exclusions :**
❌ Support de Windows (uniquement Linux et macOS).
❌ Gestion avancée des conflits Git.
❌ Interface graphique (script en ligne de commande uniquement).

## **3. Technologies et contraintes**
- **Langage** : Python 3
- **Modules** : subprocess, os, GitPython, logging
- **Système cible** : Linux/macOS
- **Exécution** : via cron ou systemd pour une automatisation récurrente

## **4. Architecture du projet**

```
/autogitsync/
│── autogitsync.py       # Script principal
│── config.py            # Configuration (Wi-Fi, GitHub)
│── wifi_manager.py      # Module de gestion du Wi-Fi
│── git_manager.py       # Module de gestion Git
│── logs/                # Dossier contenant les logs
│── requirements.txt     # Dépendances du projet
│── README.md            # Documentation
```

## **5. MVP (Produit Minimum Viable)**
### **Critères de réussite du MVP :**
✔ Activation et connexion au Wi-Fi.
✔ Exécution d'un commit/push sur un dépôt GitHub.
✔ Déconnexion automatique du Wi-Fi après la sauvegarde.
✔ Génération de logs d'exécution.

### **Tâches à réaliser :**
1. **Configurer un fichier `config.py`** avec :
   - SSID et mot de passe Wi-Fi.
   - Chemin du dépôt Git.
   - Token d’authentification GitHub.
2. **Développer `wifi_manager.py`** :
   - Utilisation de `nmcli` sous Linux et `networksetup` sous macOS.
   - Vérification de la connexion avant de continuer.
3. **Développer `git_manager.py`** :
   - Vérification de l'état du repo.
   - Ajout et commit des fichiers modifiés.
   - Push sur GitHub.
4. **Développer `autogitsync.py`** :
   - Orchestration des modules Wi-Fi et Git.
   - Gestion des erreurs et journalisation.
5. **Tester et valider** sur Linux/macOS.

## **6. Suivi et évolution**
- **Phase 1** : Développement du MVP et tests sur différentes configurations.
- **Phase 2** : Optimisation de la gestion des erreurs et amélioration des logs.
- **Phase 3** : Ajout de nouvelles fonctionnalités (ex : choix de fichiers spécifiques à synchroniser).

---
✅ **Livrable final : un script Python exécutable en ligne de commande qui réalise des sauvegardes GitHub en activant temporairement le Wi-Fi.**

