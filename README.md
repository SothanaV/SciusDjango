# SciusDjango

* install packages
```sh 
pip install -r requirements.txt
```

* start project and named as "demo"
```sh
python manage.py startproject demo
```

* start application and named "app"
```sh
python manage.py startapp app
```

* create /app/models.py
```python
class Note(models.Model):
	created=models.DateTimeField(auto_now_add=False)
	name=models.CharField(max_length=100)
	email=EmailField()
	message=models.TextField()
```

* create superuser {username: admin, password: qwer1234}
```sh
python manage.py createsuperuser
```

* add app in setting.py
```python
INSTALLED_APPS = [
	.
	.
	.
    'django.contrib.staticfiles',
    'app',
    'crispy_forms',
]
```

* run server to check the admin page
```
python manage.py runserver
```

* then open web browser and go to http://localhost:8000/admin

# Add a leave-note page

* make directory /app/templates

* create /app/form.py

* create /app/view.py

* add path in /demo/url.py


