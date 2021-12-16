from django.test import TestCase
from blog.forms import PostForm, CommentForm

class TestformsPost(TestCase):

	def test_Post_form_valid(self):
		form = PostForm({ 
			'title': 'This is for testing', 
			'text': 'Testing purpose'
		})
		self.assertTrue(form.is_valid())

	def test_Post_form_no_data(self):
		form = PostForm({})
		self.assertFalse(form.is_valid())

class TestformsComment(TestCase):

	def test_comment_form_valid(self):
		form = CommentForm({
			'author': 'Harshhaa Reddy' ,
			'text': 'Great Blog'
		})
		self.assertTrue(form.is_valid())

	def test_comment_form_no_data(self):
		form = CommentForm({})
		self.assertFalse(form.is_valid)