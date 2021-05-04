from datetime import datetime

# ashutosh.tiwari@treebohotels.com

class Parking:
	"""
	Model to create add 
	"""
	floors = []

	def __init__(self):
		pass

	@classmethod
	def get_all_floors(cls):
		for floor in cls.floors:
			floor_number, slots = floor.get_floor_detail()
			print("floor_number : ", floor_number)
			print("slots :", slots )

	@classmethod
	def add_floor(cls, floor):
		"""
			TODO: Implement to add floor based using Floor object  
		"""
		cls.floors.append(floor)

	def remove_floor(self, floor):
		"""
			TODO: Implement to remove floor based using Floor object  
		"""
		self.floors.remove(floor)

	@classmethod
	def fetch_slot(cls, reg_no):
		for floor in cls.floors:
			slot = floor.find_vehicle_slot(reg_no)
			if slot != -1:
				print("floor , slot :", floor.floor_number, slot )
				break
		return (floor.floor_number, slot)

	@classmethod
	def fetch_slot_by_colour(cls, color):

		fetch_array =[]
		for floor in cls.floors:
			fetch_array = floor.find_vehicle_slot_by_colour(color, fetch_array)
		print(fetch_array)
		return fetch_array

	@classmethod
	def park_a_vehicle(cls, reg_no, colour):
		"""

		:param reg_no: Registration number of particular vehicle
		:param color: Vehicle colour
		:return:
		"""
		vehicle_obj = Vehicle(reg_no, colour)
		for floor in cls.floors:
			slot = floor.get_free_slot()
			print("Free slot: ", slot)
			if slot != -1:
				floor.allocate_slot(slot, vehicle_obj )
				break
		return True if slot else False

	@classmethod
	def unpark_a_vehicle(cls, reg_no):
		"""

		:param reg_no:
		:return:
		"""
		for floor in cls.floors:
			slot = floor.find_vehicle_slot(reg_no)
			if slot:
				floor.deallocate_vehicle(slot)
				break


		return True if slot else False
		pass



class Floor:
	"""
	"""

	def __init__(self, floor_number, number_of_slots=5):
		"""
		"""
		self.floor_number = floor_number
		self.number_of_slots = number_of_slots
		self.slots = [ "Free" for _ in range(number_of_slots)]

	def get_all_slots(self):
		print(self.slots)

	def get_floor_detail(self):
		return self.floor_number, self.slots

	def get_free_slot(self):
		try:
			free_slot = self.slots.index("Free")
		except:
			return -1
		return free_slot

	def allocate_slot(self, slot, vehicle):
		print(f"Allocation slot for vehicle art floor {self.floor_number} at slot {slot}")
		self.slots[slot] = vehicle
		return True

	def find_vehicle_slot(self, reg_no):
		for vehicle in self.slots:
			if type(vehicle) == Vehicle and vehicle.reg_no == reg_no:
				return self.slots.index(vehicle)
		return -1

	def find_vehicle_slot_by_colour(self, color, output=[]):

		for vehicle in self.slots:
			if type(vehicle) == Vehicle and vehicle.color == color:
				output.append({self.floor_number :self.slots.index(vehicle)})
		return output

	def deallocate_vehicle(self, slot):
		self.slots[slot] = "Free"

#
class VehicleTypes:
	# TODO we can deifne vehicle types and implement factory design pattern for all type of vehicle
	pass

class Vehicle:

	def __init__(self, reg_no, color=None):
		self.reg_no = reg_no
		self.color = color
		self.type = 'bike' #

		#TODO
		self.entry_time = datetime.now()



	def __del__(self):
		#TODO delete vehicle object once it out
		pass

