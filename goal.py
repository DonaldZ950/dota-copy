import pygame

WIDTH     =  50
HEIGHT    =  50

class Goal(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super(Goal, self).__init__()
        self.surf = pygame.Surface((WIDTH, HEIGHT))
        self.surf.fill("Green")
        self.rect = self.surf.get_rect()
        self.rect.x = x
        self.rect.y = y

    def get_surface(self):
        return self.surf

    def get_rect(self):
        return self.rect
    def get_x(self):
        return self.rect.x
    def get_y(self):
        return self.rect.y
    def update(self):
        self.rect.move_ip(5, 0)