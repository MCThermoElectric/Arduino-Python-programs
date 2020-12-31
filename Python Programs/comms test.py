import serial
# This method will send a command to a listening arduino that will trigger the arduino to turn the built in LED on and then off again
def send():
	# Connect to the serial port (in this case, COM3)
	ser = serial.Serial('COM3', 9600)

	i = 0
	# Loop thru the following 5 times. this is purely for convenience's sake. This could run once or 100000000 times and it would not matter.
	while i < 5:
		# Get an input from the user and select only the first character
		val = input("Enter s to control LED: ")[0]
		# Convert the character to bytes using utf-8 encoding. This seems to be the encoding that the arduino uses as well.
		val = bytes(val, 'utf-8')
		# Write those bytes to the serial monitor
		ser.write((val))
		# Again, this is purely for convenice.
		i += 1

# This method will recieve strings in full lines from the arduino
def recieve():
	# Connect to the serial port (in this case, COM3)
	ser = serial.Serial('COM3', 9600)

	# Loop an infinite amount of time. ctrl + C can be used to stop the program.
	while True:
		# Read the next available character from the arduino (in bytes), and convert it to a string using utf-8 encoding
		val = str(ser.read(), 'utf-8')
		fullLine = ""
		# Loop thru each line. Each character is collected into a variable and then added to the fullLine variable. The loop stops when a newline is detected.
		while val != '\n':
			fullLine += val
			val = str(ser.read(), 'utf-8')
		# Print the full line that was read from the arduino
		print(fullLine)

# Get a user's input as to whether they wish to send data or recieve data from the arduino
userIn = input("Type 0 to send or 1 to recieve: ")
# Check the user input and run the correct method
if (userIn == "1"):
	recieve()
elif (userIn == "0"):
	send()
# In case the user enters anything other than 0 or 1
else:
	print("Invalid input")
