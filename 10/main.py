from pico2d import *
from random import *

# Game object class here
class Balls():
    def __init__(self):
        self.x, self.y = randint(0, 800), 599
        load_image('ball21x21.png')
        self.len = 21
        if randint(0, 1) == 0:
            load_image('ball41x41.png')
            self.len = 41

    def update(self):
        if not self.y <= 20:
            self.y -= randint(0, 10)
        else:
            self.y = 20

        Image.draw(self, self.x, self.y, self.len, self.len)



def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

# initialization code
running = True

# game main loop code
open_canvas()

grass = load_image('grass.png')

ball1 = Balls()

while (running):
    clear_canvas()
    handle_events()
    grass.draw(400, 20)

    ball1.update()

    update_canvas()

    delay(0.01)