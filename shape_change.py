from sense_hat import SenseHat
from time import sleep
from random import choice
 
sense = SenseHat()

# colors that will be used for the "Rectangle" shape and its text prompt 
color_list = [(150, 51, 0), (255, 51, 51), (153, 214, 67), (44, 88, 222), (12, 64, 200), (123, 213, 32), (67, 76, 93),
              (120, 120, 120), (34, 43, 69), (9, 124, 67), (36, 99, 145), (54, 78, 133), (219, 193, 6), (0, 0, 79),
              (110, 42, 67), (111, 222, 32), (55, 99, 130), (178, 107, 246), (92, 84, 62), (239, 238, 227), (9, 8, 129)
              ]

# individual colors used for the "Square", "Triangle", "Octagon", "Cross", and "Heart" shapes as well as their respective text prompts.
g = (0, 51, 0)
b = (0, 0, 0)
r = (255, 0, 0)
p = (153, 0, 153) 
o = (255, 128, 0) 
h = (102, 0, 51)

# selects a random color from the "color_list" list
def random_color():
    return choice(color_list)

# while loop that infinitely displays the shapes and their respective prompts, with minimal delay between shapes
while True:

    sense.show_message("SQUARE", text_colour=g)

    square = [
        g, g, g, g, g, g, g, g,
        g, g, g, g, g, g, g, g,
        g, g, g, g, g, g, g, g,
        g, g, g, g, g, g, g, g,
        g, g, g, g, g, g, g, g,
        g, g, g, g, g, g, g, g,
        g, g, g, g, g, g, g, g,
        g, g, g, g, g, g, g, g
    ]

    sense.set_pixels(square)

    sleep(2)

    sense.show_message("TRIANGLE", text_colour=r)

    triangle = [
        b, b, b, b, b, b, b, b,
        b, b, b, r, r, b, b, b,
        b, b, r, r, r, r, b, b,
        b, r, r, r, r, r, r, b,
        r, r, r, r, r, r, r, r,
        r, r, r, r, r, r, r, r,
        r, r, r, r, r, r, r, r,
        b, b, b, b, b, b, b, b
    ]

    sense.set_pixels(triangle)

    sleep(2)

    sense.show_message("OCTAGON", text_colour=p)

    octagon = [
        b, b, p, p, p, p, b, b,
        b, p, p, p, p, p, p, b,
        p, p, p, p, p, p, p, p,
        p, p, p, p, p, p, p, p,
        p, p, p, p, p, p, p, p,
        p, p, p, p, p, p, p, p,
        b, p, p, p, p, p, p, b,
        b, b, p, p, p, p, b, b
    ]

    sense.set_pixels(octagon)

    sleep(2)

    
    rectangle_text = "RECTANGLE"
    
    for letter in rectangle_text:
        sense.show_message(letter, text_colour=random_color(), scroll_speed=0.05)
    
    rectangle = [
        b, b, random_color(), random_color(), random_color(), random_color(), random_color(), b,
        b, b, random_color(), random_color(), random_color(), random_color(), random_color(), b,
        b, b, random_color(), random_color(), random_color(), random_color(), random_color(), b,
        b, b, random_color(), random_color(), random_color(), random_color(), random_color(), b,
        b, b, random_color(), random_color(), random_color(), random_color(), random_color(), b,
        b, b, random_color(), random_color(), random_color(), random_color(), random_color(), b,
        b, b, random_color(), random_color(), random_color(), random_color(), random_color(), b,
        b, b, random_color(), random_color(), random_color(), random_color(), random_color(), b
    ]

    sense.set_pixels(rectangle)
    
    sleep(2)
    
    sense.show_message("CROSS", text_colour=o)
    
    cross = [
    b, b, b, o, o, b, b, b,
    b, b, b, o, o, b, b, b,
    b, o, o, o, o, o, o, b,
    b, o, o, o, o, o, o, b,
    b, b, b, o, o, b, b, b,
    b, b, b, o, o, b, b, b,
    b, b, b, o, o, b, b, b,
    b, b, b, o, o, b, b, b,
]
    
    sense.set_pixels(cross)
    
    sleep(2)
    
    sense.show_message("HEART", text_colour=h)
    
    heart = [
    b, h, h, b, b, h, h, b,
    h, h, h, h, h, h, h, h,
    h, h, h, h, h, h, h, h,
    h, h, h, h, h, h, h, h,
    b, h, h, h, h, h, h, b,
    b, b, h, h, h, h, b, b,
    b, b, b, h, h, b, b, b,
    b, b, b, b, b, b, b, b,
]
    
    sense.set_pixels(heart)
    
    sleep(2)
    
    sense.clear()
