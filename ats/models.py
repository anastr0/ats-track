from django.db import models

# Create your models here.
class Candidate(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]
    name = models.CharField(max_length=150)
    age = models.IntegerField()
    gender = models.CharField(choices=GENDER_CHOICES, max_length=1, blank=True, null=True)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-created_at']
