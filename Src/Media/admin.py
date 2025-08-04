from django.contrib import admin
from .models import Category,News,Comment,Articles


admin.site.register(Category)

class AdminNews(admin.ModelAdmin):
    list_display=('title','category','add_time','image', 'views')
admin.site.register(News,AdminNews)

class Admin_Comment(admin.ModelAdmin):
    list_display=('news', 'email', 'comments', 'status')
admin.site.register(Comment,Admin_Comment)

class Admin_Article(admin.ModelAdmin):
    list_display=('title','add_time','image', 'views')
admin.site.register(Articles,Admin_Article)