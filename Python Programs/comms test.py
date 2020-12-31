import serial

def send():
	ser = serial.Serial('COM3', 9600)

	i = 0

	while i < 5:
		val = input("Enter s to control LED: ")[0]
		val = bytes(val, 'utf-8')
		ser.write((val))
		print("Value: " + str(val, 'utf-8'))
		#print(ser.read())
		i += 1


def recieve():
	ser = serial.Serial('COM3', 9600)

	while True:
		val = str(ser.read(), 'utf-8')
		print(val)
		if (val == "-1"):
			break


userIn = input("Type 0 to send or 1 to recieve: ")
if (userIn == "1"):
	recieve()
else:
	send()
