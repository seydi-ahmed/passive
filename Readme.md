# PASSIVE (first cybersecurity project)


## Compréhension de l'OSINT:
L'Intelligence Artificielle à Source Ouverte (OSINT) désigne la collecte et l'analyse d'informations provenant de sources publiques. Cela inclut :

- Registres publics
- Profils sur les réseaux sociaux
- Moteurs de recherche
- Articles d'actualité
- etc.

## Description:
Un outil en ligne de commande pour effectuer une reconnaissance passive à l'aide de méthodes d'intelligence à source ouverte. L'outil doit gérer trois types d'entrées :

- Nom complet (Prénom Nom)
- Adresse IP
- Nom d'utilisateur

## Utilisation:

### Installation:
Clone le dépôt:
```
git clone https://learn.zone01dakar.sn/git/mouhameddiouf/passive.git
```

### Commandes:
- **Recherche par Nom Complet :**
- commande:
    ```
    python3 passive.py -fn "Prénom Nom"
    ```
- resultat:
    ```
    First name: Prénom
    Last name: Nom
    Address: 7273 Avenida de América, Parla, Castilla y León, Spain 43092
    Number: 942-160-155
    Saved in result.txt
    ```

- **Recherche par Adresse IP :**
- commande:
    ```
    python3 passive.py -ip "adresseIp"
    ```
- resultat:
    ```
    ISP: AS8346 SONATEL-AS Autonomous System
    City: Dakar
    Latitude/Longitude: (14.6937) / (-17.4441)
    Saved in result2.txt
    ```

- **Recherche par Nom d'Utilisateur :**
- commande:
    ```
    python3 passive.py -u "@utilisateur"
    ```
- resultat:
    ```
    Github: no
    Youtube: no
    Instagram: yes
    Twitter: yes
    MySpace: no
    Saved in result3.txt
    ```

### Sortie:
Les résultats sont sauvegardés dans `resultat.txt` ou dans un fichier similaire si ce dernier existe déjà.

### Développeur:
- Prénom Nom: Mouhamed Diouf
- git: mouhameddiouf
- email: seydiahmedelchikh@gmail.com