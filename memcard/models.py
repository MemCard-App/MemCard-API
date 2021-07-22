from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Word(models.Model):
    word = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    # Feature for a later time
    # is_private = models.BooleanField(default=True)
    
    def __str__(self):
        return self.word
    
