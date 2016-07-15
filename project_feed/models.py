from __future__ import unicode_literals

from django.core.exceptions import ValidationError
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.contrib.auth.models import User

import uuid



@python_2_unicode_compatible
class Tag(models.Model):
	'''
	This is a tag model. A tag is a string that contains an attribute.
	'''
	title = models.CharField(max_length = 20)
	def __str__(self):
		return self.title


@python_2_unicode_compatible
class Organization(models.Model):
	name = models.CharField(max_length = 50)
	about = models.TextField()
	owner = models.ForeignKey(User)
	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	def __str__(self):
		return self.name

@python_2_unicode_compatible
class Project(models.Model):
	name = models.CharField(max_length = 50)
	about = models.TextField()
	org = models.ForeignKey(Organization)
	donation_amount = models.DecimalField(max_digits = 10, decimal_places = 2, default=0.0)
	donation_goal = models.DecimalField(max_digits = 10, decimal_places = 2)
	start_date = models.DateField()
	end_date = models.DateField()
	tags = models.ManyToManyField(Tag, blank=True)
	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	def __str__(self):
		return self.name

	#Validation Logic
	def clean(self):
		if self.start_date > self.end_date:
			raise ValidationError(_("Start Date Must be Earlier Than End Date"))

@python_2_unicode_compatible
class ProjectUpdate(models.Model):
	name = models.CharField(max_length = 50)
	about = models.TextField()
	post_date = models.DateField(auto_now_add=True)
	project = models.ForeignKey(Project)
	def __str__(self):
		return self.name
