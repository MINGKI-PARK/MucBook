from django.contrib import admin

from .models import Tasty, Category

admin.site.register(Tasty)
admin.site.register(Category)