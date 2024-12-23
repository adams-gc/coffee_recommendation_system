import unittest
from app import app  # Replace 'your_app' with the actual name of your Flask app module

class CoffeeRecommendationTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.client = app.test_client()

    def test_recommendation_with_all_valid_inputs(self):
        response = self.client.post('/recommend', data={
            'flavor': 'Fruity',
            'roast_level': 'Light',
            'acidity': 'Medium',
            'drink_type': 'Drip',
            'drink_time': 'Morning',
            'strength': 'Mild'
        })
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'<title>Coffee Recommendation Result</title>', response.data)

    def test_recommendation_boundary_values(self):
        response = self.client.post('/recommend', data={
            'flavor': 'Chocolatey',
            'roast_level': 'Dark',
            'acidity': 'Low',
            'drink_type': 'Espresso',
            'drink_time': 'Evening',
            'strength': 'Strong'
        })
        self.assertEqual(response.status_code, 200)
        print(response.data)# temporarily added for debugging
        self.assertIn(b'Chocolatey', response.data)

    def test_recommendation_with_missing_optional_input(self):
        response = self.client.post('/recommend', data={
            'flavor': 'Nutty',
            'roast_level': 'Medium',
            'acidity': 'High',
            'drink_type': 'Aeropress'
            # Missing 'drink_time' and 'strength'
        })
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Nutty', response.data)

    def test_recommendation_invalid_data_types(self):
        response = self.client.post('/recommend', data={
            'flavor': 123,  # Invalid type, should be a string
            'roast_level': 'Medium',
            'acidity': 'Low',
            'drink_type': 'Drip',
            'drink_time': 'Morning',
            'strength': 'Mild'
        })
        self.assertEqual(response.status_code, 400)
        self.assertIn(b'Invalid input type', response.data)

    def test_feedback_submission(self):
        response = self.client.post('/feedback', data={
            'recommendation_id': 1,
            'user_feedback': 'Loved it!'
        })
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Thank you for your feedback', response.data)

    def test_invalid_recommendation_id(self):
        response = self.client.get('/recommend/9999')  # Assuming 9999 is a non-existent ID
        self.assertEqual(response.status_code, 404)
        self.assertIn(b'Recommendation not found', response.data)

    def test_multiple_requests(self):
        for i in range(10):  # Adjust range for desired load
            response = self.client.post('/recommend', data={
                'flavor': 'Fruity',
                'roast_level': 'Light',
                'acidity': 'Medium',
                'drink_type': 'Drip',
                'drink_time': 'Morning',
                'strength': 'Mild'
            })
            self.assertEqual(response.status_code, 200)
            self.assertIn(b'Fruity', response.data)

if __name__ == "__main__":
    unittest.main()
