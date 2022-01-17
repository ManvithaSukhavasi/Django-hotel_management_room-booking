from hotelapp.models import Room

def get_room_category_human_format(category):
    room = Room.objects.all()[0]
    room_category = dict(room.room_categories).get(category, None)
    return room_category

