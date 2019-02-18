from django.contrib import admin

from Rating.models import Post, UserProfile, Comment, Rating

admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(UserProfile)
admin.site.register(Rating)
