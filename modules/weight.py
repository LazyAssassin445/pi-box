#!/usr/bin/python

import spidev
import time
import os

spi = spidev.SpiDev()
spi.open(0, 0)

def readchannel(channel):
	adc = spi.xfer2([1, (8+channel)<<4, 0])
	data = ((adc[1]&3)<<8) + adc[2]
	return data

