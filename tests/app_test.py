import unittest
import pytest
from app import app


class BasicTests(unittest.TestCase):

    # executed prior to each test
    def setUp(self):
        app.config['TESTING'] = True
        self.app = app.test_client()

    def tearDown(self):
        pass

    def test_application_root(self):
        """check that the application root is responding"""
        response = self.app.get('/', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'welcome to smart steel application', response.data)        

    def test_task_data(self):
        """check that the task data get method is response should be 200"""
        response = self.app.get('/taskdata', follow_redirects=True)
        self.assertEqual(response.status_code, 200)   

    def test_log_data(self):
        """check that the log data get method is response should be 200"""
        response = self.app.get('/logs', follow_redirects=True)
        self.assertEqual(response.status_code, 200)      

    def test_invalid_url(self):
        """check that the response for invalid URL should be 404"""
        response = self.app.get('/invalidurl', follow_redirects=True)
        self.assertEqual(response.status_code, 404)

    def test_internal_server_error(self):
        """check that the response for internal server error should be 500"""
        with pytest.raises(Exception):
            response = self.app.get('/taskdata', follow_redirects=True)
            self.assertEqual(response.status_code, 500)
            


if __name__ == "__main__":
    unittest.main()