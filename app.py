from flask import Flask, render_template
import urllib.request, json

app = Flask(__name__)

#obter lista personagens
@app.route('/')
def get_list_characters_pages():
    url = "https://rickandmortyapi.com/api/character/"
    response = urllib.request.urlopen(url)
    data = response.read()
    dict = json.loads(data) 

    return render_template("characters.html", characters=dict["results"])

# obter perfil único
@app.route('/profile/<id>')
def get_profile(id):
    url = "https://rickandmortyapi.com/api/character/" + id
    response = urllib.request.urlopen(url)
    data = response.read()
    dict = json.loads(data) 

    return render_template("profile.html", profile=dict)


#obter lista de personagens
@app.route('/lista')
def get_list_characters():

    url = "https://rickandmortyapi.com/api/character/"
    response = urllib.request.urlopen(url)
    characters = response.read()
    dict = json.loads(characters)
    characters = []

    for character in dict["results"]:
        character = {
            "name": character["name"],
            "status":character["status"],
            "especie":character["spercies"],
            "genero":character["gender"],
            "origem":character["location"],


        }

        characters.append(character)

    return {"characters": characters}

#Rota para listar as localizações
@app.route('/locations')
def get_list_locations():
    url = "https://rickandmortyapi.com/api/location"
    response = urllib.request.urlopen(url)
    locations = response.read()
    dict = json.loads(locations)
    locations_list = []
 #LISTA DE LOCALIZAÇÃO
    
    for location in dict["results"]:
        location_dict = {
            "Nome": location["name"],
            "Tipo": location["type"],
            "Dimensão":location["dimension"],
            "Personagens":location["residents"],
            "codigo":location["id"]
        }
        locations_list.append(location_dict)
        #print(location_dict)
       
    return render_template("locations.html",locations=locations_list)

#Rota para listar as Episódios
@app.route('/episodes')
def get_list_episodes():
    url = "https://rickandmortyapi.com/api/episode"
    response = urllib.request.urlopen(url)
    episodes = response.read()
    dict = json.loads(episodes)
    episodes_list = []
 #LISTA DE EPISÓDIOS
    
    for episode in dict["results"]:
        episode_dict = {
            "Nome": episode["name"],
            "Data": episode["air_date"],
            "Código": episode["id"],
        }
        episodes_list.append(episode_dict)
        #print(episode_dict)
       
    return render_template("episodes.html",episodes=episodes_list)

# obter Localização única
@app.route("/location/<id>")
def get_single_location(id):
    url = "https://rickandmortyapi.com/api/location/" + id
    response = urllib.request.urlopen(url)
    data = response.read()
    single_location = json.loads(data)
    
    #print(data)

    return render_template("location.html",  location = single_location)
#obter episódio unico
@app.route("/episode/<id>")
def get_single_episode(id):
    url = "https://rickandmortyapi.com/api/episode/" + id
    #url = f"https://rickandmortyapi.com/api/episode/{id}"
    response = urllib.request.urlopen(url)
    data = response.read()
    single_episode = json.loads(data)

    return render_template("episode.html", episode = single_episode)
