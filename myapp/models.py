from django.db import models

class Places(models.Model):
    place_name = models.CharField(max_length = 100)
