import location, webbrowser
from scene import *
import scene, scene

def getLocation():
	location.start_updates()
	currLoc = location.get_location()
	location.stop_updates()
	return currLoc

def getStreetAddress(loc = getLocation()):
	return location.reverse_geocode(loc)[0]
	
street_address = '{Street},\n{City},\n{Country}'.format(**getStreetAddress())
map_URL = 'http://maps.google.com?q=' + street_address.replace(' ', '+')

class address(Scene):
	def setup(self):
		self.show_instructions = True
		self.p_size = 64 if self.size.w > 700 else 32
	
	def draw(self):
		background(0, 0, 0)
		s = 22 if self.size.w > 100 else 7
		text(street_address, 'Futura', s, *self.bounds.center().as_tuple())
		
	def should_rotate(self, orientation):
		return True	
		
run(address(), LANDSCAPE)
