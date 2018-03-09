from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from uuid import uuid4

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
        return '<TeacherClassRegistration %r>' % self.name


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
    name = db.Column(db.String(150), unique=False, nullable=False)
    creation_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return '<Quiz %r>' % self.name


class QuestionQuizRegistration(db.Model):
    id = db.Column(db.String, primary_key=True)
    question_id = db.Column(db.String, db.ForeignKey('question.id'), nullable=False)
    quiz_id = db.Column(db.String, db.ForeignKey('quiz.id'), nullable=False)
    creation_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return '<QuestionQuizRegistration %r>' % self.name


class Question(db.Model):
    id = db.Column(db.String, primary_key=True)
    description = db.Column(db.String(500), unique=False, nullable=False)
    creation_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return '<Question %r>' % self.name


class QuestionAnswerRegistration(db.Model):
    id = db.Column(db.String, primary_key=True)
    question_id = db.Column(db.String, db.ForeignKey('question.id'), nullable=False)
    answer_id = db.Column(db.String, db.ForeignKey('answer.id'), nullable=False)
    creation_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return '<QuestionQuizRegistration %r>' % self.name


class Answer(db.Model):
    id = db.Column(db.String, primary_key=True)
    description = db.Column(db.String(250), unique=False, nullable=False)
    creation_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return '<Answer %r>' % self.name


class StudentAnswerQuestionQuizRegistration(db.Model):
    id = db.Column(db.String, primary_key=True)
    student_id = db.Column(db.String, db.ForeignKey('student.id'), nullable=False)
    answer_id = db.Column(db.String, db.ForeignKey('answer.id'), nullable=False)
    question_id = db.Column(db.String, db.ForeignKey('question.id'), nullable=False)
    quiz_id = db.Column(db.String, db.ForeignKey('quiz.id'), nullable=False)
    creation_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return '<QuestionQuizRegistration %r>' % self.name


#  Database related
# ##################################################################################

def connect_app_db(app_to_connect):
    """Connect the database to app."""
    app_to_connect.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    postgres_config = {
        'user': 'postgres',
        'pw': 'mysecretpassword',
        'db': 'postgres',
        'host': 'localhost',
        'port': '5432',
    }
    if app_to_connect.testing is True:
        postgres_config = {
            'user': 'postgres',
            'pw': 'mysecretpassword',
            'db': 'postgres_testing',
            'host': 'localhost',
            'port': '5432',
        }
    app_to_connect.config[
        'SQLALCHEMY_DATABASE_URI'] = 'postgresql://%(user)s:%(pw)s@%(host)s:%(port)s/%(db)s' % postgres_config
    db.app = app_to_connect
    db.init_app(app_to_connect)


def load_sample_test_data():
    teacher_1 = Teacher(id=uuid4(), name='ismael', last_name='terreno')
    teacher_2 = Teacher(id=uuid4(), name='clau', last_name='silva')
    admin = Student(id=uuid4(), name='logan', last_name='silva')
    guest = Student(id=uuid4(), name='banner', last_name='silva')
    db.session.add(admin)
    db.session.add(guest)
    db.session.add(teacher_1)
    db.session.add(teacher_2)
    db.session.commit()
