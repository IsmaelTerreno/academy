import unittest
import app_api
import json


class AppTestCase(unittest.TestCase):

    def setUp(self):
        self.app = app_api.app.test_client()

    def test_index_api(self):
        rv = self.app.get('/')
        assert b'Welcome!' in rv.data

    def test_should_create_a_teacher(self):
        response = self.app.post('/teacher', data=json.dumps(dict(
            name='Dario Test',
            last_name='Hilton test'
        )), content_type='application/json', follow_redirects=True)
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
        )), content_type='application/json', follow_redirects=True)
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
        )), content_type='application/json', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        json_response = json.loads(response.get_data(as_text=True))
        message = str(json_response['message'])
        id_teacher = str(json_response['id'])
        self.assertTrue(message.__eq__('New student created!'))
        self.assertFalse(id_teacher.__eq__(''))
        print('Should create student.')
        print('')

    def test_should_view_student_by_id(self):
        response_create = self.app.post('/student', data=json.dumps(dict(
            name='Francis Test',
            last_name='Silva test'
        )), content_type='application/json', follow_redirects=True)
        self.assertEqual(response_create.status_code, 200)
        json_response = json.loads(response_create.get_data(as_text=True))
        id_student = str(json_response['id'])
        response_view_by_id = self.app.get('/student/{}'.format(id_student), follow_redirects=True)
        json_response_view = json.loads(response_view_by_id.get_data(as_text=True))
        id_teacher_view = str(json_response_view['id'])
        self.assertTrue(id_teacher_view.__eq__(id_student))
        print('Should find student by id.')
        print('')

    def test_should_view_student_by_id_not_found(self):
        id_student = 'no-existing-student'
        response_view_by_id = self.app.get('/student/{}'.format(id_student), follow_redirects=True)
        json_response_view = json.loads(response_view_by_id.get_data(as_text=True))
        message = str(json_response_view['message'])
        self.assertTrue(message.__eq__('No student found!'))
        print('Should not find student by id.')
        print('')


if __name__ == '__main__':
    unittest.main()
