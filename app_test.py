import unittest
import app_api


class AppTestCase(unittest.TestCase):

    def setUp(self):
        self.app = app_api.app.test_client()

    def test_config_db(self):
        self.assertEqual(True, True)

    def test_empty_db(self):
        rv = self.app.get('/')
        print(rv.data)
        assert b'Welcome!' in rv.data


if __name__ == '__main__':
    unittest.main()
