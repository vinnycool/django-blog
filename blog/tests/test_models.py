from django.test import TestCase
from blog.models import Post, Comment
from django.utils import timezone

class TestModelsPost(TestCase):

	def setUpTestData(self):
		Post.objects.create(title="testing Purpose",text="This is for testing Post method")

	def test_titlePost(self):
		post = Post.objects.get(id=1)
		field_label = post._meta.get_field('title').verbose_name
		self.assertEquals(field_label, 'testing Purpose')

	def test_title_Post_maxlength(self):
		post = Post.objects.get(id=1)
		max_length = post._meta.get_field('title').max_length
		self.assertEquals(max_length, 200)

	def test_textPost(self):
		post = Post.objects.get(id=1)
		field_label = post._meta.get_field('text').verbose_name
		self.assertEquals(field_label, 'This is for testing Post method')

	def test_Post_str(self):
		post = Post.objects.get(id=1)
		self.assertEquals(str(post), 'testing Purpose')

class TestModelsComment(TestCase):

	def SetUpTestData(self):
		Comment.objects.create(author= 'Harshhaa Reddy', text='Nice Post')

	def test_authorComment(self):
		comment = Comment.objects.get(id=1)
		field_label = comment._meta.get_field('author').verbose_name
		self.assertEquals(field_label, 'Harshhaa Reddy')

	def test_author_max_length(self):
		comment = Comment.objects.get(id=1)
		max_length = comment._meta.get_field('author').max_length
		self.assertEquals(max_length,200)

	def test_textComment(self):
		comment = Comment.objects.get(id=1)
		field_label = comment._meta.get_field('text').verbose_name
		self.assertEquals(field_label, 'Great Blog')

	def test_approveComment(self):
		comment = Comment.objects.get(id=1)
		self.assertEquals(comment.approve(), 'True')

	def test_Comment_str(self):
		comment = Comment.objects.get(id=1)
		self.assertEquals(str(comment),'Great Blog')