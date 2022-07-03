from cgitb import html
import unittest
import os
from urllib import response

from sqlalchemy import null
os.environ['TESTING'] = 'true'

from app import app

class AppTestCase(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()
    
    def test_home(self):
        response = self.client.get('/')
        assert response.status_code == 200
        html = response.get_data(as_text=True)
        assert "<h3>David Lázaro</h3>" in html
        # TODO Add more tests relating to the home page
        assert "+ About Us" in html
        assert "Our Hobbies" in html
        assert "Places" in html
    
    def test_timeline(self):
        response = self.client.get("/api/timeline_post")
        assert response.status_code == 200
        assert response.is_json
        json = response.get_json()
        assert "timeline_post" in json
        assert len(json["timeline_post"]) == 0

    # Test Driven Development -> write some tests on error or edge cases
    def test_malformed_timeline_post(self):
        # POST request missing name
        response = self.client.post("/api/timeline_post", data=
        {"email": "kristen@example.com", "content": "Hello World, I'm Kristen!"})
        assert response.status_code == 400
        html = response.get_data(as_text=True)
        assert "Invalid name" in html

        # POST request with empty content
        response = self.client.post("/api/timeline_post", data=
        {"name": "Kristen Zhang", "email": "kristen@example.com", "content": ""})
        assert response.status_code == 400
        html = response.get_data(as_text=True)
        assert "Invalid content" in html

        # POST request with malformed email
        response = self.client.post("/api/timeline_post", data=
        {"name": "Kristen Zhang", "email": "not-an-email", "content": "Hello"})
        assert response.status_code == 400
        html = response.get_data(as_text=True)
        assert "Invalid email" in html
