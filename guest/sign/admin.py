from django.contrib import admin
from sign.models import Event,Guest

# Register your models here.
class EventAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'status', 'address', 'start_time']
    search_fields = ['name']
    list_filter = ['status']

class GuestAdmin(admin.ModelAdmin):
    list_display = ['guest_name', 'phone', 'email', 'sign', 'create_time', 'event_id']
    search_fields = ['guest_name', 'phone']
    list_filter = ['sign']

admin.site.register(Event, EventAdmin)
admin.site.register(Guest, GuestAdmin)
