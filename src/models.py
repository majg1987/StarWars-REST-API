from flask_sqlalchemy import SQLAlchemy

# db = SQLAlchemy()

# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     email = db.Column(db.String(120), unique=True, nullable=False)
#     password = db.Column(db.String(80), unique=False, nullable=False)
#     is_active = db.Column(db.Boolean(), unique=False, nullable=False)

#     def __repr__(self):
#         return '<User %r>' % self.username

#     def serialize(self):
#         return {
#             "id": self.id,
#             "email": self.email,
#             # do not serialize the password, its a security breach
#         }

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable = False)
    email = db.Column(db.String(200), unique = True, nullable = False)
    password = db.Column(db.String(20), unique = True, nullable = False)
    favourites = db.relationship('Favourites', backref = 'User')

    def __repr__(self):
        return '<User %r>' % self.id

    def serialize(self):
        return{
            "id": self.id,
            "name": self.name,
            "email": self.email
        }


class Character(db.Model):
    __tablename__ = 'character'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(250), unique = True, nullable = False)
    gender = db.Column(db.String(20), nullable = False)
    birth_date = db.Column(db.String(10), nullable = False)
    height = db.Column(db.Integer, nullable = False)
    hair_color = db.Column(db.String(50), nullable=False)
    eye_color = db.Column(db.String(50), nullable = False)
    skin_color = db.Column(db.String(50), nullable = False)
    url_image = db.Column(db.String(200), unique = True, nullable = False)
    description = db.Column(db.String(500), unique = True, nullable = False)
    planet_id = db.Column(db.Integer, db.ForeignKey('planet.id'))
    vehicles = db.relationship('Vehicles', backref = 'character')

    def __repr__(self):
        return '<Character %r>' % self.id

    def serialize(self):
        return{
            "id": self.id,
            "name": self.name,
            "gender": self.gender,
            "birth_date": self.birth_date,
            "heigth": self.heigth,
            "hair_color": self.hair_color,
            "eye_color": self.eye_color,
            "skin_color": self.skin_color,
            "url_image": self.url_image,
            "description": self.description,
            "planet_id": self.planet_id
        }

class Planet(db.Model):
    __tablename__= 'planet'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(250), unique = True, nullable = False)
    population = db.Column(db.Integer, nullable = False)
    terrain = db.Column(db.String(50), nullable = False)
    climate = db.Column(db.String(50), nullable = False)
    orbit_period = db.Column(db.Integer, nullable = False)
    orbit_rotation = db.Column(db.Integer, nullable = False)
    diameter = db.Column(db.Integer, nullable = False)
    url_image = db.Column(db.String(200), unique = True, nullable = False)
    description = db.Column(db.String(500), unique = True, nullable = False)
    character = db.relationship('Character', backref = 'planet')
    vehicles = db.relationship('Vehicles', backref = 'planet')

    def __repr__(self):
        return '<Planet %r>' % self.id

    def serialize(self):
        return{
            "id": self.id,
            "name": self.name,
            "population": self.population,
            "terrain": self.terrain,
            "climate": self.climate,
            "orbit_period": self.orbit_period,
            "orbit_rotation": self.orbit_rotation,
            "diameter": self.diameter,
            "url_image": self.url_image,
            "description": self.description,
        }


class Vehicles(db.Model):
    __tablename__='vehicles'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(250), unique = True, nullable = False)
    model = db.Column(db.String(100), nullable = False)
    vehicle_class = db.Column(db.String(100), unique = True, nullable = False)
    passengers = db.Column(db.Integer, nullable = False)
    max_speed = db.Column(db.Integer, nullable = False)
    consumables = db.Column(db.Integer, nullable = False)
    url_image = db.Column(db.String(200), unique = True, nullable = False)
    description = db.Column(db.String(500), unique = True, nullable = False)
    planet_id = db.Column(db.Integer, db.ForeignKey('planet.id'))
    character_id = db.Column(db.Integer, db.ForeignKey('character.id'))

    def __repr__(self):
        return '<Vehicles %r>' % self.id

    def serialize(self):
        return{
            "id": self.id,
            "name": self.name,
            "model": self.model,
            "vehicle_class": self.vehicle_class,
            "passengers": self.passengers,
            "max_speed": self.max_speed,
            "consumables": self.consumables,
            "url_image": self.url_image,
            "description": self.description,
            "planet_id": self.planet_id,
            "character_id": self.character_id
        }

class Favourites(db.Model):
    __tablename__ = 'favourites'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(250), nullable = False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return 'Favourites %r>' % self.id

    def serialize(self):
        return{
            "id": self.id,
            "name": self.name,
            "user_id": self.user_id
        }