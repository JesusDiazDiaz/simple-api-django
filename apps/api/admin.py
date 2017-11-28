from django.contrib import admin
from apps.api import models
# Register your models here.


@admin.register(models.Movies, models.Categories)
class BaseAdmin(admin.ModelAdmin):
    pass
