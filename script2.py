import unittest
from app import app

class FlaskAppTest(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_predict(self):
        response = self.app.post('/predict', json={'x1': 3, 'x2': 4})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json()['decision'], 'Low')

    def test_predict_high(self):
        response = self.app.post('/predict', json={'x1': 8, 'x2': 5})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json()['decision'], 'High')

if __name__ == '__main__':
    unittest.main()
