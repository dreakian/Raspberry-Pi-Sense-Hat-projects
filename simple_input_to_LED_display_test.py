from sense_hat import SenseHat
from time import sleep

sense = SenseHat()

while True:

    selection = input(f"""
        Select a color:
            1. Red
            2. Blue
            3. Green
            4. White

    """)

    r = (255, 0, 0)
    b = (0, 0, 255)
    g = (0, 204, 0)
    w = (255, 255, 255)
    error_color = (255, 255, 0)

    if selection == str(1):
        print("You have chosen the color red.")
        sense.show_message("RED", text_colour=r)

    elif selection == str(2):
        print("You have chosen the color blue.")
        sense.show_message("BLUE", text_colour=b)
        
    elif selection == str(3):
        print("You have chosen the color green.")
        sense.show_message("GREEN", text_colour=g)
        
    elif selection == str(4):
        print("You have chosen the color white.")
        sense.show_message("WHITE", text_colour=w)
        
    else:
        print("You have made an invalid selection.")
        sense.show_message("ERROR", text_colour=error_color)
        
    sense.clear()

    sleep(2)