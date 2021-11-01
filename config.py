from flask import Flask, request, jsonify, Response, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)

# tex = Person.query.filter_by(name='Tex').first()
# tex >>> <Person 1>
# tex.id >>> 1
# tex.name >>> 'Tex'
# tex.pets >>> [<Pet 1>, <Pet 3>]
# tex.pets[0] >>> <Pet 1>
# tex.pets[0].name >>> 'Cookie'
# tex.pets[1].name >>> 'Spy Fish'
