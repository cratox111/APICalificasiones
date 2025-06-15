from app import db

class Students(db.Model):
    __tablename__ = 'students'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    password = db.Column(db.String(100), nullable=False)
    semester = db.Column(db.String(100), nullable=False)

    classes = db.relationship('Classes', backref='student', lazy=True)