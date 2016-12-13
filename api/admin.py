from django.contrib import admin

from api.models import Car


class CarAdmin(admin.ModelAdmin):
    list_display = ('id', 'make', 'model', 'year')

admin.site.register(Car, CarAdmin)
