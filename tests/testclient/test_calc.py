import unittest

from fastapi import status

from .utils import get_test_client


class TestResourceCalcConverter(unittest.TestCase):
    def test_dec2hex(self):
        """Tests the Dec2Hex API"""
        with get_test_client() as client:
            with self.subTest("Zero"):
                res = client.post("/calculator/convert/dec2hex", params={"value": 0}).raise_for_status()
                self.assertEqual(res.status_code, status.HTTP_200_OK)
                self.assertDictEqual(res.json(), {"value": "0x0"})

            with self.subTest("Positive"):
                res = client.post("/calculator/convert/dec2hex", params={"value": 255}).raise_for_status()
                self.assertEqual(res.status_code, status.HTTP_200_OK)
                self.assertDictEqual(res.json(), {"value": "0xff"})

            with self.subTest("Negative"):
                res = client.post("/calculator/convert/dec2hex", params={"value": -64}).raise_for_status()
                self.assertEqual(res.status_code, status.HTTP_200_OK)
                self.assertDictEqual(res.json(), {"value": "-0x40"})

    def test_hex2dec(self):
        """Tests the Hex2Dec API"""
        with get_test_client() as client:
            with self.subTest("Zero"):
                res = client.post("/calculator/convert/hex2dec", params={"value": "0x0"}).raise_for_status()
                self.assertEqual(res.status_code, status.HTTP_200_OK)
                self.assertDictEqual(res.json(), {"value": 0})

            with self.subTest("Positive"):
                res = client.post("/calculator/convert/hex2dec", params={"value": "0xff"}).raise_for_status()
                self.assertEqual(res.status_code, status.HTTP_200_OK)
                self.assertDictEqual(res.json(), {"value": 255})

            with self.subTest("Negative"):
                res = client.post("/calculator/convert/hex2dec", params={"value": "-0x40"}).raise_for_status()
                self.assertEqual(res.status_code, status.HTTP_200_OK)
                self.assertDictEqual(res.json(), {"value": -64})
