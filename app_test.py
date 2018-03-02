import unittest


class AppTestCase(unittest.TestCase):

    def test_config_db(self):
        print('first test')
        self.assertEqual(True, True)


if __name__ == '__main__':
    unittest.main()
