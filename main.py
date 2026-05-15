import serial
import serial.tools.list_ports

# Connect your ESP32(or Arduino) and insert their port:
Port = "COM6"
# Insert your baudrate here (default: 11500):
Baudrate = 11500

ports = serial.tools.list_ports.comports()
print("Avalible Ports:")
for p in ports:
    print(p.device) # list avalible ports

try:
    Ser = serial.Serial(port=Port, baudrate=Baudrate, timeout=2) # open port
    Ser.write(b'connected!') # hello world

except serial.serialutil.SerialException as e:
    raise Exception(f"Port '{Port}' Not Found")
    

while True:
    line = Ser.readline()
    line = line.decode('utf-8').strip() # convert to string
    print(f"> {line}") # print line in the console, for testing

    if line == 'BUTTON_1':
        print(f"{line} read successfully!")
        break
    
    elif line == 'BUTTON_2':
        print(f"{line} read successfully!")
        break
    
    elif line == 'BUTTON_3':
        print(f"{line} read successfully!")
        break

Ser.close() # close port    