from django.contrib import admin
from hotelapp.models import Room,Booking
# Register your models here.

class RoomAdmin(admin.ModelAdmin):
    list_display=['number','category','beds','capacity','room_categories']
admin.site.register(Room,RoomAdmin)


class BookingAdmin(admin.ModelAdmin):
    list_display=['user','room','check_in','check_out']

admin.site.register(Booking,BookingAdmin)
