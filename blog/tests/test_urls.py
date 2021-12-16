from django.test import SimpleTestCase
from django.urls import reverse, resolve
from blog.views import post_list, post_detail, post_new, post_edit, post_draft_list, post_publish, post_remove, add_comment_to_post, comment_approve, comment_remove 

class TestUrls(SimpleTestCase):
	def test_post_list(self):
		url = reverse('post_list')
		self.assertEquals(resolve(url).func, post_list)

	def test_post_detail(self):
		url = reverse('post_detail', args=[arg1])
		self.assertEquals(resolve(url).func, post_detail)

	def test_post_new(self):
		url = reverse('post_new')
		self.assertEquals(resolve(url).func, post_new)

	def test_post_edit(self):
		url = reverse('post_edit', args=[arg1])
		self.assertEquals(resolve(url).func, post_edit)

	def test_post_draft_list(self):
		url = reverse('post_draft_list')
		self.assertEquals(resolve(url).func, post_draft_list)

	def test_post_publish(self):
		url = reverse('post_publish', args=['arg1'])
		self.assertEquals(resolve(url).func, post_publish)

	def test_post_remove(self):
		url = reverse('post_remove', args=['arg1'])
		self.assertEquals(resolve(url).func, post_remove)

	def test_add_comment(self):
		url = reverse('add_comment_to_post', args=[arg1])
		self.assertEquals(resolve(url).func, add_comment_to_post)

	def test_comment_approve(self):
		url = reverse('comment_approve', args=[arg1])
		self.assertEquals(resolve(url).func, comment_approve)

	def test_comment_remove(self):
		url = reverse('comment_remove', args=[arg1])
		self.assertEquals(resolve(url).func, comment_remove)