import random
from pico2d import *
# import game_world
import game_framework

PIXEL_PER_METER = (100.0 / 0.09)  # 비둘기의 평균길이는 9cm: 100 pixel 10 cm
FLY_SPEED_KMPH = 20.0            # 앵무새가 천천히 비행할때의 평균 속도는 45Km/H
FLY_SPEED_MPM = (FLY_SPEED_KMPH * 1000.0 / 60.0)
FLY_SPEED_MPS = (FLY_SPEED_MPM / 60.0)
FLY_SPEED_PPS = (FLY_SPEED_MPS * PIXEL_PER_METER)

# Bird Action Speed
TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 8


class Bird:
    image = None

    def __init__(self):
        if self.image == None:
            self.image = load_image('bird100x100x14.png')

        self.x, self.y = random.randint(100, 1500-1), random.randint(200, 500-1)
        self.dir = 1
        self.velocity = FLY_SPEED_PPS
        self.frame = 0

    def draw(self):
        self.image.clip_draw(int(self.frame) * 100, 0, 100, 100, self.x, self.y)

    def update(self):
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 14

        self.x += self.velocity * game_framework.frame_time  # S = V * T

        if self.x <= 50:
            self.dir = 1
        elif self.x >= 1550:
            self.dir = -1

        self.velocity = self.dir * FLY_SPEED_PPS