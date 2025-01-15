import requests
from bs4 import BeautifulSoup
import json

# URL de la page des applications Zapier
URL = "https://zapier.com/apps"

# Envoi d'une requête GET
response = requests.get(URL)

# Vérification du succès de la requête
if response.status_code == 200:
    soup = BeautifulSoup(response.content, "html.parser")

    # Extraction des blocs contenant les informations des apps
    app_blocks = soup.find_all("div", class_="grid gap-xs app-tile")[:20]  
# Limiter à 20 apps

    apps_data = []

    # Parcours des blocs pour récupérer les noms et logos
    for block in app_blocks:
        app_name = block.find("h3", class_="text-base font-medium").text.strip()
        app_logo = block.find("img", class_="app-tile__image")
        
        # Vérification si le logo est disponible
        logo_url = app_logo["src"] if app_logo else "No logo available"
        
        # Ajout aux données des apps
        apps_data.append({"name": app_name, "logo": logo_url})

    # Exportation des données en JSON
    with open("zapier_apps.json", "w") as f:
        json.dump(apps_data, f, indent=4)

    print("Extraction terminée ! Les données des 20 premières apps sont sauvegardées dans 'zapier_apps.json'.")
else:
    print(f"Échec de la requête. Code de statut: {response.status_code}")

