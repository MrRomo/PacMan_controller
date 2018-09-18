import serial 


#Serial Controller
def serialKey(): 
    try:
        action = int(float(ser.read().strip()))
    except ValueError:
        action = 4
    return action
    
if __name__ == '__main__':
    while True:
        print(serialKey())