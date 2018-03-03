from flask import Flask, jsonify, request
from uuid import uuid4
from models import Teacher, Student, connect_app_db, db, load_sample_test_data

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
    load_sample_test_data()
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
        teacher_data = {
            'id': student.id,
            'name': student.name
        }
        output.append(teacher_data)
    return jsonify(output)


if __name__ == "__main__":
    app.run()
