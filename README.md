# install-winget
Un utilitaire graphique léger, autonome en Python/Tkinter pour automatiser l'installation par lots de logiciels sous Windows via **Winget**.

---

<img width="522" height="532" alt="1" src="https://github.com/user-attachments/assets/b449569d-9b3f-4023-98ae-a26027b42ff4" />


## Fonctionnalités

* **Zero dépendance tierce :** Utilise exclusivement la bibliothèque standard de Python (`tkinter`, `threading`, `subprocess`). Aucun `pip install` nécessaire.
* **Interface Réactive (Multi-threading) :** L'IHM reste fluide pendant les téléchargements et installations.
* **Mise à jour en temps réel :** Journal d'installation (logs) et barre de progression mis à jour de manière sécurisée (*thread-safe*).
* **Gestion des états d'IHM :** Verrouillage automatique des boutons et cases à cocher durant l'exécution pour éviter les clics multiples ou les erreurs d'inattention.
* **Installation silencieuse :** Accepte automatiquement les licences et sources `winget` pour une installation 100% automatisée.

---

## Prérequis

* **Système d'exploitation :** Windows 10 (version 1709 ou plus récente) ou Windows 11.
* **Gestionnaire de paquets :** `winget` (inclus par défaut sur la plupart des installations récentes de Windows).
* **Langage :** [Python 3.8+](https://www.python.org/) installé et ajouté au PATH.

---

## Utilisation

1. **Cloner ou télécharger le dépôt :**
   ```bash
   git clone https://github.com/T209995/install-winget.git
   cd install-winget
   ```

2. **Lancer l'application :**
   ```bash
   python app.py
   ```

3. **Installer des logiciels :**
   * Cochez les applications souhaitées.
   * Cliquez sur **Installer**.
   * Suivez la progression directement dans la fenêtre du journal.

---

##  Personnaliser la liste des logiciels

Vous pouvez facilement ajouter ou retirer des logiciels en modifiant le dictionnaire `PACKS` situé au début du fichier `app.py` :

```python
PACKS = {
    "Mozilla Firefox": "Mozilla.Firefox",
    "Google Chrome": "Google.Chrome",
    "Votre Logiciel": "Editeur.IdentifiantWinget",
}
```

> **Conseil :** Pour trouver l'ID Winget exact d'un logiciel, ouvrez une invite de commandes Windows et tapez :  
> `winget search "nom_du_logiciel"`

---

## Licence

Ce projet est sous licence MIT — vous êtes libre de le modifier et de le redistribuer.
