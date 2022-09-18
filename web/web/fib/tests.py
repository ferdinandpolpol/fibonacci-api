
import time 

from django.test import TransactionTestCase, Client, override_settings
from web.fib import tasks


@override_settings(
    task_eager_propagates=True,
    task_always_eager=True,
    broker_url='memory://',
    backend='memory'
)
class FibonacciAPIViewTestCase(TransactionTestCase):
    url = '/api/fibonacci/'

    def setUp(self):
        super().setUp()

        self.client = Client()

    def test__fib_api_post(self):
        """ Test that the POST API endpoint is working """
        res = self.client.post(self.url, {'n': 1})

        self.assertEqual(res.status_code, 200)

    def test__fib_api(self):
        """ Test that pending data will work """
        res = self.client.post(self.url, {'n': 10})
        data = res.json()

        self.assertEqual("pending", data["status"])

        # Re-do the API call and assert that there is now data that is being returned
        res = self.client.post(self.url, {'n': 10})
        data = res.json()
        
        self.assertTrue(data["nth"] is not None)
        self.assertTrue("success", data["status"])

    def test__fib_api(self):
        """ Assert that the first 10 sequence of the fib is correct """
        res = self.client.post(self.url, {'n': 10})

        # Assert known sequence
        known_sequence = [0,1,1,2,3,5,8,13,21,34]
        for i in range(0, 10):
            res = self.client.post(self.url, {'n': i})
            data = res.json()
            
            self.assertEqual(known_sequence[i], int(data["nth"]))
