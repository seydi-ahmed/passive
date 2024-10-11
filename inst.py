import requests

def check_instagram_user_presence(user_id, access_token):
    # Construire l'URL de l'API pour récupérer les informations de l'utilisateur
    url = f"https://graph.instagram.com/{user_id}?fields=id,username&access_token={access_token}"
    
    response = requests.get(url)

    # Vérifier le code de réponse HTTP
    if response.status_code == 200:
        # La requête a réussi, l'utilisateur existe
        user_data = response.json()
        if 'id' in user_data:
            return f"Instagram: yes, username: {user_data['username']}, id: {user_data['id']}"
        else:
            return f"Instagram: no, user data not found"
    elif response.status_code == 404:
        # L'utilisateur n'a pas été trouvé
        return f"Instagram: no, user not found"
    else:
        # Gérer les autres erreurs possibles
        return f"Instagram: error ({response.status_code}) - {response.text}"

# Exemple d'utilisation :
access_token = 'EAAYzSaZAZChBgBOzojcchglybjxfPMOf5C9eqbN13GNTPXLLgZBTcCDKZB3QGUzXXjHq1vhQ7x52iyOmEDw6ZBL1dK0LZA6mFyvLbDZClUgHqRebMjJrb95plZCXwklLGCacYQPrNmrbipTtZBDHcXNMF532NEPMGaZCE8WGO1xFmZBJbF5BhRe8ZCnJsDoFgmNNJeHOZAeJ7ARz5aSZAoY2I4fQZDZD'
user_id = 'diop'

print(check_instagram_user_presence(user_id, access_token))
