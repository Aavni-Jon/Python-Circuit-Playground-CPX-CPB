# Save on CPX/CPB as code.py
# Blinks the top right RED LED
import board
import digitalio
import time

led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT

def main():
    print(dir(board))
    print("----------------")
    print(dir(digitalio))
    print("----------------")
    print(dir(led))
    print("----------------")
    print(dir(digitalio.DigitalInOut))
    print("----------------")
    print(dir(led.direction))
    print("----------------")
    print(dir(digitalio.Direction))
    print("----------------")
    print (dir(led))
    print("----------------")
    print(dir(led.value))
    print(type(led.value))
    print(dir(board.LED))
    print(type(board.LED))
    print("----------------")

main()

while True:
    led.value = True
    time.sleep(0.1)
    led.value = False
    time.sleep(0.1)
