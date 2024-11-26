from django.db import models

class SampleModel(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=1000)
    
    def __str__(self) -> str:
        return self.title