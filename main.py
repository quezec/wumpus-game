import pygame

from config import *
from lib.Player import Player
from lib.GameMap import GameMap
from lib.helpers import Direction


pygame.init()

# Set up window & FPS clock
clock = pygame.time.Clock()

pygame.display.set_caption("wumpus game")
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

# Create objects and changed_rects
player = Player((WINDOW_WIDTH/2, WINDOW_HEIGHT/2))

background = pygame.image.load('assets/grokwallpaper.png').convert()

# Initialize map
map = GameMap()

all = pygame.sprite.OrderedUpdates() #renders sprites in ORDER OF ADDITION
all.add(player)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            break

    # Level Handling
    direction_exited = map.check_player_exited(player.rect)
    if direction_exited:
        x_change, y_change = direction_exited
        player.rect.x -= x_change * (WINDOW_WIDTH + 15)
        player.rect.y -= y_change * (WINDOW_HEIGHT + 15)
        map.move_player(direction_exited)

    all.clear(window, background)
    all.update()
    all.add(player.friendly_bullets)

    rects = all.draw(window)
    pygame.display.update([pygame.Rect(rect.x - 20, rect.y - 20, rect.width + 40, rect.height + 40) for rect in rects])

    clock.tick(FPS)

pygame.quit()
