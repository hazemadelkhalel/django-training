from email.policy import default
from django.db import models



class Artist(models.Model):
    name = models.TextField(blank = False, unique = True)
    social_link = models.URLField(max_length = 128, null = False)  
    def __str__(self) -> str:
        return self.name
    
        