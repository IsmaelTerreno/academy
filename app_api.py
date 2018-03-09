from flask import Flask, jsonify, request
from uuid import uuid4
from models import Teacher, \
    Student, \
    Classes, \
    StudentClassRegistration, \
    TeacherClassRegistration, \
    Quiz, \
    Question, \
    Answer, \
    QuestionQuizRegistration, \
    StudentQuizRegistration, \
    connect_app_db, \
    db

app = Flask(__name__)
app.config['DEBUG'] = True
# Connect app to db.
connect_app_db(app)
# Later create the structure for domain models.
db.create_all()


#  Routes for the API
# ##################################################################################
@app.route("/")
def index():
    return "Welcome!"


@app.route("/teacher", methods=['POST'])
def create_teacher():
    """ Create a teacher """
    data = request.get_json()
    new_id = uuid4()
    new_teacher = Teacher(id=new_id, name=data['name'], last_name=data['last_name'])
    db.session.add(new_teacher)
    db.session.commit()
    return jsonify({
        'message': 'New teacher created!',
        'id': new_id
    })


@app.route("/teacher/<teacher_id>", methods=['GET'])
def view_teacher(teacher_id):
    """ View a particular teacher """
    teacher = Teacher.query.filter_by(id=teacher_id).first()
    if not teacher:
        return jsonify({'message': 'No teacher found!'})
    return jsonify({
        'id': teacher.id,
        'name': teacher.name,
        'last_name': teacher.last_name
    })


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
    new_id = uuid4()
    new_student = Student(id=new_id, name=data['name'], last_name=data['last_name'])
    db.session.add(new_student)
    db.session.commit()
    return jsonify({
        'message': 'New student created!',
        'id': new_id
    })


@app.route("/student/<student_id>", methods=['GET'])
def view_student(student_id):
    """ View a particular student """
    student = Student.query.filter_by(id=student_id).first()
    if not student:
        return jsonify({'message': 'No student found!'})
    return jsonify({
        'id': student.id,
        'name': student.name,
        'last_name': student.last_name
    })


@app.route("/student/all", methods=['GET'])
def view_all_students():
    """ View all students """
    students = Student.query.all()
    output = []
    for student in students:
        student_data = {
            'id': student.id,
            'name': student.name
        }
        output.append(student_data)
    return jsonify(output)


@app.route("/class", methods=['POST'])
def create_class():
    """ Create a class """
    data = request.get_json()
    new_id = uuid4()
    new_class = Classes(id=new_id, name=data['name'])
    db.session.add(new_class)
    db.session.commit()
    return jsonify({
        'message': 'New Class created!',
        'id': new_id
    })


@app.route("/class/<class_id>", methods=['GET'])
def view_class(class_id):
    """ View a particular class """
    class_view = Classes.query.filter_by(id=class_id).first()
    if not class_view:
        return jsonify({'message': 'No class found!'})
    return jsonify({
        'id': class_view.id,
        'name': class_view.name
    })


@app.route("/class/student", methods=['POST'])
def register_student_in_class():
    """ Register a student in a existing class """
    data = request.get_json()
    new_id = uuid4()
    student_class_registration = StudentClassRegistration(id=new_id,
                                                          student_id=data['student_id'],
                                                          classes_id=data['classes_id']
                                                          )
    db.session.add(student_class_registration)
    db.session.commit()
    return jsonify({
        'message': 'Registered student in class!',
        'id': new_id
    })


@app.route("/class/teacher", methods=['POST'])
def register_teacher_in_class():
    """ Register a teacher in a existing class """
    data = request.get_json()
    new_id = uuid4()
    teacher_class_registration = TeacherClassRegistration(id=new_id,
                                                          teacher_id=data['teacher_id'],
                                                          classes_id=data['classes_id']
                                                          )
    db.session.add(teacher_class_registration)
    db.session.commit()
    return jsonify({
        'message': 'Registered teacher in class!',
        'id': new_id
    })


@app.route("/quiz", methods=['POST'])
def create_quiz():
    """ Create a Quiz """
    data = request.get_json()
    new_id = uuid4()
    new_quiz = Quiz(id=new_id, name=data['name'])
    db.session.add(new_quiz)
    db.session.commit()
    return jsonify({
        'message': 'New Quiz created!',
        'id': new_id
    })


@app.route("/quiz/question", methods=['POST'])
def register_question_in_quiz():
    """ Register a question in a existing quiz """
    data = request.get_json()
    new_id = uuid4()
    question_quiz_registration = QuestionQuizRegistration(id=new_id,
                                                          question_id=data['question_id'],
                                                          quiz_id=data['quiz_id']
                                                          )
    db.session.add(question_quiz_registration)
    db.session.commit()
    return jsonify({
        'message': 'Registered question in quiz!',
        'id': new_id
    })


@app.route("/quiz/student", methods=['POST'])
def register_student_in_quiz():
    """ Register a question in a existing quiz """
    data = request.get_json()
    new_id = uuid4()
    student_quiz_registration = StudentQuizRegistration(id=new_id,
                                                        student_id=data['student_id'],
                                                        quiz_id=data['quiz_id']
                                                        )
    db.session.add(student_quiz_registration)
    db.session.commit()
    return jsonify({
        'message': 'Registered student in quiz!',
        'id': new_id
    })


@app.route("/question", methods=['POST'])
def create_question():
    """ Create a Question """
    data = request.get_json()
    new_id = uuid4()
    new_question = Question(id=new_id, description=data['description'])
    db.session.add(new_question)
    db.session.commit()
    return jsonify({
        'message': 'New Question created!',
        'id': new_id
    })


@app.route("/answer", methods=['POST'])
def create_answer():
    """ Create a Answer """
    data = request.get_json()
    new_id = uuid4()
    new_answer = Answer(id=new_id, description=data['description'])
    db.session.add(new_answer)
    db.session.commit()
    return jsonify({
        'message': 'New Answer created!',
        'id': new_id
    })


if __name__ == "__main__":
    app.run()
