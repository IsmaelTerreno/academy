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
        id_techer = str(json_response['id'])
        self.assertTrue(message.__eq__('New student created!'))
        self.assertFalse(id_techer.__eq__(''))

    def test_should_view_teacher_by_id(self):
        response = self.app.post('/teacher', data=json.dumps(dict(
            name='Dario Test',
            last_name='Hilton test'
        )), content_type='application/json', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        json_response = json.loads(response.get_data(as_text=True))
        message = str(json_response['message'])
        id_techer = str(json_response['id'])
        self.assertTrue(message.__eq__('New student created!'))
        self.assertFalse(id_techer.__eq__(''))


if __name__ == '__main__':
    unittest.main()
