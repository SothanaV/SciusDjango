from django.shortcuts import render

from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.list import ListView
from app.models import Note
from app.forms import NoteForm

from django.shortcuts import render

def home(request):
	return render(request, 'home.html', {'key': "value" })

class CreateNoteView(CreateView):
	queryset = Note()
	template_name='note.html'
	form_class = NoteForm
	success_url = '/home'