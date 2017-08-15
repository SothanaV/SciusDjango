from django import forms
from django.forms import ModelForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django.forms.extras.widgets import SelectDateWidget
from django.contrib.admin import widgets
import datetime
from app.models import Note

class NoteForm(ModelForm):
	class Meta:
		model =  Note
		exclude=[]

		# widgets = {
		# 	'dob': forms.DateInput(
		# 		attrs={
		# 		'type': 'date', 
		# 		'value': datetime.datetime.now().strftime("%Y-%m-%d")
		# 		}, format="%Y-%m-%d"
		# 	),
		# }
		
	def __init__(self, *args, **kwargs):
		super(NoteForm, self).__init__(*args, **kwargs)
		self.helper = FormHelper()
		self.helper.add_input(Submit('submit', 'Submit'))