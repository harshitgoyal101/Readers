from django.contrib import admin

# Register your models here.
from .models import *
admin.site.register(Reader)
admin.site.register(Post)
admin.site.register(Book)
admin.site.register(Gener)