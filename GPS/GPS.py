#!/usr/bin/env python
import serial
import operator

ser = serial.Serial(port = "/dev/ttyACM0", baudrate = 38400, timeout = 0.1)	

def GPSparser(data):
	gps_data = list()
	idx_rmc = data.find('GNRMC')
	if data[idx_rmc:idx_rmc+5] == "GNRMC":
		data = data[idx_rmc:]	
		print data
		if checksum(data):
			spliteddata = data.split(",")
			if spliteddata[2] == 'V':
				print "data invalid"		
	
			elif spliteddata[2] == 'A':
				gps_data.append(float(spliteddata[1]))
				if spliteddata[4] == 'N' :
					gps_data.append(float(spliteddata[3]))
				else:
					gps_data.append( -1.0*float(spliteddata[3]))
	
				if spliteddata[6] == 'E' :
					gps_data.append(float(spliteddata[5]))
				else:
					gps_data.append(-1.0*float(spliteddata[5]))
					
				if not spliteddata[7] == '':
					gps_data.append(float(spliteddata[7]))
				else :
					gps_data.append(-1.0)
				if not spliteddata[8] == '':
					gps_data.append(float(spliteddata[8]))
				else :
					gps_data.append(-1.0)
		
				return gps_data 
		else :
			print "checksum error"

def checksum(sentence):
	sentence = sentence.strip('\n')
	nmeadata, cksum = sentence.split('*',1)
	calc_cksum = reduce(operator.xor, (ord(s) for s in nmeadata), 0)
	print int(cksum,16), calc_cksum
	if int(cksum,16) == calc_cksum:
		return True 
	else:
		return False 

while 1: 
	data = ser.readline()
	gps_data  = GPSparser(data) 
	print gps_data 



	
