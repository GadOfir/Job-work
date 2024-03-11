import unittest
import requests
from collections import OrderedDict

class BaseTest(unittest.TestCase):
    default_params = OrderedDict([
        ('h_width', 6),
        ('h_length', 12),
        ('grip_type', 'FINGERTIP'),
        ('leniency', 0),
        ('wireless', 'false'),
        ('lefthanded', 'false'),
        ('buttons', -1),
        ('shape', 'both')
    ])

    def setUp(self):
        self.base_url = 'https://www.rocketjumpninja.com/api/search/mice'

    def _send_request(self, params):
        # Define the order of parameters in the URL
        param_order = ['h_width', 'h_length', 'grip_type', 'leniency', 'wireless', 'lefthanded', 'buttons', 'shape']

        # Construct the URL with parameters in the desired order
        url = self.base_url + '?' + '&'.join([f"{k}={params[k]}" for k in param_order if k in params])

        print("Request URL:", url)  # Print complete request URL with parameters
        response = requests.get(url)
        return response.json()  # Return the JSON response directly

    def send_test_request(self, params=None):
        # Method to send a request with provided parameters or default parameters if none are provided
        if params is None:
            params = self.default_params
        return self._send_request(params)

if __name__ == '__main__':
    unittest.main()
