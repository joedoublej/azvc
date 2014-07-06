from django.db import models
import os


class Author(models.Model):
	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)
	photo = models.ImageField(upload_to="images/", blank=True, null=True)
	title = models.CharField(max_length=100)
	company = models.CharField(max_length=100)
	blog_url = models.URLField(blank=True, null=True)
    
	def __unicode__(self):
		return u'%s %s' % (self.first_name, self.last_name)


class Post(models.Model):
	author = models.ForeignKey(Author)
	url = models.URLField(blank=True, null=True)
	title = models.CharField(max_length=100, null=True)
	created = models.DateField()
	body = models.CharField(max_length=5000)
	comment_count = models.IntegerField()