from datetime import datetime

class clock():
	"""docstring for ClassName"""
	def __init__(self):
		super(clock, self).__init__()
		now = datetime.now()
		self.current_time = now.strftime("%H:%M")
		print("Current Time =", self.current_time)

	def getCurrentTime(self):
		now = datetime.now()
		self.current_time = now.strftime("%H:%M")
		print("Current Time =", self.current_time)
		return self.current_time



#if __name__ == "__main__":
#    import sys
#    BrewClock = clock()
