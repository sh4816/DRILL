from pico2d import *
import math
winX, winY = 800, 600

open_canvas(winX, winY)

grass = load_image('grass.png')
character = load_image('character.png')

turn = 0
x, y = 400, 90

direction = 0
angle = 0
cx, cy = 400, 345
r = 255
        

while(1):
    clear_canvas_now()
    grass.draw_now(400, 30)
    if turn % 2 == 0:
        # 사각형 운동
        if direction % 4 == 0:
            if x >= winX:
                direction += 1
            else:
                x += 10
        elif direction % 4 == 1:
            if y >= winY:
                direction += 1
            else:
                y += 10
        elif direction % 4 == 2:
            if x <= 0:
                direction += 1
            else:
                x -= 10
        else:
            if y <= 90:
                if x < 400:
                    x += 10
                else:
                    direction += 1
                    turn += 1
            else:
                y -= 10
    else:
        # 원 운동
        if angle < 360:
            x = cx + r * math.cos((angle-90) * math.pi / 180)
            y = cy + r * math.sin((angle-90) * math.pi / 180)
            angle += 2
        else:
            angle = 0
            turn += 1

    character.draw_now(x, y)
    delay(0.02)
