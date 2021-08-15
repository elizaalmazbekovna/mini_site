from django.contrib import admin
from shopping.models import *


class PruductAdmin(admin.ModelAdmin):
    class Meta:
        model= Product
    search_fields = ['title','description']
    list_display = 'id title category price'.split()
    list_filter = 'category'.split()
# Register your models here.
admin.site.register(Category)
admin.site.register(Product,PruductAdmin)
admin.site.register(Tag)