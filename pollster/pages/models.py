from django.db import models
from django.db.models.fields import DateTimeField, IntegerField


class Page(models.Model):
    title=models.CharField(max_length=200)
    description=models.TextField(default='')
    content=models.TextField()
    pub_date=DateTimeField(auto_now=True)
    view_count=IntegerField(default=0)

    def __str__(self):
        return self.title



