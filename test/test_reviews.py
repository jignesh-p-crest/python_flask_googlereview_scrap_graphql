import json
import unittest
from unittest.mock import patch
from nose.tools import assert_true
import requests
from datetime import datetime
from app.app import db
from app.main.models import ReviewModel
from base import BaseTestCase


class TestReviewModel(BaseTestCase):

	#client = app.test_client
	@patch('requests.post')
	def test_review_creation(self,mock_post):
		""" test review creation with valid inputs """
		review = {'review_time': '1 day ago','reviewer_name': 'Test User','rating': '4','review_text': 'This is testing review'}
		res = requests.post('http://127.0.0.1:5000/api/v1/reviews/', headers={'Content-Type': 'application/json'}, data=json.dumps(review))
		assert_true(res.ok)
	
if __name__ == "__main__":
  unittest.main() 