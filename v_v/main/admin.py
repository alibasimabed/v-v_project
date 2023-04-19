from django.contrib import admin
from main.models import Flight


class FlighAdmin(admin.ModelAdmin):
    pass



admin.site.register(Flight, FlighAdmin)

