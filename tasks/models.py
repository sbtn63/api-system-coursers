from django.db import models

from courses.models import Course

class Task(models.Model):
    
    STATUS = [
        ('P', 'PENDIENDTE'),
        ('C', 'COMPLETADO'),
        ('D', 'DISPONIBLE'),
        ('A', 'ATRASADO'),
    ]
    
    class Status(models.TextChoices):
        PENDIENDTE = 'P', 'PENDIENTE'
        COMPLETADO = 'C', 'COMPLETADO'
        DISPONIBLE = 'D', 'DISPONIBLE'
        ATRASADO = 'A', 'ATRASADO'
    
    name = models.CharField(max_length=255)
    avaliable_date = models.DateField()
    deadline = models.DateField()
    completed = models.BooleanField(default=False)
    task_status = models.CharField(
        max_length=1, 
        choices=Status.choices, 
        default=Status.PENDIENDTE
    )
    course = models.ForeignKey(
        Course, 
        related_name='tasks', 
        on_delete=models.CASCADE
    )
    created_at =models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.name}"