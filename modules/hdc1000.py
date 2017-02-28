# Library for the temperature and humidity sensor
#  ----> https://www.adafruit.com/products/2635

import time
from pprint import pprint
import i2c

I2CADDR			= 0x40

TEMP_REG		= 0x00
HUMID_REG		= 0x01
CONFIG_REG		= 0x02

CONFIG_RESET		= (1 << 15)
CONFIG_HEAT		= (1 << 13)
CONFIG_MODE_SINGLE	= 0
CONFIG_MODE_BOTH	= (1 << 12)
CONFIG_BATT		= (1 << 11)
CONFIG_TRES_14		= 0
CONFIG_TRES_11		= (1 << 10)
CONFIG_HRES_14		= 0
CONFIG_HRES_11		= (1 << 8)
CONFIG_HRES_8		= (1 << 9)

SERIAL1			= 0xFB
SERIAL2			= 0xFC
SERIAL3			= 0xFD
MANUFID			= 0xFE
DEVICEID		= 0xFF

bus = i2c.IIC(I2CADDR, 1)

def reset(extra = 0):
	config = (
		CONFIG_RESET |
		CONFIG_MODE_SINGLE |
		CONFIG_TRES_14 |
		CONFIG_HRES_14 |
		extra
	)
	bus.i2c([CONFIG_REG, config >> 8, config & 0xff], 0)
	time.sleep(0.2)

def temperature():
	# Request temperature measurement
	bus.i2c([TEMP_REG], 0)

	time.sleep(0.2)

	data = bus.read(2)
	temp = (data[0] << 8) | data[1]
	#print(hex(temp))
	return (temp / 65536.0) * 165.0 - 40

def humidity():
	# Request humidity measurement
	bus.i2c([HUMID_REG], 0)

	time.sleep(0.2)

	data = bus.read(2)
	hum = (data[0] << 8) | data[1]
	#print(hex(hum))
	return (hum / 65536.0) * 100.0

def drySensor():
	# Turn on the heater
	reset(CONFIG_HEAT)

	# Take 1000 reading as fast as possible
	# (the heater is only activated when performing a reading)
	for x in range(1000):
		try:
			temperature()
		except: pass

	# Turn off the heater
	reset()

def init():
	reset()

def done():
	global bus
	bus.close()
	del bus

