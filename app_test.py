import unittest
import app_api
import json


class AppTestCase(unittest.TestCase):

    APPLICATION_JSON_CONTENT_TYPE = 'application/json'

    def setUp(self):
        self.app = app_api.app.test_client()

    def test_index_api(self):
        rv = self.app.get('/')
        assert b'Welcome!' in rv.data

    def test_should_create_a_teacher(self):
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
        id_teacher = 'no-existing-teacher'
        response_view_by_id = self.app.get('/teacher/{}'.format(id_teacher), follow_redirects=True)
        json_response_view = json.loads(response_view_by_id.get_data(as_text=True))
        message = str(json_response_view['message'])
        self.assertTrue(message.__eq__('No teacher found!'))
        print('Should not find teacher by id.')
        print('')

    def test_should_create_a_student(self):
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
        id_student = 'no-existing-student'
        response_view_by_id = self.app.get('/student/{}'.format(id_student), follow_redirects=True)
        json_response_view = json.loads(response_view_by_id.get_data(as_text=True))
        message = str(json_response_view['message'])
        self.assertTrue(message.__eq__('No student found!'))
        print('Should not find student by id.')
        print('')

    def test_should_create_a_class(self):
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
        id_class = 'no-existing-class'
        response_view_by_id = self.app.get('/class/{}'.format(id_class), follow_redirects=True)
        json_response_view = json.loads(response_view_by_id.get_data(as_text=True))
        message = str(json_response_view['message'])
        self.assertTrue(message.__eq__('No class found!'))
        print('Should not find class by id.')
        print('')

    def test_should_register_student_in_class(self):
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
            description='Does Python is dynamically typed?'
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


if __name__ == '__main__':
    unittest.main()
