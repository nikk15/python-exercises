"""
A simple reservation system for guests to book seats on a plane 
and for an airline to keep track of a plane's capacity to prevent
overbooking.
"""

class Seat:

	def __init__(self, total_seats):
		self.total_seats = total_seats

	def __str__(self):
		return f'{self.total_seats}'

	def book(self, num_seats):
		#subtract number of seats booked from the total seats available
		if self.total_seats >= num_seats:
			self.total_seats -= num_seats
		else:
			print ('Unavailable - this class is fully booked.')

	def seats_avail():
		return self.total_seats

class Economy(Seat):

	def __init__(self, total_seats = 120):
		super().__init__(total_seats = 120)

	def __str__(self):
		return f'Economy'

class Business(Seat):

	def __init__(self, total_seats = 30):
		super().__init__(total_seats = 30)

	def __str__(self):
		return f'Business'

class FirstClass(Seat):

	def __init__(self, total_seats = 10):
		super().__init__(total_seats = 10)

	def __str__(self):
		return f'First'

class Guest:
    
	def __init__(self, name, seats_held = 0, class_held = ''):
		self.name = name
		self.seats_held = seats_held
		self.class_held = class_held

	def __str__(self):
		return f'{self.name}: {self.seats_held} {self.class_held} seats confirmed'


def book_seat(class_type, num_seats, guest):
    #add number of seats and class booked to guest's attributes
	class_type.book(num_seats)
	if class_type.total_seats >= num_seats:
		guest.seats_held += num_seats
		guest.class_held = class_type
	print(f'{guest.__str__()}')


def plane_capacity(plane):
    #display remaining availability
	print(f'Current plane capacity:\nFirst - {plane["first"].total_seats}\nBusiness - {plane["business"].total_seats}\nEconomy - {plane["economy"].total_seats}')


# Next additions include airline and flight number
# airbus = {
#     "economy": Economy(),
#     "business": Business(),
#     "first": FirstClass()
# }
#This could be expanded to a full fledged application with a SQL database.


