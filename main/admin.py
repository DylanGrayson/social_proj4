from django.contrib import admin
from main.models.corgi import Corgi
from main.models.post import Post


admin.site.register(Corgi)
admin.site.register(Post)