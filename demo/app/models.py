from __future__ import unicode_literals

from django.db import models

class Person(models.Model):
	created=models.DateTimeField(auto_now_add=False)
	name=models.CharField(max_length=100)
	email=EmailField()
	message=models.TextField()
	
	def __unicode__(self):
		return u"%s %s"%(self.name, self.email)