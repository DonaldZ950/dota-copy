import pygame

SPEED  =  3.0
WIDTH  = 10
HEIGHT = 10
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_CLEAR,
)

UP = K_UP
DOWN = K_DOWN
LEFT = K_LEFT
RIGHT = K_RIGHT
CLEAR = K_CLEAR

class Player(pygame.sprite.Sprite):
    def __init__(self, screen_w, screen_h, x, y):
        super(Player, self).__init__()
        self.surf = pygame.Surface((WIDTH, HEIGHT))
        self.surf.fill("Black")
        self.surface = pygame.Surface((700, 700))
        self.surface.fill("White")
        self.rectangle = self.surface.get_rect()
        self.rectangle.x = x - 350
        self.rectangle.y = y - 350
        self.rect = self.surf.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.screen_w = screen_w
        self.screen_h = screen_h


    def get_surface(self):
        return self.surf
    def get_rect(self):
        return self.rect
    def get_rectangle(self):
        return self.rectangle
    def get_surf(self):
        return self.surface
    def get_x(self):
        return self.rect.x + 5
    def get_y(self):
        return self.rect.y + 5

    # Move the sprite based on user keypresses
    def update(self, pressed_keys):
        self.rect.move_ip(4.75, 0)



