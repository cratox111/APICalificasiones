from app import db

class Classes(db.Model):
    __tablename__ = 'classes'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    lounge = db.Column(db.String(10), nullable=False)
    hour = db.Column(db.String(10), nullable=False)
    max_students = db.Column(db.Integer, nullable=False)
    num_students = db.Column(db.Integer, nullable=False)
    teacher = db.Column(db.String(100), nullable=False)

    student_id = db.Column(db.Integer, db.ForeignKey('students.id'), nullable=False)
    teacher_id = db.Column(db.Integer, db.ForeignKey('teachers.id'), nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'lounge': self.lounge,
            'hour': self.hour,
            'max_students': self.max_students,
            'num_students': self.num_students,
            'teacher': self.teacher,
            'student_id': self.student_id
        }