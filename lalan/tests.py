from django.test import TestCase
from lalan.models import Blog

# Create your tests here.


class BlogModelTestCase(TestCase):

    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        Blog.objects.create(title='The 1st blog ever', body='Such blog body, much wow')

    def test_title(self):
        author = Blog.objects.get(id=1)
        field_label = author._meta.get_field('title').verbose_name
        self.assertEquals(field_label, 'title')
