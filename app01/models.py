from django.db import models

# Create your models here.

class UserInfo(models.Model):
    name = models.CharField(max_length=32)
    password = models.CharField(max_length=64)
    age = models.IntegerField()
    data = models.IntegerField(null=True,blank=True)
#python manage.py makemigrations
#python manage.py migrate
# create table app01_userinfo(
#     id bigint auto_increment primary key,
#     name varchar(32),
#     password varchar(64),
#     age int
# )
class Department(models.Model):
    title = models.CharField(max_length=16)

# class Role(models.Model):
#     caption = models.CharField(max_length=16)

# 新建數據
# 本質:insert into app01_deparment(title)values("銷售部")
# Department.objects.create(title="銷售部")