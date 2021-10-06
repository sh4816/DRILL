from pico2d import *
from random import randint

KPU_WIDTH, KPU_HEIGHT = 1280, 1024

hand_x, hand_y = randint(0, KPU_WIDTH) // 2, randint(0, KPU_HEIGHT) // 2

print(hand_x, hand_y)

def handle_events():
    # fill here
    global running
    global x, y
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        # elif event.type == SDL_MOUSEMOTION:
        #     x, y = event.x, KPU_HEIGHT - 1 - event.y
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False
        elif event.type == SDL_MOUSEBUTTONDOWN:
            print(event.x, event.y)
    pass

def following_hand():
    global following
    global x, y
    global hand_x, hand_y
    global difference_x, difference_y

    if following == False:
        hand_x, hand_y = randint(0, KPU_WIDTH), randint(0, KPU_HEIGHT)
        difference_x, difference_y = x - hand_x, y - hand_y
        following = True
    else:
        if (abs(hand_x - x) <= 10):
            if (abs(hand_y - y) <= 10):
                following = False
        else:
            if x > hand_x:
                x -= difference_x / 1000
            elif x < hand_x:
                x += difference_x / 1000

            if y > hand_y:
                y -= difference_y / 1000
            else:
                y += difference_y / 1000

open_canvas(KPU_WIDTH, KPU_HEIGHT)

# fill here
kpu_ground = load_image('KPU_GROUND.png')
character = load_image('animation_sheet.png')
hand_arrow = load_image('hand_arrow.png')

running = True
following = True
x, y = KPU_WIDTH // 2, KPU_HEIGHT // 2
frame = 0
hide_cursor()

difference_x, difference_y = x - hand_x, y - hand_y

while running:
    clear_canvas()
    kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
    character.clip_draw(frame * 100, 100 * 1, 100, 100, x, y)

    hand_arrow.draw(hand_x, hand_y)

    following_hand()
    update_canvas()
    frame = (frame + 1) % 8

    handle_events()

close_canvas()
