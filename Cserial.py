import serial
import syslog
import time

port = '/dev/ttyUSB0' # note I'm using Mac OS-X


ard = serial.Serial(port,9600,timeout=5)
time.sleep(2) # wait for Arduino


while True:
#     sample = 3
    sample = input("Ingrese valor: ")
    ard.flush()
    data = str(sample)
    print ("Valor enviado desde Python: ")
    print (data)
#     ard.write(data.encode('ascii'))
#     time.sleep(1) # I shortened this to match the new value in your Arduino code

    # Serial read section
#     msg = ard.read(ard.inWaiting()).strip() # read all characters in buffer
#     print ("Valor devuelve arduino: ",msg)
#     i = i + 1
