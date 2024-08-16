import unittest


class TestSampleApp(unittest.TestCase):
    def test_app_initializes(self):
        from fastapi import FastAPI

        from sample_fastapi.app.app_factory import init_app

        # Create application
        app = init_app()

        self.assertTrue(isinstance(app, FastAPI))

    def test_app_testclient_connects(self):
        from fastapi.testclient import TestClient

        from sample_fastapi.app.app_factory import init_app

        # Create application
        app = init_app()

        # Create test client
        with TestClient(app) as client:
            # Test if it is able to make requests
            client.get("/")
