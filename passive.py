import argparse
import os

def search_full_name(first_name, last_name):
    # Exemple de données fictives
    address = "7 rue du Progrès, 75016 Paris"
    number = "+33601010101"
    
    result = f"First name: {first_name}\nLast name: {last_name}\nAddress: {address}\nNumber: {number}"
    save_to_file("result.txt", result)

def search_ip(ip_address):
    # Exemple de données fictives
    isp = "FSociety, S.A."
    city_lat_lon = "(13.731) / (-1.1373)"
    
    result = f"ISP: {isp}\nCity Lat/Lon:\t{city_lat_lon}"
    save_to_file("result2.txt", result)

def search_username(username):
    # Exemples de réseaux sociaux
    platforms = {
        "Facebook": True,
        "Twitter": True,
        "LinkedIn": True,
        "Instagram": False,
        "Skype": True
    }
    
    result = "\n".join([f"{platform}: {'yes' if exists else 'no'}" for platform, exists in platforms.items()])
    save_to_file("result3.txt", result)

def save_to_file(filename, content):
    # Vérifie si le fichier existe déjà et modifie le nom si c'est le cas
    if os.path.exists(filename):
        filename = "result2.txt" if filename == "result.txt" else "result3.txt"
    
    with open(filename, 'w') as f:
        f.write(content)
    
    print(f"Saved in {filename}")

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
