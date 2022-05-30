from django.contrib import admin
from videos.models import Category, AuthorVideo, VideoContent, Comments

# Register your models here.


admin.site.register(AuthorVideo)
admin.site.register(Category)
admin.site.register(VideoContent)
admin.site.register(Comments)