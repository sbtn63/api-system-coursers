from django.db import models
from django.contrib.auth.models import User

class WallPeper(models.Model):
    wallpeper = models.URLField(max_length=500)
    created_at =models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.wallpeper}"
