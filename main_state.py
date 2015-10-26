import random
import json
import os

from pico2d import *

import game_framework
import title_state

name = "MainState"

hero = None
grass = None
font = None

def handle_events():
    global key_down_right
    global key_down_left

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                key_down_left = False
                key_down_right = True

            elif event.key == SDLK_LEFT:
                key_down_right = False
                key_down_left = True
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                key_down_left = False
                key_down_right = False

            elif event.key == SDLK_LEFT:
                key_down_right = False
                key_down_left = True




class Hero:
    image = None

    def __init__(self):
        self.x, self.y = 300, 125
        self.frame = random.randint(0, 3)
        self.image = load_image('hulk.png')

    def update(self):
        self.frame = (self.frame + 1) % 4

    def draw(self):
        self.image.clip_draw(self.frame * 200, 0, 200, 200, self.x, self.y)




class Background:
    def __init__(self):
        self.x, self.y = 400,300
        self.image = load_image('Background.png')

    def draw(self):
        self.image.draw(self.x, self.y)

class Grass:
    def __init__(self):
        self.image = load_image('grass.png')

    def draw(self):
        self.image.draw(400, 30)

class Block:

    def get_bb(self):
        return self.x - 50, self.y - 50, self.x + 50, self.y + 50
    def __init__(self):
        self.x, self.y = 400, 600
        self.image = load_image('block1.png')

    def draw(self):
        self.image.draw(self.x, self.y)
        if(self.y > 80):
            self.y -= 10

def enter():
    global hulk, grass, block, background
    background = Background()
    hulk = Hero()
    grass = Grass()
    block = Block()


def exit():
    global hero, grass, blcok, background
    del(hero)
    del(grass)
    del(block)
    del(background)

def pause():
    pass

def resume():
    pass


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.change_state(title_state)


def update():
    hero.update()
    delay (0.5)

def draw():
    clear_canvas()
    grass.draw()
    hero.draw()
    block.draw()
    background.draw()
    update_canvas()

def main():

    open_canvas()
    hero = Hero()
    background = Background()
    grass = Grass()
    block = Block()

    global running
    running = True

    while running:
        handle_events()
        hero.update()
        block.draw()

        clear_canvas()
        background.draw()
        grass.draw()
        block.draw()
        hero.draw()
        update_canvas()

        delay(0.06)



    close_canvas()

if __name__ == '__main__':
    main()



