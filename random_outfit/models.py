from django.db import models

class Outfit(models.Model):
    TYPE_CHOICES = [
        ('casual', 'Casual'),
        ('professional', 'Professional'),
    ]

    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='outfits/')
    main_color = models.CharField(max_length=20)
    outfit_type = models.CharField(max_length=15, choices=TYPE_CHOICES, default='casual')
    color_one = models.CharField(max_length=20, default='black')
    color_two = models.CharField(max_length=20, default='white')

    def __str__(self):
        return self.name
