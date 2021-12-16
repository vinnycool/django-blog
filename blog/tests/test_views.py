from django.test import TestCase, Client
from django.urls import reverse
from blog.models import Post, Comment
import json
from django.contrib.auth.models import User

class TestViews(TestCase):

	def SetUp(self):
		self.client = Client()
		self.user = User.objects.create_superuser('test_admin','test_admin')
		self.client.login(username='test_admin',password='test_admin')
		self.list_url = reverse('post_list')
		self.detail_url = reverse('post_detail', args=[arg1])
		self.new_url = reverse('post_new')
		self.remove_url = reverse('post_remove')

	def test_post_list_GET(self):
		response = self.client.get(reverse(self.list_url))

		self.assertEquals(response.status_code, 200)
		self.assertTemplateUsed(response, 'blog/post_list.html')

	def test_post_detail_GET(self):
		response = self.client.get(self.detail_url)

		self.assertEquals(response.status_code, 200)
		self.assertTemplateUsed(response, 'blog/post_detail.html')

	def test_post_new_POST(self):
		response = self.client.post(self.new_url,{
			'title': 'Testing' ,
			'text': 'This is for Testing'
		)}
		self.assertEquals(response.status_code, 302)
		self.assertEquals(Post.first().title, 'Testing')

	def test_post_remove(self):
		Post.objects.create(
			title='Testing'
			text='For Testing'
		)
		response = self.client.delete(self.remove_url, json.dunps({
			'id': 1
		}))
		self.assertEquals(response.status_code, 302)
		self.assertEuals(Post.count(),0)

	def test_post_no_remove(self):
		Post.objects.create(
			title='testing'
			text='For testing'
		)
		response = self.client.delete(self.remove_url)

		self.assertEquals(response.status_code, 404)