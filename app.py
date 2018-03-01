from flask import Flask, jsonify, request
from uuid import uuid4
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['DEBUG'] = True

#  Database related
# ##################################################################################
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
POSTGRES = {
    'user': 'postgres',
    'pw': 'mysecretpassword',
    'db': 'university',
    'host': 'localhost',
    'port': '5432',
}
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://%(user)s:%(pw)s@%(host)s:%(port)s/%(db)s' % POSTGRES
db = SQLAlchemy(app)


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


@app.route("/")
def index():
    teacher_1 = Teacher(id=uuid4(), name='ismael', last_name='terreno')
    teacher_2 = Teacher(id=uuid4(), name='clau', last_name='silva')
    admin = Student(id=uuid4(), name='logan', last_name='silva')
    guest = Student(id=uuid4(), name='banner', last_name='silva')
    db.session.add(admin)
    db.session.add(guest)
    db.session.add(teacher_1)
    db.session.add(teacher_2)
    db.session.commit()
    return "Welcome!"


db.create_all()


@app.route("/teacher", methods=['POST'])
def create_teacher():
    """ Create a teacher """
    data = request.get_json()
    new_teacher = Teacher(id=uuid4(), name=data['name'], last_name=data['last_name'])
    db.session.add(new_teacher)
    db.session.commit()
    return jsonify({'message': 'New teacher created!'})


@app.route("/teacher/<teacher_id>", methods=['GET'])
def view_teacher(teacher_id):
    """ View a particular teacher """
    return teacher_id


@app.route("/teacher/all", methods=['GET'])
def view_all_teachers():
    """ View all teachers """
    teachers = Teacher.query.all()
    output = []
    for teacher in teachers:
        teacher_data = {
            'id': teacher.id,
            'name': teacher.name
        }
        output.append(teacher_data)
    return jsonify(output)


@app.route("/student", methods=['POST'])
def create_student():
    """ Create a student """
    data = request.get_json()
    new_student = Student(id=uuid4(), name=data['name'], last_name=data['last_name'])
    db.session.add(new_student)
    db.session.commit()
    return jsonify({'message': 'New student created!'})


@app.route("/student/<student_id>", methods=['GET'])
def view_student(student_id):
    """ View a particular student """
    student = Student.query.filter_by(id=student_id).first()
    if not student:
        return jsonify({'message': 'No student found!'})

    student_data = {'public_id': student.id, 'name': student.name}
    return jsonify(student_data)


@app.route("/student/all", methods=['GET'])
def view_all_students():
    """ View all students """
    students = Student.query.all()
    output = []
    for student in students:
        teacher_data = {
            'id': student.id,
            'name': student.name
        }
        output.append(teacher_data)
    return jsonify(output)


if __name__ == "__main__":
    app.run()
