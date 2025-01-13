# Save on CPX/CPB as code.py
# Blinks the top right RED LED
import board
import digitalio
import time

led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT

def main():
    print(dir(board)) #board library
    print("----------------")
    print(dir(digitalio)) #digitalio library
    print("----------------")
    print(dir(led)) #variable "led"
    print("----------------")
    print(dir(digitalio.DigitalInOut)) #Attributes of "led"
    print("----------------")
    print(dir(led.direction)) #Attribute of "led.direction"
    print("----------------")
    print(dir(digitalio.Direction)) #Attribute of "digitalio.direction"
    
    # How does it blink?
    print("----------------")
    print (dir(led))
    print("----------------")
    print(dir(led.value))
    print(type(led.value))
    print(dir(board.LED))
    print(type(board.LED)) #LED is the Pin
    print("----------------")

main()

while True:
    led.value = True
    time.sleep(0.2) #Line 28 showed that it's a boolean
    led.value = False
    time.sleep(0.2)
