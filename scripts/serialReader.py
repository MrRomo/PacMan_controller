import serial 
import serial.tools.list_ports as port_list


#Serial Controller
def lookPorts():
    ports = list(port_list.comports())
    for p in ports:
        print (p)

def readPorts():
    print("read ports")
    ports = list(port_list.comports())
    for p in ports:
        print (p)
        portDirection = p[0]
        ser = serial.Serial(portDirection, 9600)
        print(ser.name)
        print(portDirection)
        ser.write('a')     # write a string
        try:
            action = ser.read()
            if(action=='4'):
                print(action)
                return portDirection
            else:
                ser.close()
        except ValueError:
            pass


def serialKey(): 
    try:
        action = int(float(ser.read().strip()))
    except ValueError:
        action = 4
    return action

ser = serial.Serial(readPorts(), 9600)

if __name__ == '__main__':
    
    while True:
        print(serialKey())