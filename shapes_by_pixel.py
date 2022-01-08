#notes

# create shapes 

# each shape will be created pixel-by-pixel 

# pixel-creation will in random color

from sense_hat import SenseHat
from time import sleep
from random import choice

sense = SenseHat()

b = (0, 0, 0)
w = (255, 255, 255)

# red = (255, 0, 0)
# blue = (26, 0, 255)
# green = (13, 191, 36)
# yellow = (230, 255, 0)
# orange = (255, 94, 0)
# purple = (100, 31, 179)
# white = (255, 255, 255)

color_list = [(255, 0, 0), (26, 0, 255), (100, 31, 179), (13, 191, 36), (230, 255, 0), (255, 94, 0), (255, 255, 255)]

def random_color_from_list():
    return choice(color_list)


# 
# def random_color():
#     rand_r = randint(0, 255)
#     rand_g = randint(0, 255)
#     rand_b = randint(0, 255)
#     return (rand_r, rand_g, rand_b)

counter = 0

# square_pixels = [
#     w, w, w, w, w, w, w, w,
#     w, b, b, b, b, b, b, w,
#     w, b, b, b, b, b, b, w,
#     w, b, b, b, b, b, b, w,
#     w, b, b, b, b, b, b, w,
#     w, b, b, b, b, b, b, w,
#     w, b, b, b, b, b, b, w,
#     w, w, w, w, w, w, w, w    
# ]
# 
# sense.set_pixels(square_pixels)

# sense.clear()

while True:

    sense.show_message("SQUARE", text_colour=random_color_from_list())
    sleep(1)
    
    sense.clear()

    sense.set_pixel(0, 0, random_color_from_list())
    sleep(0.1)
    sense.set_pixel(0, 1, random_color_from_list())
    sleep(0.1)
    sense.set_pixel(0, 2, random_color_from_list())
    sleep(0.1)
    sense.set_pixel(0, 3, random_color_from_list())
    sleep(0.1)
    sense.set_pixel(0, 4, random_color_from_list())
    sleep(0.1)
    sense.set_pixel(0, 5, random_color_from_list())
    sleep(0.1)
    sense.set_pixel(0, 6, random_color_from_list())
    sleep(0.1)
    sense.set_pixel(0, 7, random_color_from_list())
    sleep(0.1)
    sense.set_pixel(1, 7, random_color_from_list())
    sleep(0.1)
    sense.set_pixel(2, 7, random_color_from_list())
    sleep(0.1)
    sense.set_pixel(3, 7, random_color_from_list())
    sleep(0.1)
    sense.set_pixel(4, 7, random_color_from_list())
    sleep(0.1)
    sense.set_pixel(5, 7, random_color_from_list())
    sleep(0.1)
    sense.set_pixel(6, 7, random_color_from_list())
    sleep(0.1)
    sense.set_pixel(7, 7, random_color_from_list())
    sleep(0.1)
    sense.set_pixel(7, 6, random_color_from_list())
    sleep(0.1)
    sense.set_pixel(7, 5, random_color_from_list())
    sleep(0.1)
    sense.set_pixel(7, 4, random_color_from_list())
    sleep(0.1)
    sense.set_pixel(7, 3, random_color_from_list())
    sleep(0.1)
    sense.set_pixel(7, 2, random_color_from_list())
    sleep(0.1)
    sense.set_pixel(7, 1, random_color_from_list())
    sleep(0.1)
    sense.set_pixel(7, 0, random_color_from_list())
    sleep(0.1)
    sense.set_pixel(6, 0, random_color_from_list())
    sleep(0.1)
    sense.set_pixel(5, 0, random_color_from_list())
    sleep(0.1)
    sense.set_pixel(4, 0, random_color_from_list())
    sleep(0.1)
    sense.set_pixel(3, 0, random_color_from_list())
    sleep(0.1)
    sense.set_pixel(2, 0, random_color_from_list())
    sleep(0.1)
    sense.set_pixel(1, 0, random_color_from_list())
    sleep(0.1)
    
    sense.clear()
     
    sense.show_message("CIRCLE", text_colour=random_color_from_list())
    sleep(1)

    sense.set_pixel(0, 2, random_color_from_list())
    sleep(0.1)
    sense.set_pixel(0, 3, random_color_from_list())
    sleep(0.1)
    sense.set_pixel(0, 4, random_color_from_list())
    sleep(0.1)
    sense.set_pixel(0, 5, random_color_from_list())
    sleep(0.1)
    sense.set_pixel(1, 6, random_color_from_list())
    sleep(0.1)
    sense.set_pixel(2, 7, random_color_from_list())
    sleep(0.1)
    sense.set_pixel(3, 7, random_color_from_list())
    sleep(0.1)
    sense.set_pixel(4, 7, random_color_from_list())
    sleep(0.1)
    sense.set_pixel(5, 7, random_color_from_list())
    sleep(0.1)
    sense.set_pixel(6, 6, random_color_from_list())
    sleep(0.1)
    sense.set_pixel(7, 5, random_color_from_list())
    sleep(0.1)
    sense.set_pixel(7, 4, random_color_from_list())
    sleep(0.1)
    sense.set_pixel(7, 3, random_color_from_list())
    sleep(0.1)
    sense.set_pixel(7, 2, random_color_from_list())
    sleep(0.1)
    sense.set_pixel(6, 1, random_color_from_list())
    sleep(0.1)
    sense.set_pixel(5, 0, random_color_from_list())
    sleep(0.1)
    sense.set_pixel(4, 0, random_color_from_list())
    sleep(0.1)
    sense.set_pixel(3, 0, random_color_from_list())
    sleep(0.1)
    sense.set_pixel(2, 0, random_color_from_list())
    sleep(0.1)
    sense.set_pixel(1, 1, random_color_from_list())
    sleep(0.1)
    sense.set_pixel(0, 1, random_color_from_list())

    sense.clear()
    
    counter += 1
    
    sense.show_message(str(counter), text_colour=random_color_from_list())












