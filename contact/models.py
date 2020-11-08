from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField(max_length=500)
    messege = models.TextField(blank=False)

    def __str__(self):
        return self.name