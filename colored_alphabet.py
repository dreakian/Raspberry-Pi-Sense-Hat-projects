from sense_hat import SenseHat
from random import randint
from time import sleep

sense = SenseHat()

alphabet = ["A", "B", "C", "D", "E", "F", "G", "H",
"I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T",
"U", "V", "W", "X", "Y", "Z"]

def random_color():
    rand_red = randint(0, 255)
    rand_green = randint(0, 255)
    rand_blue = randint(0, 255)
    return (rand_red, rand_green, rand_blue)

while True:

    for letter in alphabet:
        sense.show_letter(letter, random_color())
        sleep(0.85)
      
sense.clear()