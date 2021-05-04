from models import Parking
from models import Floor


def setup():
    floor_obj = Floor(1, 5)
    Parking.add_floor(floor_obj)

    floor_obj_2 = Floor(2, 5)
    Parking.add_floor(floor_obj_2)

    Parking.park_a_vehicle(100, 'black')
    Parking.park_a_vehicle(200, 'black')
    Parking.get_all_floors()

    Parking.unpark_a_vehicle(200)
    Parking.get_all_floors()

    Parking.fetch_slot(100)
    Parking.fetch_slot_by_colour('black')

setup()

