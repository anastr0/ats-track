from django.db import models

# Create your models here.
class Candidate(models.Model):
    name = models.CharField(max_length=150)
    age = models.IntegerField()
    gender = models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-created_at']
