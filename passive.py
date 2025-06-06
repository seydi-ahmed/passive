import argparse
import os
import requests
import json
from bs4 import BeautifulSoup
import time

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
            print("this ip addres {ip_address} doesn't exist")
            return
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

def search_username(username):
    # Enlève le '@' au début du nom d'utilisateur, s'il est présent
    username = username.lstrip('@')

    # Liste des plateformes à vérifier
    platforms = {
        "Github": f"https://api.github.com/users/{username}",
        "Youtube": f"https://www.youtube.com/{username}",
        "Instagram": f"https://www.instagram.com/{username}/",
        "Reddit": f"https://www.reddit.com/user/{username}/about.json",
        "MySpace": f"https://www.myspace.com/{username}"
    }
    
    results = []
    
    # Remplacez par vos vraies clés API Twitter et Instagram
    BEARER_TOKEN = "AAAAAAAAAAAAAAAAAAAAAA3CwQEAAAAAilAee1FzUbV%2Bseg9Ax32Tk0rTEM%3DDIR5QsE694bTwA9Y3IuLPQQpaoGloRc21WjpCNFiI1OCbIKkj2"
    INSTAGRAM_TOKEN = "IGQWROZA1lZAb1dzaFlVLVpzbGtWUk9LNzU2cjJmZAW03VGdtOHRpSzZA3bWFUMl91T01BYkltR0FxV1FpZAWRUUHdhQmxOVkFyNlBuM2p0UUpEcGJMd3pjRXQ2b2xoT1cwblhYY3pkRTJpeDlUeGdsbEs1NVpjUnh0RUUZD"
    
    for platform, url in platforms.items():
        try:
            if platform == "Github":
                response = requests.get(url)
                if response.status_code == 200:
                    results.append(f"{platform}: yes")
                elif response.status_code == 404:
                    results.append(f"{platform}: no")
                else:
                    results.append(f"{platform}: error ({response.status_code})")
            elif platform == "Youtube":
                response = requests.get(url)
                if response.status_code == 200:
                    results.append(f"{platform}: yes")
                elif response.status_code == 404:
                    results.append(f"{platform}: no")
                else:
                    results.append(f"{platform}: error ({response.status_code})")
            elif platform == "Reddit":
                headers = {'User-Agent': 'MyRedditApp/0.1'}
                response = requests.get(url, headers=headers)
                
                if response.status_code == 200:
                    results.append(f"{platform}: yes")
                elif response.status_code == 404:
                    results.append(f"{platform}: no")
                else:
                    results.append(f"{platform}: error ({response.status_code})")
            elif platform == "MySpace":
                response = requests.get(url)
                if response.status_code == 200:
                    results.append(f"{platform}: yes")
                elif response.status_code == 404:
                    results.append(f"{platform}: no")
                else:
                    results.append(f"{platform}: error ({response.status_code})")
            elif platform == "Instagram":
                response = requests.get(url)
                
                if response.status_code == 200:
                    soup = BeautifulSoup(response.text, 'html.parser')
                    title = soup.find('title')
                    if title and username.lower() in title.text.lower():
                        results.append(f"{platform}: yes")
                    elif title and "Page Not Found" in title.text:
                        results.append(f"{platform}: no")
                    else:
                        results.append(f"{platform}: no")
                elif response.status_code == 404:
                    results.append(f"{platform}: no")
                else:
                    results.append(f"{platform}: error ({response.status_code})")
        except requests.exceptions.RequestException as e:
            results.append(f"{platform}: error ({str(e)})")
    
    result = "\n".join(results)
    print(result)
    save_to_file("result.txt", result)

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