from django.db import models

# Create your models here.


class Blog(models.Model):
    title = models.CharField(max_length=200, help_text="Enter title", null=False)
    body = models.CharField(max_length=200, help_text="Add your blog body here", null=False)
    author = models.CharField(max_length=200, help_text="Enter author name", null=False)

    def __str__(self):
        return self.title
