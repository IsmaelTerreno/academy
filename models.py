from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


#  Domain Models related
# ##################################################################################
class Teacher(db.Model):
    id = db.Column(db.String, primary_key=True)
    name = db.Column(db.String(80), unique=False, nullable=False)
    last_name = db.Column(db.String(80), unique=False, nullable=False)
    creation_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return '<Teacher %r>' % self.name


class Student(db.Model):
    id = db.Column(db.String, primary_key=True)
    name = db.Column(db.String(80), unique=False, nullable=False)
    last_name = db.Column(db.String(80), unique=False, nullable=False)
    creation_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return '<Student %r>' % self.name


class StudentClassRegistration(db.Model):
    id = db.Column(db.String, primary_key=True)
    student_id = db.Column(db.String, db.ForeignKey('student.id'), nullable=False)
    classes_id = db.Column(db.String, db.ForeignKey('classes.id'), nullable=False)
    creation_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return '<StudentClassRegistration %r>' % self.name


class TeacherClassRegistration(db.Model):
    id = db.Column(db.String, primary_key=True)
    teacher_id = db.Column(db.String, db.ForeignKey('teacher.id'), nullable=False)
    classes_id = db.Column(db.String, db.ForeignKey('classes.id'), nullable=False)
    creation_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return '<StudentClassRegistration %r>' % self.name


class Classes(db.Model):
    id = db.Column(db.String, primary_key=True)
    name = db.Column(db.String(80), unique=False, nullable=False)
    creation_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return '<Classes %r>' % self.name


class StudentQuizRegistration(db.Model):
    id = db.Column(db.String, primary_key=True)
    student_id = db.Column(db.String, db.ForeignKey('student.id'), nullable=False)
    quiz_id = db.Column(db.String, db.ForeignKey('quiz.id'), nullable=False)
    creation_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return '<StudentQuizRegistration %r>' % self.name


class Quiz(db.Model):
    id = db.Column(db.String, primary_key=True)
    name = db.Column(db.String(80), unique=False, nullable=False)
    creation_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return '<Quiz %r>' % self.name


class QuestionQuizRegistration(db.Model):
    id = db.Column(db.String, primary_key=True)
    student_id = db.Column(db.String, db.ForeignKey('question.id'), nullable=False)
    quiz_id = db.Column(db.String, db.ForeignKey('quiz.id'), nullable=False)
    creation_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return '<QuestionQuizRegistration %r>' % self.name


class Question(db.Model):
    id = db.Column(db.String, primary_key=True)
    name = db.Column(db.String(80), unique=False, nullable=False)
    creation_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return '<Question %r>' % self.name


#  Database related
# ##################################################################################

def connect_app_db(app_to_connect):
    """Connect the database to app."""
    app_to_connect.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    postgres_config = {
        'user': 'postgres',
        'pw': 'mysecretpassword',
        'db': 'university',
        'host': 'localhost',
        'port': '5432',
    }
    app_to_connect.config[
        'SQLALCHEMY_DATABASE_URI'] = 'postgresql://%(user)s:%(pw)s@%(host)s:%(port)s/%(db)s' % postgres_config
    db.app = app_to_connect
    db.init_app(app_to_connect)
