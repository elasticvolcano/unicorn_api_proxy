import os
import app
import unittest

class AppTestCase(unittest.TestCase):

    def setUp(self):
        app.app.config['TESTING'] = True
        self.app = app.app.test_client()

    def test_empty_get(self):
        rv = self.app.get('/')
        self.assertEqual(rv.status, '200 OK')

    def test_healthcheck(self):
        rv = self.app.get('/healthcheck')
        self.assertEqual(rv.status, '200 OK')

    def test_unicorns(self):
        rv = self.app.get('/unicorn')
        self.assertEqual(rv.status, '200 OK')

    def test_unicorn(self):
        rv = self.app.get('/unicorn/Buzzy')
        self.assertEqual(rv.status, '200 OK')


if __name__ == '__main__':
    unittest.main()
