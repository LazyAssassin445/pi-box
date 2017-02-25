# Library for the temperature and humidity sensor
#  ----> https://www.adafruit.com/products/2635

from pprint import pprint
try:
	import smbus2 as smbus
except ImportError:
	import smbus

I2CADDR			= 0x40

TEMP_REG		= 0x00
HUMID_REG		= 0x01
CONFIG_REG		= 0x02

CONFIG_RST		= (1 << 15)
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

try:
	bus = smbus.SMBus(1)
except:
	print("No I2C bus found.")

def reset():
	config = (
		CONFIG_RST |
		CONFIG_MODE_BOTH |
		CONFIG_TRES_14 |
		CONFIG_HRES_14
	)
	bus.write_word_data(I2CADDR, CONFIG_REG, config)

def triggerMeasurements():
	bus.write_byte(I2CADDR, TEMP_REG)

def readTemperature():
	vals = bus.read_i2c_block_data(I2CADDR, TEMP_REG)
	pprint(vals)
	#float temp = (read32(HDC1000_TEMP, 20) >> 16);
	#temp /= 65536;
	#temp *= 165;
	#temp -= 40;

	#return temp;

def readHumidity():
	vals = bus.read_i2c_block_data(I2CADDR, HUMID_REG)
	pprint(vals)
	#float hum = (read32(HDC1000_TEMP, 20) & 0xFFFF);
	#hum /= 65536;
	#hum *= 100;

	#return hum;

def drySensor():
	origconfig = bus.read_word_data(I2CADDR, CONFIG_REG)
	newconfig = (
		CONFIG_RST |
		CONFIG_HEAT |
		CONFIG_MODE_BOTH |
		CONFIG_TRES_14 |
		CONFIG_HRES_14
	)

	bus.write_word_data(I2CADDR, CONFIG_REG, newconfig)

	sleep(0.1)

	# Take 1000 readings
	for x in range(0, 1000):
		triggerMeasurements()
		sleep(0.1)

	sleep(0.1)

	origconfig |= CONFIG_RST;
	bus.write_word_data(I2CADDR, CONFIG_REG, origconfig)

def init():
	reset()
	manuf = bus.read_word_data(I2CADDR, MANUFID)
	dev = bus.read_word_data(I2CADDR, DEVICEID)
	print("Manufacturer:", manuf, "Device:", dev)

