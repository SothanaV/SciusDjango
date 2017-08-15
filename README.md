# SciusDjango

* install packages
```sh 
pip install -r requirements.txt
```

* start project and named as "demo"
```sh
python manage.py startproject demo
```

*start application and named "app"
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

* create superuser

* add app in setting.py

* run server to check the admin page
```
http://localhost:8000/admin
```
* make directory /app/templates

* create /app/form.py

* create /app/view.py

* add path in /demo/url.py


