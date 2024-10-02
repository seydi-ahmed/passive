import argparse
import requests
import os

def recherche_nom_complet(prenom, nom):
    # Logique de recherche fictive (remplacer par des appels à des API réelles)
    return {
        "adresse": "7 rue du Progrès, 75016 Paris",
        "numero": "+33601010101"
    }

def recherche_ip(ip):
    # Appel d'API pour obtenir des informations sur l'ISP et la ville
    response = requests.get(f"http://api.ipstack.com/{ip}?access_key=YOUR_ACCESS_KEY")
    data = response.json()
    return {
        "ISP": data.get("connection", {}).get("isp"),
        "ville": data.get("city"),
        "lat": data.get("latitude"),
        "lon": data.get("longitude")
    }

def recherche_utilisateur(utilisateur):
    # Logique pour vérifier la présence sur les réseaux sociaux
    plateformes = ["Facebook", "Twitter", "LinkedIn", "Instagram", "Skype"]
    resultats = {plateforme: False for plateforme in plateformes}
    # Vérifications simulées
    resultats["Facebook"] = True  # Supposons trouvé
    resultats["Twitter"] = True
    return resultats

def sauvegarder_resultats(nom_fichier, donnees):
    # Gestion de la création de fichiers
    if os.path.exists(nom_fichier):
        nom_fichier = "resultat2.txt"
    
    with open(nom_fichier, 'w') as fichier:
        fichier.write(str(donnees))

def main():
    parser = argparse.ArgumentParser(description='Outil de reconnaissance passive')
    parser.add_argument('-fn', help='Recherche par nom complet')
    parser.add_argument('-ip', help='Recherche par adresse IP')
    parser.add_argument('-u', help='Recherche par nom d\'utilisateur')
    args = parser.parse_args()

    if args.fn:
        prenom, nom = args.fn.split()
        resultats = recherche_nom_complet(prenom, nom)
        sauvegarder_resultats("resultat.txt", resultats)

    elif args.ip:
        resultats = recherche_ip(args.ip)
        sauvegarder_resultats("resultat.txt", resultats)

    elif args.u:
        resultats = recherche_utilisateur(args.u)
        sauvegarder_resultats("resultat.txt", resultats)

if __name__ == "__main__":
    main()
