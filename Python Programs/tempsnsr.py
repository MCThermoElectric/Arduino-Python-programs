import serial

arduino = serial.Serial('COM3', 9600)

# Loop an infinite amount of time. ctrl + C can be used to stop the program.
while True:
	# Read the next available character from the arduino (in bytes), and convert it to a string using utf-8 encoding
	val = str(arduino.read(), 'utf-8')
	fullLine = ""
	line1 = ""
	# Loop thru each line. Each character is collected into a variable and then added to the fullLine variable. The loop stops when a newline is detected.
	while val != '\n':
		fullLine += val
		val = str(arduino.read(), 'utf-8')
	    # Print the full line that was read from the arduino
	line1 = fullLine.strip().split("!")
	line1.pop()
	print(fullLine)
	print(line1)
