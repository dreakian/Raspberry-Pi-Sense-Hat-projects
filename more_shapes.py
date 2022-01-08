from sense_hat import SenseHat
from time import sleep

sense = SenseHat()

word_list = ["HEART", "TREE", "WORLD", "COOKIE"]

word_colors = [(204, 0, 102), (0, 255, 0), (255, 102, 178), (204, 102, 0)]

# x = (102, 51, 0)
# y = (255, 154, 0)
# z = (51, 25, 0)

b = (0, 0, 0)
y = (255, 154, 0)
z = (51, 25, 0)
h = (204, 0, 102)
w = (255, 255, 255)
g = (0, 255, 0)
r = (255, 0, 0)
db = (0, 0, 255)
br = (102, 51, 0)

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

tree = [
    b, b, g, g, g, b, b, b,
    b, g, g, r, g, g, b, b,
    b, g, g, g, g, g, b, b,
    b, b, g, g, g, b, b, b,
    b, b, b, br, b, b, b, b,
    b, b, b, br, b, b, b, b,
    b, b, b, br, b, b, b, b,
    b, b, b, br, b, b, b, b,
]

world = [
    b, db, w, w, w, db, db, b,
    db, db, db, db, w, w, db, db,
    w, db, g, g, db, db, db, db,
    db, g, g, g, g, db, db, w,
    db, db, g, g, db, db, w, db,
    db, db, db, g, db, db, g, db,
    db, db, db, db, db, g, g, db,
    b, db, w, db, db, db, db, b,
    
]



cookie = [
    b, b, y, y, y, y, b, b,
    b, y, y, y, y, z, y, b,
    y, z, y, z, y, y, y, y,
    y, y, y, y, y, y, y, y,
    y, y, y, y, y, z, y, y,
    y, y, z, y, y, y, y, y,
    b, y, y, y, y, z, y, b,
    b, b, y, y, y, y, b, b
]


def display_heart():
    sense.show_message(word_list[0], text_colour=word_colors[0])
    sense.clear()
    sense.set_pixels(heart)
    sleep(1.5)

def display_tree():
    sense.show_message(word_list[1], text_colour=word_colors[1])
    sense.clear()
    sense.set_pixels(tree)
    sleep(1.5)


def display_world():
    sense.show_message(word_list[2], text_colour=word_colors[2])
    sense.clear()
    sense.set_pixels(world)
    sleep(1.5)

def display_cookie():
    sense.show_message(word_list[3], text_colour=word_colors[3])
    sense.clear()
    sense.set_pixels(cookie)
    sleep(1.5)

while True:

    display_heart()
    display_tree()
    display_world()
    display_cookie()

    sense.show_message("LOVE", text_colour=(255, 0, 0))
    

    