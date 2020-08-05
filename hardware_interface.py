import sys
import os

import gpiozero

ON = 1
OFF = 0

class pin_class(object):
	def __init__(self, LED_number):
		self.led_state = OFF
		if os.name == 'nt':
			print("On a windows system")
		else:
			self.led = gpiozero.LED(int(LED_number))
			print("Not on a windows system")

		#gpiozero.Device.pin_factory
		pass

	def setPinState(state):
		if state == ON:
			self.led_state = ON
			self.led.on()
		elif state == OFF:
			self.led_state = OFF
			self.led.off()
		else:
			print("How did you get there?!")

	def getPinState():
		if self.led_state == ON:
			print("LED status is ON")
		elif self.led_state == OFF:
			print("LED status is OFF")
		else:
			print("How did you get there?!")

		return self.led_state


#test = pin_class()