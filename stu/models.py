
from __future__ import  unicode_literals
from django.db import models

# Create your models here.


class Student(models.Model):
    sname = models.CharField(max_length=30, unique=True)
    spwd = models.CharField(max_length=30)

    def __str__(self):
        return u'Student:%s'%self.sname


class Post(models.Model):
    pid = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100, unique=True,null=True)
    content = models.TextField()
    create = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    email = models.EmailField()
    isdelete = models.BooleanField(default=False)
    access_count = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    file = models.ImageField(upload_to='upload/images')

    def __str__(self):
        return u'Post:%s, %s'%(self.title, self.access_count)

    class Meta:
        db_table = 't_post'
