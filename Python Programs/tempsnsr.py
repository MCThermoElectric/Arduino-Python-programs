import serial

import time

def openFile(fileName):
	dataFile = open(fileName + str(time.time()) + ".csv", "w")
	return dataFile
	

def collectLine(inputDevice):
	# Loop an infinite amount of time. ctrl + C can be used to stop the program.
	while True:
		# Read the next available character from the arduino (in bytes), and convert it to a string using utf-8 encoding
		val = str(inputDevice.read(), 'utf-8')
		fullLine = ""
		line1 = ""
		# Loop thru each line. Each character is collected into a variable and then added to the fullLine variable. The loop stops when a newline is detected.
		while val != '\n':
			fullLine += val
			val = str(inputDevice.read(), 'utf-8')
		# return the full line that was read from the arduino
		#print(fullLine)
		fullLine = fullLine[:-2]
		print(fullLine)
		return fullLine

def writeLineToFile(line, file):
	file.write(line + "\n")

arduino = serial.Serial('COM3', 9600)
dataFile = openFile("datafile")

time1 = time.time()
writeLineToFile("time,sensor1,sensor2,sensor3", dataFile)

for i in range(0, 15):
	line = collectLine(arduino)
	#print(line)
	writeLineToFile(str(time.time()) + "\t" + line, dataFile)

print("Total time taken: " + str(time.time() - time1))
dataFile.close()
