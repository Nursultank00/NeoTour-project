from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

CHOICES = (
        ('Summer', 'Summer'),
        ('Winter', 'Winter'),
        ('Spring', 'Spring'),
        ('Autumn', 'Autumn'),
)
class Category(models.Model):
    category_name = models.CharField(max_length = 255)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.category_name

# Create your models here.
class Tour(models.Model):
    tour_name = models.CharField(max_length = 255)
    category = models.ManyToManyField(Category, related_name = 'tourslist')
    location = models.CharField(max_length = 255)
    description = models.TextField()
    season = models.CharField(max_length=10, choices = CHOICES, default = 'Summer')
    image = models.ImageField(upload_to = 'tour_profile_photos')

    class Meta:
        verbose_name = 'Tour'
        verbose_name_plural = 'Tours'

    def __str__(self):
        return self.tour_name
    
class Review(models.Model):
    nickname = models.CharField(max_length = 255)
    review_image = models.ImageField(upload_to = 'review_images')
    commentary = models.TextField()
    tour_related = models.ForeignKey(Tour, related_name = 'reviews', on_delete = models.CASCADE)
    class Meta:
        verbose_name = 'Review'
        verbose_name_plural = 'Reviews'

    def __str__(self):
        return f'{self.nickname} - {self.tour_related}'

class Reservation(models.Model):
    phone_number = models.CharField(max_length = 20)
    comments_to_reserve = models.TextField()
    number_of_people = models.IntegerField(default=1, validators=[
                                                                MaxValueValidator(100),
                                                                MinValueValidator(1)
                                                                ])
    tour_reserved = models.ForeignKey(Tour, related_name = 'reservations', on_delete = models.CASCADE)
    
    class Meta:
        verbose_name = 'Reservation'
        verbose_name_plural = 'Reservations'

    def __str__(self):
        return f'{self.phone_number}: {self.tour_reserved}'