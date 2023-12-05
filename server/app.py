# server/app.py
#!/usr/bin/env python3

from flask import Flask, make_response
from flask_migrate import Migrate

from models import db, Earthquake

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///earthquakes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

migrate = Migrate(app, db)
db.init_app(app)


@app.route('/')
def index():
    body = {'message': 'Flask SQLAlchemy Lab 1'}
    return make_response(body, 200)

# Add views here
@app.route('/earthquakes/<int:id>')
def res_by_id(id):
    quake = Earthquake.query.filter(Earthquake.id == id).first()
    
    if quake != None:
        response_body = quake.to_dict()
        return make_response(response_body,200)
    
    return {"error": "Hotel Not Found!"}

@app.route('/earthquakes/magnitude/<float:magnitude>')
def by_mag(magnitude):
    quakes = Earthquake.query.filter(Earthquake.magnitude >= magnitude).all()
    
    if quakes != []:
        response_body = [quake.to_dict() for quake in quakes]
        return make_response(response_body,200)
    
    return {"error": "Hotel Not Found!"}


if __name__ == '__main__':
    app.run(port=5001, debug=True)
