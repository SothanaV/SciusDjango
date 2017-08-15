from __future__ import unicode_literals

from django.db import models

class Note(models.Model):
	created=models.DateTimeField(auto_now_add=True)
	name=models.CharField(max_length=100)
	email=models.EmailField()
	message=models.TextField()
	
	def __unicode__(self):
		return u"%s %s"%(self.name, self.email)