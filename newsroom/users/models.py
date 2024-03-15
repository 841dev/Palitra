from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.html import mark_safe
from tinymce.models import HTMLField

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    profile_picture = models.ImageField(upload_to='profile_images/', blank=True, verbose_name='Profile Picture')
    description = HTMLField(blank=True)
    is_author = models.BooleanField(default=False)

    def get_profile_picture(self):
        if self.profile_picture:
            return mark_safe(f'<img src = "{self.profile_picture.url}" width = "100"/>')
        else:
            return 'No profile picture uploaded.'


    def __str__(self):
        return self.email