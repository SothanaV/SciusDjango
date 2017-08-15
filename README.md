# SciusDjango

* install packages
```sh 
pip install -r requirements.txt
```

* start project

*start app

* create models
```python
class Note(models.Model):
	created=models.DateTimeField(auto_now_add=False)
	name=models.CharField(max_length=100)
	email=EmailField()
	message=models.TextField()
```
