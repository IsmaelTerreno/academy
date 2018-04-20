import unittest
import app_api
import json
from datetime import datetime


class AppTestCase(unittest.TestCase):
    APPLICATION_JSON_CONTENT_TYPE = 'application/json'

    def setUp(self):
        app_api.app.testing = True
        self.app = app_api.app.test_client()

    def test_index_api(self):
        rv = self.app.get('/')
        assert b'Welcome!' in rv.data

    def test_should_create_a_teacher(self):
        """ There are Teachers. """
        response = self.app.post('/teacher', data=json.dumps(dict(
            name='Dario Test',
            last_name='Hilton test'
        )), content_type=AppTestCase.APPLICATION_JSON_CONTENT_TYPE, follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        json_response = json.loads(response.get_data(as_text=True))
        message = str(json_response['message'])
        id_teacher = str(json_response['id'])
        self.assertTrue(message.__eq__('New teacher created!'))
        self.assertFalse(id_teacher.__eq__(''))
        print('Should create teacher.')
        print('')

    def test_should_view_teacher_by_id(self):
        """ There are Teachers that can be viewed. """
        response_create = self.app.post('/teacher', data=json.dumps(dict(
            name='Mark Test',
            last_name='Joker test'
        )), content_type=AppTestCase.APPLICATION_JSON_CONTENT_TYPE, follow_redirects=True)
        self.assertEqual(response_create.status_code, 200)
        json_response = json.loads(response_create.get_data(as_text=True))
        id_teacher = str(json_response['id'])
        response_view_by_id = self.app.get('/teacher/{}'.format(id_teacher), follow_redirects=True)
        json_response_view = json.loads(response_view_by_id.get_data(as_text=True))
        id_teacher_view = str(json_response_view['id'])
        self.assertTrue(id_teacher_view.__eq__(id_teacher))
        print('Should find teacher by id.')
        print('')

    def test_should_view_teacher_by_id_not_found(self):
        """ There are Teachers that can be not found. """
        id_teacher = 'no-existing-teacher'
        response_view_by_id = self.app.get('/teacher/{}'.format(id_teacher), follow_redirects=True)
        json_response_view = json.loads(response_view_by_id.get_data(as_text=True))
        message = str(json_response_view['message'])
        self.assertTrue(message.__eq__('No teacher found!'))
        print('Should not find teacher by id.')
        print('')

    def test_should_create_a_student(self):
        """ There are Students. """
        response = self.app.post('/student', data=json.dumps(dict(
            name='Marcelo Test',
            last_name='Gibson test'
        )), content_type=AppTestCase.APPLICATION_JSON_CONTENT_TYPE, follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        json_response = json.loads(response.get_data(as_text=True))
        message = str(json_response['message'])
        id_student = str(json_response['id'])
        self.assertTrue(message.__eq__('New student created!'))
        self.assertFalse(id_student.__eq__(''))
        print('Should create student.')
        print('')

    def test_should_view_student_by_id(self):
        """ There are Students that can be viewed. """
        response_create = self.app.post('/student', data=json.dumps(dict(
            name='Francis Test',
            last_name='Silva test'
        )), content_type=AppTestCase.APPLICATION_JSON_CONTENT_TYPE, follow_redirects=True)
        self.assertEqual(response_create.status_code, 200)
        json_response = json.loads(response_create.get_data(as_text=True))
        id_student = str(json_response['id'])
        response_view_by_id = self.app.get('/student/{}'.format(id_student), follow_redirects=True)
        json_response_view = json.loads(response_view_by_id.get_data(as_text=True))
        id_teacher_view = str(json_response_view['id'])
        self.assertTrue(id_teacher_view.__eq__(id_student))
        print('Should view student by id.')
        print('')

    def test_should_view_student_by_id_not_found(self):
        """ There are Students that can be not found. """
        id_student = 'no-existing-student'
        response_view_by_id = self.app.get('/student/{}'.format(id_student), follow_redirects=True)
        json_response_view = json.loads(response_view_by_id.get_data(as_text=True))
        message = str(json_response_view['message'])
        self.assertTrue(message.__eq__('No student found!'))
        print('Should not find student by id.')
        print('')

    def test_should_create_a_class(self):
        """ There are Classes. """
        response = self.app.post('/class', data=json.dumps(dict(
            name='Java and micro-services with spring',
        )), content_type=AppTestCase.APPLICATION_JSON_CONTENT_TYPE, follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        json_response = json.loads(response.get_data(as_text=True))
        message = str(json_response['message'])
        id_class = str(json_response['id'])
        self.assertTrue(message.__eq__('New Class created!'))
        self.assertFalse(id_class.__eq__(''))
        print('Should create a Class.')
        print('')

    def test_should_view_class_by_id(self):
        """ There are Classes that can be viewed. """
        response_create = self.app.post('/class', data=json.dumps(dict(
            name='SPA with Angular and React.js',
        )), content_type=AppTestCase.APPLICATION_JSON_CONTENT_TYPE, follow_redirects=True)
        self.assertEqual(response_create.status_code, 200)
        json_response = json.loads(response_create.get_data(as_text=True))
        id_class = str(json_response['id'])
        response_view_by_id = self.app.get('/class/{}'.format(id_class), follow_redirects=True)
        json_response_view = json.loads(response_view_by_id.get_data(as_text=True))
        id_class_view = str(json_response_view['id'])
        self.assertTrue(id_class_view.__eq__(id_class))
        print('Should view class by id.')
        print('')

    def test_should_view_class_by_id_not_found(self):
        """ There are Classes that can be not found. """
        id_class = 'no-existing-class'
        response_view_by_id = self.app.get('/class/{}'.format(id_class), follow_redirects=True)
        json_response_view = json.loads(response_view_by_id.get_data(as_text=True))
        message = str(json_response_view['message'])
        self.assertTrue(message.__eq__('No class found!'))
        print('Should not find class by id.')
        print('')

    def test_should_register_student_in_class(self):
        """ Students are in classes that teachers teach. """
        response_new_student = self.app.post('/student', data=json.dumps(dict(
            name='Federico Test',
            last_name='Klan test'
        )), content_type=AppTestCase.APPLICATION_JSON_CONTENT_TYPE, follow_redirects=True)
        self.assertEqual(response_new_student.status_code, 200)
        json_response_new_student = json.loads(response_new_student.get_data(as_text=True))
        student_id = str(json_response_new_student['id'])
        response_new_class = self.app.post('/class', data=json.dumps(dict(
            name='Javascript with React Native',
        )), content_type=AppTestCase.APPLICATION_JSON_CONTENT_TYPE, follow_redirects=True)
        self.assertEqual(response_new_class.status_code, 200)
        json_response = json.loads(response_new_class.get_data(as_text=True))
        classes_id = str(json_response['id'])
        response_registration = self.app.post('/class/student', data=json.dumps(dict(
            student_id=student_id,
            classes_id=classes_id
        )), content_type=AppTestCase.APPLICATION_JSON_CONTENT_TYPE, follow_redirects=True)
        self.assertEqual(response_registration.status_code, 200)
        json_response_registration = json.loads(response_registration.get_data(as_text=True))
        message = str(json_response_registration['message'])
        self.assertTrue(message.__eq__('Registered student in class!'))
        print('Should register student in class by id.')
        print('')

    def test_should_register_teacher_in_class(self):
        """ Students are in classes that teachers teach. """
        response_new_teacher = self.app.post('/teacher', data=json.dumps(dict(
            name='Martin Test',
            last_name='Manna test'
        )), content_type=AppTestCase.APPLICATION_JSON_CONTENT_TYPE, follow_redirects=True)
        self.assertEqual(response_new_teacher.status_code, 200)
        json_response_new_teacher = json.loads(response_new_teacher.get_data(as_text=True))
        teacher_id = str(json_response_new_teacher['id'])
        response_new_class = self.app.post('/class', data=json.dumps(dict(
            name='Swift with UI testing automated',
        )), content_type=AppTestCase.APPLICATION_JSON_CONTENT_TYPE, follow_redirects=True)
        self.assertEqual(response_new_class.status_code, 200)
        json_response_new_class = json.loads(response_new_class.get_data(as_text=True))
        classes_id = str(json_response_new_class['id'])
        response_registration = self.app.post('/class/teacher', data=json.dumps(dict(
            teacher_id=teacher_id,
            classes_id=classes_id
        )), content_type=AppTestCase.APPLICATION_JSON_CONTENT_TYPE, follow_redirects=True)
        self.assertEqual(response_registration.status_code, 200)
        json_response_registration = json.loads(response_registration.get_data(as_text=True))
        message = str(json_response_registration['message'])
        self.assertTrue(message.__eq__('Registered teacher in class!'))
        print('Should register teacher in class by id.')
        print('')

    def test_should_create_a_quiz(self):
        """Teachers can create multiple quizzes"""
        response = self.app.post('/quiz', data=json.dumps(dict(
            name='Machine Learning'
        )), content_type=AppTestCase.APPLICATION_JSON_CONTENT_TYPE, follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        json_response = json.loads(response.get_data(as_text=True))
        message = str(json_response['message'])
        id_teacher = str(json_response['id'])
        self.assertTrue(message.__eq__('New Quiz created!'))
        self.assertFalse(id_teacher.__eq__(''))
        print('Should create quiz.')
        print('')

    def test_should_create_a_question(self):
        """Teachers can create many questions each question is multiple choice"""
        response = self.app.post('/question', data=json.dumps(dict(
            description='Java has multiple inheritance?'
        )), content_type=AppTestCase.APPLICATION_JSON_CONTENT_TYPE, follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        json_response = json.loads(response.get_data(as_text=True))
        message = str(json_response['message'])
        id_question = str(json_response['id'])
        self.assertTrue(message.__eq__('New Question created!'))
        self.assertFalse(id_question.__eq__(''))
        print('Should create question.')
        print('')

    def test_should_create_a_answer(self):
        response = self.app.post('/answer', data=json.dumps(dict(
            description='Yes Python is dynamically typed'
        )), content_type=AppTestCase.APPLICATION_JSON_CONTENT_TYPE, follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        json_response = json.loads(response.get_data(as_text=True))
        message = str(json_response['message'])
        id_answer = str(json_response['id'])
        self.assertTrue(message.__eq__('New Answer created!'))
        self.assertFalse(id_answer.__eq__(''))
        print('Should create answer.')
        print('')

    def test_should_register_question_in_quiz(self):
        """Teachers can create multiple quizzes with many questions (each question is multiple choice)"""
        response_new_question = self.app.post('/question', data=json.dumps(dict(
            description='Java has multiple inheritance?'
        )), content_type=AppTestCase.APPLICATION_JSON_CONTENT_TYPE, follow_redirects=True)
        self.assertEqual(response_new_question.status_code, 200)
        json_response_new_question = json.loads(response_new_question.get_data(as_text=True))
        question_id = str(json_response_new_question['id'])
        response_new_quiz = self.app.post('/quiz', data=json.dumps(dict(
            name='OOP Programing paradigm'
        )), content_type=AppTestCase.APPLICATION_JSON_CONTENT_TYPE, follow_redirects=True)
        self.assertEqual(response_new_quiz.status_code, 200)
        json_response = json.loads(response_new_quiz.get_data(as_text=True))
        quiz_id = str(json_response['id'])
        response_registration = self.app.post('/quiz/question', data=json.dumps(dict(
            question_id=question_id,
            quiz_id=quiz_id
        )), content_type=AppTestCase.APPLICATION_JSON_CONTENT_TYPE, follow_redirects=True)
        self.assertEqual(response_registration.status_code, 200)
        json_response_registration = json.loads(response_registration.get_data(as_text=True))
        message = str(json_response_registration['message'])
        self.assertTrue(message.__eq__('Registered question in quiz!'))
        print('Should register question in quiz by id.')
        print('')

    def test_should_register_student_in_quiz(self):
        """ Teachers can assign quizzes to students """
        response_new_student = self.app.post('/student', data=json.dumps(dict(
            name='Arturo Test',
            last_name='Markes test'
        )), content_type=AppTestCase.APPLICATION_JSON_CONTENT_TYPE, follow_redirects=True)
        self.assertEqual(response_new_student.status_code, 200)
        json_response_new_student = json.loads(response_new_student.get_data(as_text=True))
        student_id = str(json_response_new_student['id'])
        response_new_quiz = self.app.post('/quiz', data=json.dumps(dict(
            name='FP Programing paradigm '
        )), content_type=AppTestCase.APPLICATION_JSON_CONTENT_TYPE, follow_redirects=True)
        self.assertEqual(response_new_quiz.status_code, 200)
        json_response = json.loads(response_new_quiz.get_data(as_text=True))
        quiz_id = str(json_response['id'])
        response_registration = self.app.post('/quiz/student', data=json.dumps(dict(
            student_id=student_id,
            quiz_id=quiz_id
        )), content_type=AppTestCase.APPLICATION_JSON_CONTENT_TYPE, follow_redirects=True)
        self.assertEqual(response_registration.status_code, 200)
        json_response_registration = json.loads(response_registration.get_data(as_text=True))
        message = str(json_response_registration['message'])
        self.assertTrue(message.__eq__('Registered student in quiz!'))
        print('Should register student in quiz by id.')
        print('')

    def test_should_register_student_answer_in_question(self):
        """ Students solve/answer questions to complete the quiz,
        but they don't have to complete it at once. (Partial submissions can be made)."""
        response_new_student = self.app.post('/student', data=json.dumps(dict(
            name='Esteban Test',
            last_name='Dakame test'
        )), content_type=AppTestCase.APPLICATION_JSON_CONTENT_TYPE, follow_redirects=True)
        self.assertEqual(response_new_student.status_code, 200)
        json_response_new_student = json.loads(response_new_student.get_data(as_text=True))
        student_id = str(json_response_new_student['id'])
        response_new_answer = self.app.post('/answer', data=json.dumps(dict(
            description='Red Green Refactor'
        )), content_type=AppTestCase.APPLICATION_JSON_CONTENT_TYPE, follow_redirects=True)
        self.assertEqual(response_new_answer.status_code, 200)
        json_response_new_answer = json.loads(response_new_answer.get_data(as_text=True))
        answer_id = str(json_response_new_answer['id'])
        response_registration = self.app.post('/student/answer', data=json.dumps(dict(
            student_id=student_id,
            answer_id=answer_id,
            response=True
        )), content_type=AppTestCase.APPLICATION_JSON_CONTENT_TYPE, follow_redirects=True)
        self.assertEqual(response_registration.status_code, 200)
        json_response_registration = json.loads(response_registration.get_data(as_text=True))
        message = str(json_response_registration['message'])
        self.assertTrue(message.__eq__('Registered student answer in question!'))
        print('Should register student answer in question by id.')
        print('')

    def test_should_register_answer_in_question(self):
        """ Teachers can assign answers to questions """
        response_new_question = self.app.post('/question', data=json.dumps(dict(
            description='Does Swift has tuples?'
        )), content_type=AppTestCase.APPLICATION_JSON_CONTENT_TYPE, follow_redirects=True)
        self.assertEqual(response_new_question.status_code, 200)
        json_response_new_question = json.loads(response_new_question.get_data(as_text=True))
        question_id = str(json_response_new_question['id'])
        response_new_answer = self.app.post('/answer', data=json.dumps(dict(
            description='Yes it has tuples.'
        )), content_type=AppTestCase.APPLICATION_JSON_CONTENT_TYPE, follow_redirects=True)
        self.assertEqual(response_new_answer.status_code, 200)
        json_response_new_answer = json.loads(response_new_answer.get_data(as_text=True))
        answer_id = str(json_response_new_answer['id'])
        response_registration = self.app.post('/question/answer', data=json.dumps(dict(
            question_id=question_id,
            answer_id=answer_id
        )), content_type=AppTestCase.APPLICATION_JSON_CONTENT_TYPE, follow_redirects=True)
        self.assertEqual(response_registration.status_code, 200)
        json_response_registration = json.loads(response_registration.get_data(as_text=True))
        message = str(json_response_registration['message'])
        self.assertTrue(message.__eq__('Registered answer in question!'))
        print('Should register answer in question by id.')
        print('')

    def test_should_register_grade_in_quiz(self):
        """ Quizzes need to get graded. """
        # Create a student.
        response_new_student = self.app.post('/student', data=json.dumps(dict(
            name='Mauro Test',
            last_name='Treat test'
        )), content_type=AppTestCase.APPLICATION_JSON_CONTENT_TYPE, follow_redirects=True)
        self.assertEqual(response_new_student.status_code, 200)
        json_response_new_student = json.loads(response_new_student.get_data(as_text=True))
        student_id = str(json_response_new_student['id'])
        # Create a teacher.
        response_new_teacher = self.app.post('/teacher', data=json.dumps(dict(
            name='Marcus Test',
            last_name='Platon test'
        )), content_type=AppTestCase.APPLICATION_JSON_CONTENT_TYPE, follow_redirects=True)
        self.assertEqual(response_new_teacher.status_code, 200)
        json_response_new_teacher = json.loads(response_new_teacher.get_data(as_text=True))
        teacher_id = str(json_response_new_teacher['id'])
        # Create a answer.
        response_new_answer = self.app.post('/answer', data=json.dumps(dict(
            description='Yes must be a TDD.'
        )), content_type=AppTestCase.APPLICATION_JSON_CONTENT_TYPE, follow_redirects=True)
        self.assertEqual(response_new_answer.status_code, 200)
        json_response_new_answer = json.loads(response_new_answer.get_data(as_text=True))
        answer_id = str(json_response_new_answer['id'])
        # Create a quiz.
        response_new_quiz = self.app.post('/quiz', data=json.dumps(dict(
            name='CI and CD for Quality and delivery'
        )), content_type=AppTestCase.APPLICATION_JSON_CONTENT_TYPE, follow_redirects=True)
        self.assertEqual(response_new_quiz.status_code, 200)
        json_response = json.loads(response_new_quiz.get_data(as_text=True))
        quiz_id = str(json_response['id'])
        # Register the student into quiz.
        response_registration = self.app.post('/quiz/student', data=json.dumps(dict(
            student_id=student_id,
            quiz_id=quiz_id
        )), content_type=AppTestCase.APPLICATION_JSON_CONTENT_TYPE, follow_redirects=True)
        self.assertEqual(response_registration.status_code, 200)
        json_response_registration = json.loads(response_registration.get_data(as_text=True))
        student_quiz_registration_id = str(json_response_registration['id'])
        # Register the student answer.
        response_registration_new_student_answer = self.app.post('/student/answer', data=json.dumps(dict(
            student_id=student_id,
            answer_id=answer_id,
            response=True
        )), content_type=AppTestCase.APPLICATION_JSON_CONTENT_TYPE, follow_redirects=True)
        self.assertEqual(response_registration_new_student_answer.status_code, 200)
        json_response_registration_new_student_answer = json.loads(
            response_registration_new_student_answer.get_data(as_text=True))
        # Register the teacher grade for student quiz.
        response_registration_new_teacher_grade = self.app.post('/student/quiz/grade', data=json.dumps(dict(
            student_quiz_registration_id=student_quiz_registration_id,
            teacher_id=teacher_id,
            score=6
        )), content_type=AppTestCase.APPLICATION_JSON_CONTENT_TYPE, follow_redirects=True)
        self.assertEqual(response_registration_new_teacher_grade.status_code, 200)
        json_response_registration_new_teacher_grade = json.loads(
            response_registration_new_teacher_grade.get_data(as_text=True))
        message = str(json_response_registration_new_teacher_grade['message'])
        self.assertTrue(message.__eq__('Registered teacher grade in quiz!'))
        print('Should register grade in answer by id.')
        print('')

    def test_should_calculate_semester_student_grade_by_teacher_classes(self):
        """ For each teacher, they can calculate each student's total
        grade accumulated over a semester for their classes. """
        # Create a student.
        response_new_student = self.app.post('/student', data=json.dumps(dict(
            name='Markus Test',
            last_name='Atom test'
        )), content_type=AppTestCase.APPLICATION_JSON_CONTENT_TYPE, follow_redirects=True)
        self.assertEqual(response_new_student.status_code, 200)
        json_response_new_student = json.loads(response_new_student.get_data(as_text=True))
        student_id = str(json_response_new_student['id'])
        # Create a teacher.
        response_new_teacher = self.app.post('/teacher', data=json.dumps(dict(
            name='Benny Test',
            last_name='Chuck test'
        )), content_type=AppTestCase.APPLICATION_JSON_CONTENT_TYPE, follow_redirects=True)
        self.assertEqual(response_new_teacher.status_code, 200)
        json_response_new_teacher = json.loads(response_new_teacher.get_data(as_text=True))
        teacher_id = str(json_response_new_teacher['id'])
        # Create a quiz.
        response_new_quiz = self.app.post('/quiz', data=json.dumps(dict(
            name='Cloud Native With Kubernetes.'
        )), content_type=AppTestCase.APPLICATION_JSON_CONTENT_TYPE, follow_redirects=True)
        self.assertEqual(response_new_quiz.status_code, 200)
        json_response_new_quiz = json.loads(response_new_quiz.get_data(as_text=True))
        quiz_id = str(json_response_new_quiz['id'])
        # Register the student into quiz.
        response_registration_new_student_quiz = self.app.post('/quiz/student', data=json.dumps(dict(
            student_id=student_id,
            quiz_id=quiz_id,
            response=True
        )), content_type=AppTestCase.APPLICATION_JSON_CONTENT_TYPE, follow_redirects=True)
        self.assertEqual(response_registration_new_student_quiz.status_code, 200)
        json_response_registration_new_student_quiz = json.loads(
            response_registration_new_student_quiz.get_data(as_text=True))
        student_quiz_registration_id = str(json_response_registration_new_student_quiz['id'])
        # Register the teacher grade for student quiz.
        response_registration_new_teacher_grade = self.app.post('/student/quiz/grade', data=json.dumps(dict(
            student_quiz_registration_id=student_quiz_registration_id,
            teacher_id=teacher_id,
            score=6
        )), content_type=AppTestCase.APPLICATION_JSON_CONTENT_TYPE, follow_redirects=True)
        self.assertEqual(response_registration_new_teacher_grade.status_code, 200)
        json_response_registration_new_teacher_grade = json.loads(
            response_registration_new_teacher_grade.get_data(as_text=True))
        message = str(json_response_registration_new_teacher_grade['message'])
        self.assertTrue(message.__eq__('Registered teacher grade in quiz!'))
        # Check the grade accumulated over a semester for their classes.
        current_semester_number_to_ask = 1 if (datetime.now().month <= 6) else 2
        response_semester_student_grade = self.app.get(
            '/teacher/{}/student/{}/semester/{}/grade'.format(teacher_id, student_id, current_semester_number_to_ask),
            follow_redirects=True)
        json_response_view = json.loads(response_semester_student_grade.get_data(as_text=True))
        message_grade = str(json_response_view['message'])
        student_name = str(json_response_view['name'])
        last_name = str(json_response_view['last_name'])
        grade_accumulated = int(json_response_view['grade_accumulated'])
        self.assertTrue(message_grade.__eq__('Result found for student!'))
        self.assertTrue(student_name.__eq__('Markus Test'))
        self.assertTrue(last_name.__eq__('Atom test'))
        self.assertTrue(grade_accumulated.__eq__(6))
        print('Should calculate student grade in semester by teacher classes.')
        print('')


if __name__ == '__main__':
    unittest.main()
