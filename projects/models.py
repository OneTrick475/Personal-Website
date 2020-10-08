from django.db import models

class Projects(models.Model):
    name = models.CharField(max_length=255)
    info = models.CharField(max_length=1000, default='')
    image_url = models.CharField(max_length=255, default='') 
    github_url = models.CharField(max_length=255, default='')

    def __str__(self):
        return self.name
