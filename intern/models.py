from django.db import models

class Application(models.Model):
    name = models.CharField(max_length=100)
    pid = models.PositiveIntegerField(unique=True)

    def __str__(self):
        return self.name
