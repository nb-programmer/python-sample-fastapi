import unittest

from fastapi import status

from .utils import get_test_client


class TestResourceHello(unittest.TestCase):
    def test_hello(self):
        """Tests the Hello World API"""
        with get_test_client() as client:
            res = client.get("/hello").raise_for_status()
            self.assertEqual(res.status_code, status.HTTP_200_OK)
            self.assertDictEqual(res.json(), {"message": "Hello, World!"})

    def test_greet_name(self):
        """Tests the greeting API (echo)"""
        with get_test_client() as client:
            with self.subTest("Generic name"):
                res = client.get("/hello/greet", params={"name": "TestClient"}).raise_for_status()
                self.assertEqual(res.status_code, status.HTTP_200_OK)
                self.assertDictEqual(res.json(), {"message": "Hello, TestClient!"})

            with self.subTest("Emoji"):
                res = client.get("/hello/greet", params={"name": "🚀 FastAPI"}).raise_for_status()
                self.assertEqual(res.status_code, status.HTTP_200_OK)
                self.assertDictEqual(res.json(), {"message": "Hello, 🚀 FastAPI!"})

            with self.subTest("Control Characters"):
                res = client.get("/hello/greet", params={"name": "John\tAdam\nDoe"}).raise_for_status()
                self.assertEqual(res.status_code, status.HTTP_200_OK)
                self.assertDictEqual(res.json(), {"message": "Hello, John\tAdam\nDoe!"})
