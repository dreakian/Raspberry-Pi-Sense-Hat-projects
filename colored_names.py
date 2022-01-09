from sense_hat import SenseHat

sense = SenseHat()

names = ["BOB", "JILL", "JACK", "SARAH"]

color_one = (227, 5, 101)
color_two = (255, 0, 0)
color_three = (8, 8, 255)
color_four = (153, 50, 204)
color_counter = (54, 166, 36)

counter = 0

while True:

    sense.show_message(names[0], text_colour=color_one)
    sense.show_message(names[1], text_colour=color_two)
    sense.show_message(names[2], text_colour=color_three)
    sense.show_message(names[3], text_colour=color_four)
    counter += 1
    sense.show_message(str(counter), text_colour=color_counter)

sense.clear()
