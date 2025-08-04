from django.contrib import admin
from .models import Category,Blog

admin.site.register(Category)

class blog_add(admin.ModelAdmin):
    list_display=('title', 'date', 'image')
admin.site.register(Blog,blog_add)