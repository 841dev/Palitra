from django.contrib import admin
from adminsortable2.admin import SortableAdminMixin, SortableInlineAdminMixin
from .models import Menu, MenuCategory, Block



@admin.register(Menu)
class SortableMenuAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ('id', 'menu_order', 'name', 'link', 'is_external', 'category', 'is_active')
    list_display_links = ('name', 'link', 'is_external', 'category', 'is_active')
    list_per_page = 5

@admin.register(MenuCategory)
class SortableMenyCategoryAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ('id', 'menu_category_order', 'name', 'slug')
    list_display_links = ('id', 'name', 'slug')


class ArticleInline(admin.TabularInline):
    model = Block.link.through
    extra = 0


@admin.register(Block)
class BlockAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ('id', 'title', 'visual_selection', 'block_position', 'row')
    list_display_links = ('id', 'title', 'visual_selection', 'block_position', 'row')
    inlines = [ArticleInline]
    exclude = ('link',)
