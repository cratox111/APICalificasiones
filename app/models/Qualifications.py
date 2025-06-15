from app import db

class Qualifications(db.Model):
    __tablename__ = 'qualifications'

    id = db.Column(db.Integer, primary_key=True)
    qualification = db.Column(db.Intiger)

    