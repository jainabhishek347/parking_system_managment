from heapq import heapify, heappush, heappop

class Slot():

    def __init__(self):
        pass

class Parking:

	def __init__(self):
		
		# dict of all vehicles using reg_no as key and  vehicle object value.
		# Fetch booked slot for any particular reg_no Time complexity: O(1) using dict
		self.booked_slots = {}
		
		# Heap queue algorithm as heap[0] is the smallest item so fetching free slot Time complexity O(1).
		self.heap = [x for x in range(1, (5*3)+1)]
		heapify(self.heap)
		
	def print_floor_plan(self):
		print("HEAP :", self.heap)
		
	def get_available_slot(self):
		try:
			return heappop(self.heap)
		except:
			return -1

	def fetch_slot(self, slot):
		"""
		Time complexity O(1).
		:param slot:
		:return:
		"""
		if slot in self.booked_slots:
			return self.booked_slots[slot].slot
		return None
	
	def fetch_slot_by_colour(self, color):

		fetch_array =[]
		for reg_no, vehicle in self.booked_slots.items():
			if vehicle.color == color:
				fetch_array.append(vehicle)
		return fetch_array

	def park_a_vehicle(self, reg_no, colour):
		"""

		:param reg_no: Registration number of particular vehicle
		:param color: Vehicle colour
		:return:
		"""
		
		slot = self.get_available_slot()
		if slot > -1:
			vehicle_obj = Vehicle(reg_no, slot, colour)
			self.booked_slots[reg_no] = vehicle_obj
			return True
		return False

	def unpark_a_vehicle(self, reg_no):
		"""

		:param reg_no:
		:return:
		"""
		slot = self.booked_slots[reg_no].slot
		del self.booked_slots[reg_no]
		heappush(self.heap, slot)


class Vehicle:

	def __init__(self, reg_no, slot, color=None):
		self.reg_no = reg_no
		self.color = color
		self.slot = slot
		self.type = 'bike' #


	def __del__(self):
		#TODO delete vehicle object once it out
		pass


def setup():
	parking = Parking()
	parking.park_a_vehicle(100, 'black')
	parking.park_a_vehicle(200, 'black')
	
	parking.unpark_a_vehicle(200)
	
	parking.fetch_slot(100)
	parking.fetch_slot_by_colour('black')
	
	parking.print_floor_plan()
	
setup()

