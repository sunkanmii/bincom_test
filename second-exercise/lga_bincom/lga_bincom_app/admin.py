from django.contrib import admin

# Register your models here.
from .models import PollingUnit, Lga

admin.site.register(PollingUnit)
admin.site.register(Lga)