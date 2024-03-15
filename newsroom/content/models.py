from django.db import models
from users.models import CustomUser
from django.utils import timezone
from django.utils.html import mark_safe
from tinymce.models import HTMLField


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=250)
    logo = models.ImageField(upload_to='logos/', null=True, blank=True)
    parent_category = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def get_logo(self):
        if self.logo:
            return mark_safe(f'<img src = "{self.logo.url}" width = "100"/>')
        else:
            return 'Could not find image.'

    def __str__(self):
        return f'{self.name}'


class Tags(models.Model):
    name = models.CharField(max_length=320)

    class Meta:
        verbose_name = 'Tags'
        verbose_name_plural = 'Tags'

    def __str__(self):
        return f'{self.name}'


class Article(models.Model):
    title = models.CharField(max_length=500)
    description = HTMLField(blank=True)
    publish_date = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    tags = models.ManyToManyField(Tags, blank=True)
    main_image = models.ImageField(upload_to='main_images/', null=True, blank=True)
    is_published = models.BooleanField(default=False)


    class Meta:
        verbose_name = 'Article'
        verbose_name_plural = 'Articles'


    def get_main_image(self):
        if self.main_image:
            return mark_safe(f'<img src = "{self.main_image.url}" width = "100"/>')
        else:
            return 'Could not find image.'

    def __str__(self):
        return f'{self.title} - {self.author}'
