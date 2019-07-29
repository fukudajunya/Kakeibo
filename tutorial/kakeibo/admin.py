from django.contrib import admin

# Register your models here.

from .models import Category, Kakeibo

class KakeiboAdmin(admin.ModelAdmin):
    list_display = ('date', 'category', 'money', 'memo')

admin.site.register(Category)
admin.site.register(Kakeibo, KakeiboAdmin)