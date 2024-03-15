from django.db import models
from content.models import Article


class MenuCategory(models.Model):
    name = models.CharField(max_length=250)
    slug = models.SlugField(unique=True)

    menu_category_order = models.PositiveIntegerField(default=0, blank=False, null=False, db_index=True)

    class Meta:
        verbose_name = 'menu Category'
        verbose_name_plural = 'menu Categories'
        ordering = ['menu_category_order']


    def __str__(self):
        return self.name


class Menu(models.Model):
    name = models.CharField(max_length=250)
    link = models.URLField(blank=True, null=True)
    is_external = models.BooleanField(default=False)
    category = models.ForeignKey(MenuCategory, on_delete=models.SET_NULL, null=True, blank=True)
    is_active = models.BooleanField(default=True)

    menu_order = models.PositiveIntegerField(default=0, blank=False, null=False, db_index=True)

    class Meta:
        ordering = ['menu_order']

    def __str__(self):
        return self.name


class Block(models.Model):
    BLOCK_VISUAL_CHOICES = [
        ('standard', 'Standard'),
        ('horizontal', 'Horizontal'),
        ('vertical', 'Vertical'),
    ]

    link = models.ManyToManyField(Article, related_name='blocks', blank=True)
    visual_selection = models.CharField(max_length=20, choices=BLOCK_VISUAL_CHOICES)
    block_position = models.CharField(max_length=50)
    row = models.IntegerField()
    title = models.CharField(max_length=250)
    show_title = models.BooleanField(default=False)

    block_order = models.PositiveIntegerField(default=0, blank=False, null=False, db_index=True)

    class Meta:
        ordering = ['block_order']

    def __str__(self):
        return self.title
