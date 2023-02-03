# importation des librairies nécessaires
import requests
import json
from pymongo import MongoClient



# importation des données via l'API
pokemon = requests.get('https://pokebuildapi.fr/api/v1/pokemon')
list_pokemons = pokemon.json()



# connexion à Mongo DB
myclient = MongoClient("mongodb://root:1234@localhost:27017")
  
# connexion à la base de données
db = myclient["JDG"]
  
# connexion à la collection
Collection = db["pokemon"]
 


# insertion des pokémons à la bdd MongoDB
Collection.insert_many(list_pokemons)



# insertion du nouveau pokémon
nouveau_pokemon = { 
    "id": 899, 
    "pokedexId": 899, 
    "name": "Darty Papa", 
    "image": "https://tenor.com/fr/view/kassos-darty-papa-gif-5752923", 
    "videoYoutube": "https://www.youtube.com/watch?v=Gt5-xU1-Ows", 
    "slug": "Darty Papa", 
    "stats": {
         "HP": 100000000, 
         "attack": 100000000, 
         "defense": 2, 
         "special\_attack": 100000000, 
         "special\_defense": 2, 
         "speed": 1 }
}
Collection.insert_one(nouveau_pokemon)



# export de la base de données en format json
data = []
for documents in Collection.find():
    data.append(documents)

with open('database.json', 'w') as outfile :
    json.dump(data, outfile, default=str)