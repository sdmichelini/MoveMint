from django import forms
from django.forms import widgets

class CustomDateInput(widgets.TextInput):
    input_type = 'date'

#Form for a new project
class ProjectForm(forms.Form):
	name = forms.CharField(label='Project Name', max_length = 50)
	about = forms.CharField(label='About Project', widget=forms.Textarea)
	donation_goal = forms.DecimalField(label='Donation Goal')
	start_date = forms.DateField(label='Project Start Date',  widget=CustomDateInput)
	end_date = forms.DateField(label='Project End Date',  widget=CustomDateInput)
	#Validation Logic
	def clean(self):
		if self.start_date > self.end_date:
			raise ValidationError(_("Start Date Must be Earlier Than End Date"))
