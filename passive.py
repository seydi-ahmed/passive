import argparse
import os
import requests
from bs4 import BeautifulSoup

#*************************search_full_name***********************************

def search_full_name(first_name, last_name):
    """
    Recherche des informations sur une personne donnée par son prénom et son nom
    en utilisant des moteurs de recherche.
    
    :param first_name: Prénom de la personne
    :param last_name: Nom de la personne
    """
    full_name = f"{first_name} {last_name}"
    query = f"{full_name} site:linkedin.com OR site:facebook.com OR site:github.com"

    # Rechercher sur Google
    search_url = f"https://www.google.com/search?q={requests.utils.quote(query)}"
    
    try:
        response = requests.get(search_url, headers={'User-Agent': 'Mozilla/5.0'})
        response.raise_for_status()
        
        # Analyse le contenu de la page
        soup = BeautifulSoup(response.text, 'html.parser')

        # Cherche les résultats
        results = soup.find_all('h3')  # Exemple de recherche des titres de résultats

        # Simuler la recherche d'informations supplémentaires
        address = "Information d'adresse non trouvée"  # Remplacer par une recherche réelle si nécessaire
        number = "Information de numéro non trouvée"    # Remplacer par une recherche réelle si nécessaire

        # Formatage du résultat
        result_text = (
            f"First name: {first_name}\n"
            f"Last name: {last_name}\n"
            f"Address: {address}\n"
            f"Number: {number}"
        )
    except requests.exceptions.RequestException as e:
        result_text = f"Error during the search: {str(e)}"

    # Enregistre dans result.txt
    save_to_file("result.txt", result_text)

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

        # Enregistrement dans le fichier result2.txt
        save_to_file("result2.txt", result)

    except requests.exceptions.RequestException as e:
        save_to_file("result2.txt", f"Error: {str(e)}")


#*************************search_username***********************************

def search_username(username):
    # Enlève le '@' au début du nom d'utilisateur, s'il est présent
    username = username.lstrip('@')

    # Liste des plateformes à vérifier
    platforms = {
        "Github": f"https://www.github.com/{username}", #Nice
        "Youtube": f"https://www.youtube.com/{username}", #Nice
        "Instagram": f"https://www.instagram.com/{username}", #Nice
        "Twitter": f"https://x.com/{username}", #Nice
        "MySpace": f"https://www.myspace.com/{username}" #Nice
    }
    
    results = []
    
    for platform, url in platforms.items():
        try:
            response = requests.get(url)
            if response.status_code == 200:
                results.append(f"{platform}: yes")
            elif response.status_code == 404:
                results.append(f"{platform}: no")
            else:
                results.append(f"{platform}: error ({response.status_code})")
        except requests.exceptions.RequestException as e:
            results.append(f"{platform}: error ({str(e)})")
    
    result = "\n".join(results)
    save_to_file("result3.txt", result)

#*************************save***********************************

def save_to_file(filename, content):
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
