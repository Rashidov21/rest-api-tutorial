from django.db import models

# Create your models here.

class Task(models.Model):
    name = models.CharField(max_length=100)
    start_date = models.DateTimeField(auto_now_add=True, blank=True)
    end_date = models.DateTimeField(blank=True)
    description = models.TextField()

    class Meta:
        verbose_name_plural = "Tasks"