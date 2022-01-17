from django.urls import path

from . views import RoomList,BookingListView, RoomDetailView, cancelBookingview

app_name='hotelapp'

urlpatterns = [
    path('room_list/', RoomList, name='RoomList'),
    path('booking_list/', BookingListView.as_view(), name='BookingListView'),
    path('room/<category>',  RoomDetailView.as_view(), name='RoomDetailView'),
    path('booking/cancel/<pk>',  cancelBookingview.as_view(), name='cancelBookingview'),
    
]

