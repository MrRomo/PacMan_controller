import serial
ser = serial.Serial('/dev/ttyACM1', 9600)
while True:
    move =ser.readline()
    print(move)
    type(move) is int
