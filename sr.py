import serial
import serial.tools.list_ports
import asyncio
# from playsound3 import playsound # DEPRICATED!

# # Connect your ESP32(or Arduino) and insert their port:
# Port = "COM5"
# Insert your baudrate here (default: 11500):
Baudrate = 11500

def connect_port():
    ports = serial.tools.list_ports.comports()
    print("Avalible Ports:")

    if not ports:
        print("No avalible COM ports found.")
        return None
    
    for p in ports:
        print(f"Trying {p.device}")

        try:

            ser = serial.Serial(port=p.device, baudrate=Baudrate, timeout=2)

            ser.write(b'connected!')

            print(f"connected on {p.device}")
            return ser
        
        except serial.SerialException:
            print(f"Fail to open {p.device}.")
    
    return None

def Main():
    ser = connect_port()

    if ser is None:
        raise Exception("No valid Serial Port found.")

    while True:
        line = ser.readline()
        line = line.decode('utf-8').strip() # convert to string
        if len(line) > 0:
            print(f"> {line}") # print line in the console, for testing

        if line == 'BTN_1':
            # playsound(r'.\sounds\gawr-gura.mp3') # test button input
            print("soud played!")


if __name__ == '__main__':
    Main()

class Module_SR:

    async def read_serial():

        ser = connect_port()

        if ser is None:
            raise Exception("No valid Serial Port found.")
        
        timeout = 60
        
        while timeout > 0:
            line = ser.readline()
            line = line.decode('utf-8').strip() # convert to string
            if len(line) > 0:
                bind = line
                print(f"new bind = '{bind}'")

                return bind
            
            else:
                timeout -=1
                await asyncio.sleep(0.5)

        
        return None