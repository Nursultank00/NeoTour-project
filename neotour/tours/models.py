from django.db import models

class Category(models.Model):
    category_name = models.CharField(max_length = 255)

    def __str__(self):
        return self.category_name

# Create your models here.
class Tour(models.Model):
    tour_name = models.CharField(max_length = 255)
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    location = models.CharField(max_length = 255)
    description = models.TextField()
    image = models.ImageField(upload_to = 'tour_profile_photos')

    def __str__(self):
        return self.tour_name
    
class Review(models.Model):
    nickname = models.CharField(max_length = 255)
    review_image = models.ImageField(upload_to = 'review_images')
    commentary = models.TextField()
    tour_related = models.ForeignKey(Tour, on_delete = models.DO_NOTHING)
