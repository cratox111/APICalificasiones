from flask import jsonify, request
from app import db
from werkzeug.security import generate_password_hash, check_password_hash
from app.models.Students import Students

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

    return jsonify({'message': 'Login successful'}), 200
    