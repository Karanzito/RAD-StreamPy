import serial
import serial.tools.list_ports

ports = serial.tools.list_ports.comports()
print(f"ports:\n{ports}") # list avalible ports

Ser = serial.Serial(port="COM4", baudrate=9600, timeout=2) # open port
Ser.write(b'connected!') # hello world

while True:
    line = Ser.readline()
    print(line) # print line in the console, for testing

    if line == 'BUTTON_1':
        print(f"{line} read successfully!")
        break

Ser.close() # close port