from django.db import models

class Application(models.Model):
    name = models.CharField(max_length=100)
    roll_number = models.CharField(max_length=30)
    department = models.CharField(max_length=100)
    interests = models.TextField(blank=True)
    applied_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.roll_number})"
