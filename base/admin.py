from django.contrib import admin
from .models import ClockListener

class ClockListenerAdmin(admin.ModelAdmin):
    pass

admin.site.register(ClockListener, ClockListenerAdmin)
