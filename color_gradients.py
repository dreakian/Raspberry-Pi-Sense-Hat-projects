# TO-DO:

# Modify this program so that it can display the color gradients of all colors, not just the color white

# Modify this program to correctly display in the terminal the final state of (0, 0, 0) for the LED Matrix RGB-color values

# Prompt the user to display the gradient in both directions (starting from the darkest shade to the lighest shade,
# instead of how it is now, which only starts at the brightest shade and then goes to the darkest shade)

# EVENTUAL/FOR FUN: Modify the program so that it can show gradient growth/gradient decline using random colors (goes from randomly bright shades
# to randomly dark shades) and display the corresponding LED Matrix RGB-color values

from sense_hat import SenseHat
from time import sleep

sense = SenseHat()

# variables that control for the RGB color values which will be displayed on the LED matrix

# IMPORTANT NOTE: based on how the code is written currently, this code only works with the color "white" (255, 255, 255).
# Using a different color, such as "red" (255, 0, 0) would cause an error and prevent the program from running as intended.
# Play around with some solutions, but basically the code needs to evaluate whether or not the color's RGB values are either all 255,
# which would mean white, or some combination of any number between 0 and 255 (but the brightest version of that color), in which case
# the logic below (the while loop) will need to be modified to reflect this. 

r = 255
g = 255
b = 255
program_over = (255, 0, 0)


# stores the initial LED Matrix RGB values as a variable in the form of a list
rgb = [r, g, b]

# initial state of the LED matrix, which is the brightest version of the color
e = (255, 255, 255) 

# the LED matrix
grid = [
    e, e, e, e, e, e, e, e,
    e, e, e, e, e, e, e, e,
    e, e, e, e, e, e, e, e,
    e, e, e, e, e, e, e, e,
    e, e, e, e, e, e, e, e,
    e, e, e, e, e, e, e, e,
    e, e, e, e, e, e, e, e,
    e, e, e, e, e, e, e, e
]

# displays the initial state of the LED matrix
sense.set_pixels(grid)

# conditional of the while loop
x = True

# the while loop is responsible for dynamically updating the LED matrix
while x:
    # first conditional loop that checks if the color can be reduced (reduce brightness)
    # if the color (brightness) can be reduced, it will be reduced
    if rgb[0] - 17 != 0 and rgb[1] - 17 != 0 and rgb[2] - 17 != 0:
        rgb[0] -= 17
        rgb[1] -= 17
        rgb[2] -= 17
        print("The color has been reduced.")
        print((rgb[0], rgb[1], rgb[2])) # prints the tuple version of the LED Matrix RGB color values
        sleep(0.5)
    # second conditional loop that checks if the color has been completely reduced (no more brightness)
    # if the color (brightness) cannot be reduced anymore, the while loop will end
    # the LED Matrix will display a "PROGRAM OVER" message and fully terminate the program
    elif rgb[0] - 17 == 0 and rgb[1] - 17 == 0 and rgb[2] - 17 == 0:
        x = False
        print("The color cannot be reduced anymore.")
        print((rgb[0], rgb[1], rgb[2]))
        sense.show_message("PROGRAM OVER", text_colour=program_over)
        sleep(1)
        sense.clear()
    
    # the updated LED matrix based on the first conditional loop      
    new_grid = [
    rgb, rgb, rgb, rgb, rgb, rgb, rgb, rgb,
    rgb, rgb, rgb, rgb, rgb, rgb, rgb, rgb,
    rgb, rgb, rgb, rgb, rgb, rgb, rgb, rgb,
    rgb, rgb, rgb, rgb, rgb, rgb, rgb, rgb,
    rgb, rgb, rgb, rgb, rgb, rgb, rgb, rgb,
    rgb, rgb, rgb, rgb, rgb, rgb, rgb, rgb,
    rgb, rgb, rgb, rgb, rgb, rgb, rgb, rgb,
    rgb, rgb, rgb, rgb, rgb, rgb, rgb, rgb 
    ]
    
    # updates the LED matrix with a slight delay to match with the delay from the first conditional loop
    sense.set_pixels(new_grid)
    sleep(0.5)
    
    

        
        
        
