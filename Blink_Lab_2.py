# Save on CPX/CPB as code.py
# Blinks the top right RED LED
import board
import digitalio

#reference the LED
led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT

#giving button_B its attributes
button_B = digitalio.DigitalInOut(board.BUTTON_B)
button_B.direction = digitalio.Direction.INPUT
button_B.pull = digitalio.Pull.DOWN #Effect happens when pushed


def main():
    print(dir(board)) #board library
    print("----------------")
   
    #finding the attributes for button_B
    print(dir(digitalio)) 
    print(dir(digitalio.DigitalInOut))
    print(dir(digitalio.Direction))
    #giving button_B its attributes line 10-13
    print(dir(digitalio.Pull)) 
    
    print("Button_B Input/Output Example")
    print("Push Button_B (Right Button)")

main()

'''
while True: #Purpose of this syntax: b/c while loops run only once
    while button_B.value: #LED will be on forever after button_B is first pressed
        led.value = True
    
    led.value = False
'''
while True:
    led.value = button_B.value

    
    
