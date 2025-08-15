from django.contrib import admin
from .models import Appointment, Service,Contact

# Register your models here.
admin.site.register(Service)

@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'formatted_time')
    readonly_fields = ('formatted_time',)  # Show this instead of editable time

    def formatted_time(self, obj):
        return obj.time.strftime("%I:%M %p") if obj.time else "-"
    formatted_time.short_description = 'Time (12-hour)'

    # Remove original time from form fields
    fields = ('name', 'phone', 'service', 'date', 'formatted_time', 'email')


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'created_at')
    search_fields = ('name', 'email', 'phone')
    list_filter = ('created_at',)
