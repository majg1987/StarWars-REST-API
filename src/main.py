"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from admin import setup_admin
from models import db, User, Character, Planet, Vehicles, Favorites
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DB_CONNECTION_STRING')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)
setup_admin(app)

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

# Personajes
# Listar info de todos los characters
@app.route('/character', methods=['GET'])
def traer_characters():
    characters = Character.query.all()
    characterList = list(map(lambda obj: obj.serialize(), characters))
    response_body = {
        "results": characterList
    }
    return jsonify(response_body), 200  

# Recibir info de un personaje a traves de su id
@app.route('/character/<int:id>', methods=['GET'])
def traer_one_characters(id):
    character_id = Character.query.get(id)
    character = character_id.serialize()
    response_body = {
        "results": character
    }
    return jsonify(response_body), 200

# Planetas
# Listar info de todos los planetas
@app.route('/planet', methods=['GET'])
def traer_planets():
    planets = Planet.query.all()
    planets_List = list(map(lambda obj: obj.serialize(), planets))
    response_body = {
        "results": planets_List
    }
    return jsonify(response_body), 200

# Recibir info de un planeta a traves de su id
@app.route('/planet/<int:id>', methods=['GET'])
def traer_one_planet(id):
    planet_id = Planet.query.get(id)
    planet = planet_id.serialize()
    response_body = {
        "results": planet
    }
    return jsonify(response_body), 200

# Vehiculos
# Listar info de todos los vehiculos
@app.route('/vehicles', methods=['GET'])
def traer_vehicles():
    vehicles = Vehicles.query.all()
    vehicles_List = list(map(lambda obj: obj.serialize(), vehicles))
    response_body = {
        "results": vehicles_List
    }
    return jsonify(response_body), 200

# Recibir info de un vehiculo a traves de su id
@app.route('/vehicles/<int:id>', methods=['GET'])
def traer_one_vehicle(id):
    vehicle_id = Vehicles.query.get(id)
    vehicle = vehicle_id.serialize()
    response_body = {
        "results": vehicle
    }
    return jsonify(response_body), 200


# Usuarios
# Listar info de todos los usuarios
@app.route('/user', methods=['GET'])
def traer_usuarios():
    users = User.query.all()
    userList = list(map(lambda obj: obj.serialize(), users))
    print(userList)

    response_body = {
        "results": userList
    }
    return jsonify(response_body), 200

# Favoritos
# # Listar favoritos de un usuario
@app.route('/user/<int:id>/favorites', methods=['GET'])
def traer_favoritos_usuario(id):
    user_favorites = Favorites.query.filter_by(user_id = id).all()
    print(user_favorites)
    favorite_list = list(map(lambda obj: obj.serialize(), user_favorites))
    print(favorite_list)
    response_body = {
        "results": favorite_list
    }
    return jsonify(response_body), 200

# # Añadir favoritos a un usuario
# @app.route('user:<int:id>/favourites', methods=['GET'])
# def añadir_favoritos_usuario(id):
#     user_favourites = list(Favourites.query.filter_by(user_id = user_id).all())
#     print(user_favourites)
#     # favourite = user_favourites.serialize()
#     response_body = {
#         "results": user_favourites
#     }
#     return jsonify(response_body), 200

# this only runs if `$ python src/main.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
