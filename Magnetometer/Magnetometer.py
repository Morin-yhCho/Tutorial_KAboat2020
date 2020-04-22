#!/usr/bin/env python
from lis3mdl import LIS3MDL

magnet = LIS3MDL()
magnet.enableLIS()

while 1:
	data_raw = magnet.getMagnetometerRaw()
	print data_raw

