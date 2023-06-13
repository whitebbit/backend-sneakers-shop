from django.contrib import admin
from . import models
# Register your models here.


class SneakerAdmin(admin.ModelAdmin):
    list_display = ('name', "article", 'price',)
    list_display_links = ('name',)
    search_fields = ('id', 'name', "price", "color")
    list_editable = ('price',)
    list_filter = ('name', "article", "price", "color")


admin.site.register(models.Sneaker, SneakerAdmin)
admin.site.register(models.Size)