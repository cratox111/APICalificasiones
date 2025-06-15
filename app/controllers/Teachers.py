from flask import jsonify, request
from werkzeug.security import generate_password_hash, check_password_hash
from app import db
from app.models.Teachers import Profesor
from app.models.Class import Classes

def userCreate():
    inputData = request.get_json()

    if not inputData:
        return jsonify({'message':'No data provided'})

    name = inputData.get('name')
    email = inputData.get('email')
    password = inputData.get('password')

    if not name or not email or not password:
        return jsonify({'message': 'Name, email, and password are required'})

    profesor_exits = Profesor.query.filter_by(email=email).first()
    if profesor_exits:
        return jsonify({'message':'data already exists'})
    
    password_hash = generate_password_hash(password, method='pbkdf2:sha256')

    new_user = Profesor(name=name, email=email, password=password_hash)

    db.session.add(new_user)
    db.session.commit()

    return jsonify({'message':'User created'})

def loginUser():
    inputData = request.get_json()


    if not inputData:
        return jsonify({'message':'data is missing'})
    
    name = inputData.get('name')
    email = inputData.get('email')
    password = inputData.get('password')

    if not name or not email or not password:
        return jsonify({'message':'data is missing'})
    
    profesor = Profesor.query.filter_by(email=email).first()

    if not profesor or not check_password_hash(profesor.password, password):
        return jsonify({'message': 'Incorrect email or password'})
    
    return jsonify({'message': 'Login successful'})
    
def createClass():
    inputData = request.get_json()