from flask import jsonify, make_response, request
from config.server_conf import db
from flask_sqlalchemy import SQLAlchemy as sq
from datetime import datetime

class Community(db.model):
    id_community = db.Column(db.Integer, nullable = False, primary_key = True)
    name = db.Column(db.String(60), nullable = False)
    description = db.Column(db.String(120))
    created_at = db.Column(db.datetime)
    updated_at = db.Column(db.datetime)

class User(db.model):
    id_user = db.Column(db.Integer, nullable = False, primary_key = True)
    name = db.Column(db.String(60), nullable = False)
    email = db.Coumn(db.String(100), nullable = False)
    password = db.Coumn(db.String(100), nullable = False)
    created_at = db.Column(db.datetime)
    updated_at = db.Column(db.datetime)

#Controlador Usuario a comunidad
class User_belongs_to_Community(db.model):
    id_user = db.Column(db.Integer, sq.ForeignKey(User.id_user), nullable = False)
    id_community = db.Column(db.Integer, sq.ForeignKey(Community.id_community), nullable = False)
    date = db.Column(db.datetime, nullable = False)
    
    def __init__(self,id_community,id_user,date):
        self.id_community = id_community
        self.id_user = id_user
        self.date = date

    def create_belong():
        id_community = request.form['id_community']
        id_user = request.form['id_user']
        date = request.form['date']
        
        new_belong = User_belongs_to_Community(id_community, id_user, date)

        db.session.add(new_belong)
        db.session.commit()

    def list_belong():
        belong_list = User_belongs_to_Community.query.all()

        response = make_response(jsonify(belong_list),200)
        response.headers["Content-Type"] = "application/json"

        return response
        
    def delete_belong(id_user,id_community):
        
        db.session.delete(id_user,id_community)
        db.session.commit()