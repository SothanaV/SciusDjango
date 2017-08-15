from django.contrib import admin

# Register your models here.
from app.models import Note

class NoteAdmin(admin.ModelAdmin):
	list_display=[f.name for f in Note._meta.fields]

admin.site.register(Note,NoteAdmin)