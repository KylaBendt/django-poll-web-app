from django.contrib import admin

from .models import Question, Category, Choice

admin.site.register(Question)
admin.site.register(Category)
admin.site.register(Choice)
