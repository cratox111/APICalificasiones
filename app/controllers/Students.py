from flask import jsonify, request, json
from app import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from app.models.Students import Students
from app.models.Class import Classes

def newUser():
    inputData = request.get_json()

    if not inputData:
        return jsonify({'message':'Not data'}), 400
    
    name = inputData.get('name')
    email = inputData.get('email')
    password = inputData.get('password')
    semester = inputData.get('semester')

    if not name or not email or not password or not semester:
        return jsonify({'message':'Not data'}), 400

    password_hash = generate_password_hash(password, method='pbkdf2:sha256')
    newUser = Students(name=name, email=email, password=password_hash, semester=semester)

    db.session.add(newUser)
    db.session.commit()
    return jsonify({'message':'User creat'}), 201

def loginUser():
    inputData = request.get_json()

    if not inputData:
        return jsonify({'message': 'No data provided'}), 400

    email = inputData.get('email')
    password = inputData.get('password')

    if not email or not password:
        return jsonify({'message': 'Email and password are required'}), 400

    student = Students.query.filter_by(email=email).first()

    if not student or not check_password_hash(student.password, password):
        return jsonify({'message': 'Incorrect email or password'}), 401
    
    access_token = create_access_token(identity=student.id)

    return jsonify({'message': 'Login successful'}), 200


@jwt_required()
def joinClass():
    inputData = request.get_json()

    name_class = inputData.get('name')
    lounge = inputData.get('lounge')
    hour = inputData.get('hour')
    teacher = inputData.get('teacher')

    if not name_class or not lounge or not hour or not teacher:
        return jsonify({'message':'not data'})
    
    clase = Classes.query.filter_by(name_class=name_class, lounge=lounge, hour=hour, teacher=teacher)
    if not clase:
        return jsonify({'message':'not exits class'})
    
    current_user = get_jwt_identity()
    student = Students.query.get(current_user)
    
    if not student:
        return jsonify({'message':'Not exits student'})
    
    if clase in student.classes:
        return jsonify({'message':'Class exits'})
    
    student.classes.append(clase)
    db.session.commit()

    return jsonify({'message':'Add class successful'})
