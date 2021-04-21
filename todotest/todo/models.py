from django.db import models

# Create your models here.
class todo(models.Model):
    taskname=models.CharField(max_length=200)
    taskstatus=models.CharField(max_length=200)
    class Meta:
      db_table = 'todo' 
        