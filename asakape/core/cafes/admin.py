from django.contrib import admin
from .models import Cafe, Tags

# Register your models here.
@admin.register(Cafe)
class CafeAdmin(admin.ModelAdmin):
    pass

@admin.register(Tags)
class TagsAdmin(admin.ModelAdmin):
    pass

