from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    bio = models.TextField(default="About me")
    tagline = models.CharField(default="I'm EPIC", max_length=200)
    first_name = models.CharField(default="John", max_length=200)
    last_name = models.CharField(default="Doe", max_length=200)
    website = models.CharField(default="example.com", max_length=200)


    def __str__(self):
        return f'{self.user.username}'

    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)
        
        # resize the image to 300px by 300px
        if img.height > 250 or img.width > 250:
            output_size = (250, 250)
            img.thumbnail(output_size)
            img.save(self.image.path)


