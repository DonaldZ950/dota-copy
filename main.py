import pygame
import tkinter as tk
import os
import signal
from goal import Goal
from player import Player
from tkinter import messagebox

from spinning_enemy import Spinning_Enemy
from stalker_enemy import Stalker_Enemy
from vertical_enemy import Vertical_Enemy
from diagonal_enemy import Diagonal_Enemy
SCREENW = 1200
SCREENH = 800
radius = 0
time = 0
ticks = 0
damage = 0
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)
root = tk.Tk()
root.withdraw()
def ask_yes_no(title, message):
   try:
       result = messagebox.askyesno(title, message)
       return result
   except tk.TclError as e:
       if "signal during handler" in str(e) or "Abort trap 6" in str(e):
           print("Encountered a 'trap 6' error. Exiting gracefully.")
           os.kill(os.getpid(), signal.SIGABRT)  # Abort the process
       else:
           print(f"An unexpected TclError occurred: {e}")
           return False  # Return False as a default

class Main:
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREENW,SCREENH))
        self.clock = pygame.time.Clock()
        self.new_game()
        self.game_loop()

    def new_game(self):
        # instantiate the game sprites
        self.player = Player(SCREENW, SCREENH, 10, 300)

        self.all_sprites = pygame.sprite.Group()
        self.all_sprites.add(self.player)
        self.goal = Goal(510, 300)
        self.goals = pygame.sprite.Group()
        self.all_sprites.add(self.goal)
        self.goals.add(self.goal)
        self.enemies = pygame.sprite.Group()



    def game_loop(self):
        running = True
        while running:
            # Process player inputs.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    raise SystemExit

            global ticks
            ticks = ticks + self.clock.get_time()

            global radius
            if(ticks < 1100):
                radius = (ticks)/1000 * 636.36363
            elif(ticks<2200):
                radius = (700 - (ticks-1100)/1000 * 636.36363)
            else:
                radius = 0
            if(self.goal.get_x() - self.player.get_x() - radius < 5 and self.goal.get_x() - self.player.get_x() - radius > -8):
                global damage
                print(radius)
                damage += radius * 0.2 + 45

            # Do logical updates here.
            if(pygame.key.get_focused()):
                pressed_keys = pygame.key.get_pressed()
                self.player.update(pressed_keys)
            # Erase the screen
            self.screen.fill("white")
            self.screen.blit(self.player.get_surf(), self.player.get_rectangle())
            for entity in self.all_sprites:
                self.screen.blit(entity.get_surface(), entity.get_rect())
            for enemy in self.enemies:
                enemy.update()
            for goal in self.goals:
                goal.update()

            if (ticks > 3000):
                messagebox.showinfo('You Win!', str(damage))
                running = False
                break
            pygame.draw.circle(self.screen, "Blue", (self.player.get_x(), self.player.get_y()), radius, 2)

            pygame.display.flip()  # Draw the screen
            if pygame.sprite.spritecollideany(self.player, self.enemies):
                messagebox.showinfo('You Lose!', 'You lost:( better luck next time')
                running = False
                break
            self.clock.tick(60)  # wait until next frame


if __name__ == "__main__":
    pygame.init()
    playing = True
    while playing:
        Main()
        if (ask_yes_no("fweoadsiofahewo", "fheaowfhodsjfojf")):
            playing = False
            break;
    pygame.quit()
    raise SystemExit
