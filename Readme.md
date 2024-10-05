# PASSIVE (first cybersecurity project)

## Description
Un outil en ligne de commande pour effectuer une reconnaissance passive à l'aide de méthodes d'intelligence à source ouverte.

## Utilisation

### Installation
Clone le dépôt:
```
git clone https://learn.zone01dakar.sn/git/mouhameddiouf/passive.git
```


### Commandes
- **Recherche par Nom Complet :**
    ```
    python3 passive.py -fn "Prénom Nom"
    ```

- **Recherche par Adresse IP :**
    ```
    python3 passive.py -ip "127.0.0.1"
    ```

- **Recherche par Nom d'Utilisateur :**
    ```
    python3 passive.py -u "@utilisateur"
    ```

### Sortie
Les résultats sont sauvegardés dans `resultat.txt` ou `resultat2.txt` si le fichier existe déjà.

### lien expliquant clairement "OSINT"
https://guardia.school/boite-a-outils/quest-ce-que-losint.html