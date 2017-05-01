import unittest
from Application import *

class test_username(unittest.TestCase):
    def test_username_correct(self):
        self.assertTrue(check_username('Luke'))

    def test_username_incorrect(self):
        self.assertFalse(check_username('blah'))

class test_password(unittest.TestCase):
    def test_password_correct(self):
        self.assertTrue(check_password('password1234'))

    def test_password_incorrect(self):
        self.assertFalse(check_password('password1235'))

class test_database(unittest.TestCase):
    def test_connection(self):
        #self.assertEqual(connect_to_mongo('0.0.0.0', 32769), MongoClient('0.0.0.0', 32769))
        print('Test DB connection true')

    def test_connection_false(self):
        #self.assertEqual(connect_to_mongo('0.0.0.0', 12345), MongoClient('0.0.0.0', 12345))
        print('Test DB connection False')


if __name__ == '__main__':
    unittest.main()


