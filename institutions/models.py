from django.db import models
from django.contrib.auth.models import User

class Institution(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    emblem = models.URLField(max_length=500, blank=True, null=True)
    user = models.ForeignKey(User, related_name='institutions', on_delete=models.CASCADE)
    created_at =models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created_at']
        constraints = [
            models.UniqueConstraint(
                fields=["user", "name"],
                name="unique_name_per_user"
            )
        ]
    
    def __str__(self):
        return f"{self.name}"