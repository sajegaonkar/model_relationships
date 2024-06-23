from django.contrib import admin

# Register your models here.
from manytomany.models import Publication, Article

admin.register(Publication)

admin.register(Article)


