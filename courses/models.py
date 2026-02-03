from django.db import models
from django.contrib.auth.models import User

from institutions.models import Institution
from wallpepers.models import WallPeper

class Course(models.Model):
    
    class Status(models.TextChoices):
        DISPONIBLE = 'D', 'DISPONIBLE'
        CURSANDO = 'C', 'CURSANDO'
        FINALIZADO = 'F', 'FINALIZADO'
        PENDIENTE = 'P', 'PENDIENTE'
    
    code = models.CharField(max_length=100, blank=True)
    name = models.CharField(max_length=255)
    block = models.CharField(max_length=100, blank=True)
    period = models.CharField(max_length=100, blank=True)
    course_status = models.CharField(
        max_length=1, 
        choices=Status.choices, 
        default=Status.PENDIENTE
    )
    start_date = models.DateField()
    end_date = models.DateField()
    institution = models.ForeignKey(
        Institution, 
        related_name='courses', 
        on_delete=models.CASCADE
    )
    wallpaper = models.ForeignKey(
        WallPeper, 
        related_name='courses', 
        on_delete=models.CASCADE
    )
    created_at =models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.code.strip()} - {self.name}" if self.code and self.code.strip() else f"{self.name}"
    