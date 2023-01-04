from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import News, Category


class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category', 'created_at', 'updated_at', 'views', 'get_photo', 'is_published')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'category', 'content')
    list_editable = ('is_published',)
    list_filter = ('is_published', 'category')

    # Rules for fields while editing single News object
    fields = (
        'id', 'title', 'category', 'content', 'photo',
        'get_photo', 'views', 'created_at', 'updated_at', 'is_published'
    )
    readonly_fields = ('id', 'created_at', 'updated_at', 'views', 'get_photo')

    # Param obj - that`s the current object. For example single News object in the news list
    def get_photo(self, obj):
        if obj.photo:
            return mark_safe(f'<img src="{ obj.photo.url }" alt="{ obj.title }" width="32" />')

    # To change the column name in the admin panel, needs to add .short_description to the field
    # Can be used only with custom attrs like made above 'get_photo'
    get_photo.short_description = 'Picture'


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    search_fields = ('title',)


admin.site.register(News, NewsAdmin)
admin.site.register(Category, CategoryAdmin)

admin.site.site_title = 'The Daily Bugle'
admin.site.site_header = 'The Daily Bugle'
