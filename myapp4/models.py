from django.db import models

class song(models.Model):
      title=models.CharField(max_length=20)
      music=models.FileField(upload_to='media')
