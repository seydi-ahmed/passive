import argparse
import os
import requests
import json

#*************************search_full_name***********************************

def search_full_name(first_name, last_name):
    try:
        # Appel à l'API randomuser.me pour générer des données fictives
        response = requests.get('https://randomuser.me/api/')
        
        # Vérifie que la requête a réussi
        if response.status_code == 200:
            data = response.json()
            user = data.get("results", [])[0]  # Prend le premier utilisateur généré
            
            # Récupère et formate l'adresse
            address = (
                f"{user['location']['street']['number']} "
                f"{user['location']['street']['name']}, "
                f"{user['location']['city']}, "
                f"{user['location']['state']}, "
                f"{user['location']['country']} "
                f"{user['location']['postcode']}"
            )
            
            # Récupère le numéro de téléphone
            phone = user.get("phone", "Information de numéro non trouvée")
            
            # Formate le résultat
            result_text = (
                f"First name: {first_name}\n"
                f"Last name: {last_name}\n"
                f"Address: {address}\n"
                f"Number: {phone}"
            )
            
            # Enregistre les informations dans result.txt
            print(result_text)
            save_to_file("result.txt", result_text)
        else:
            print(f"API request failed with status code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred while calling the API: {e}")

#*************************search_ip*****************************************

def search_ip(ip_address):
    # Utilisation de l'API ipinfo.io pour obtenir les informations de l'IP
    url = f"https://ipinfo.io/{ip_address}/json"
    
    try:
        response = requests.get(url)
        data = response.json()

        # Vérification de l'existence de l'IP dans les données retournées
        if 'ip' not in data or 'error' in data:
            result = f"Error: Unable to retrieve information for IP {ip_address}"
        else:
            city = data.get('city', 'Unknown')
            org = data.get('org', 'Unknown')  # Organisation ou ISP
            loc = data.get('loc', 'Unknown').split(',')
            lat = loc[0] if len(loc) > 0 else 'Unknown'
            lon = loc[1] if len(loc) > 1 else 'Unknown'

            result = (
                f"ISP: {org}\n"
                f"City: {city}\n"
                f"Latitude/Longitude: ({lat}) / ({lon})"
            )

        # Enregistrement dans le fichier
        print(result)
        save_to_file("result.txt", result)

    except requests.exceptions.RequestException as e:
        save_to_file("result.txt", f"Error: {str(e)}")


#*************************search_username***********************************

import os
import sherlock
from pathlib import Path

def search_username(username):
    # Enlève le '@' au début du nom d'utilisateur, s'il est présent
    username = username.lstrip('@')
    
    # Choisir les plateformes à vérifier
    platforms = ["github", "instagram", "twitter", "facebook", "linkedin"]
    results = []

    # Dossier pour les résultats
    result_file = Path("result.txt")
    result_file2 = Path("result2.txt")

    # Lancer Sherlock pour l'utilisateur
    print(f"Recherche de {username} sur les plateformes {platforms}...")
    data = sherlock.sherlock(username, site_list=platforms, timeout=5, print_found_only=True)

    # Analyser les résultats de Sherlock
    for platform in platforms:
        # Vérifier si le nom de la plateforme apparaît dans les résultats trouvés
        found = any(platform in result.lower() for result in data.get(username, {}).keys())
        result = f"{platform.capitalize()}: {'yes' if found else 'no'}"
        results.append(result)

    # Préparer le texte à écrire dans le fichier de résultats
    result_text = "\n".join(results)

    # Écrire dans le fichier de résultats approprié
    if result_file.exists():
        with open(result_file2, "w") as result_file2_handle:
            result_file2_handle.write(result_text)
        print(f"Résultats enregistrés dans {result_file2}")
    else:
        with open(result_file, "w") as result_file_handle:
            result_file_handle.write(result_text)
        print(f"Résultats enregistrés dans {result_file}")

    # Afficher les résultats à l'écran pour le retour utilisateur
    print(f"\nRésultats pour {username}:\n{result_text}")

#*************************save***********************************

def save_to_file(filename, content):
    # Vérifie si le fichier existe déjà
    base_filename = filename.rsplit('.')[0]  # Enlève l'extension .txt pour l'incrémentation
    extension = '.txt'
    counter = 2

    # Incrémente le nom jusqu'à ce qu'un fichier disponible soit trouvé
    while os.path.exists(filename):
        filename = f"{base_filename}{counter}{extension}"
        counter += 1

    # Écrit le contenu dans le fichier trouvé
    with open(filename, 'w') as f:
        f.write(content)
    
    print(f"Saved in {filename}")

#*************************main***********************************

def main():
    parser = argparse.ArgumentParser(description='Welcome to passive v1.0.0')
    parser.add_argument('-fn', help='Search with full-name')
    parser.add_argument('-ip', help='Search with IP address')
    parser.add_argument('-u', help='Search with username')
    
    args = parser.parse_args()
    
    if args.fn:
        name_parts = args.fn.split()
        if len(name_parts) == 2:
            first_name, last_name = name_parts
            search_full_name(first_name, last_name)
        else:
            print("Please provide a valid full name in the format 'Last First'.")
    
    elif args.ip:
        search_ip(args.ip)
    
    elif args.u:
        search_username(args.u)
    
    else:
        print("No valid option provided. Use --help for usage instructions.")

if __name__ == "__main__":
    main()