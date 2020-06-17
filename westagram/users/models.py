from django.db import models

# Create your models here.


class Users(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    password = models.BinaryField(max_length=500)

    class Meta:
        db_table = "users"
