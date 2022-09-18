
import time 

from django.test import TransactionTestCase, Client
from web.fib import tasks

class FooTaskTestCase(TransactionTestCase):

    def test__fib_api(self):
        client = Client()
        res = client.post('/api/fibonacci/', {'n': 1})
        data = res.json()

        self.assertEqual("pending", data["status"])
        
        time.sleep(5)

        # Re-do the API call and assert that there is now data that is being returned
        res = client.post('/api/fibonacci/', {'n': 1})
        data = res.json()
        print(data)
        
        self.assertTrue(data["nth"] is not None)
        self.assertTrue("success", data["status"])