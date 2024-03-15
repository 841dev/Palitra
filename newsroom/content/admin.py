from django.contrib import admin
from .models import Category, Tags, Article
# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'parent_category', 'logo', 'get_logo')
    #readonly_fields = ('get_logo',)

admin.site.register(Category, CategoryAdmin)

class TagsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

admin.site.register(Tags, TagsAdmin)

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'publish_date', 'author',  'article_tags', 'is_published', 'get_main_image')

    def article_tags(self, obj):
        return ', '.join([tag.name for tag in obj.tags.all()])

admin.site.register(Article, ArticleAdmin)
