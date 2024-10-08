import argparse
import os
import requests

#*************************search_full_name***********************************

def search_full_name(first_name, last_name):
    # Exemple de données fictives
    address = "7 rue du Progrès, 75016 Paris"
    number = "+33601010101"
    
    result = f"First name: {first_name}\nLast name: {last_name}\nAddress: {address}\nNumber: {number}"
    save_to_file("result.txt", result)

 #*************************search_ip***********************************

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
    """
    Enregistre le contenu dans le fichier spécifié. 
    Si le fichier existe déjà, il sera écrasé.
    
    :param filename: Nom du fichier où le contenu sera enregistré
    :param content: Contenu à enregistrer dans le fichier
    """
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
