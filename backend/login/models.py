from django.db import models


class CommonUser(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    password = models.CharField(max_length=50)
    remarks = models.TextField()

    def __str__(self):
        return self.name
