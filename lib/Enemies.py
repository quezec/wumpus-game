import pygame

from lib.Player import Bullet, Player
from lib.helpers import BaseSprite
from lib.Obstacles import Wall


class BaseEnemy(BaseSprite):
    """Used to check if a sprite is an enemy or not."""


class TestEnemy(BaseEnemy):
    def __init__(self, center=(0, 0)):
        super().__init__(image_path='assets/enemy.png', center=center)
        self.hp = 1

    def update(self, all_sprites, player):
        bullets = [sprite for sprite in all_sprites if isinstance(sprite, Bullet)]
        colliding_bullets = pygame.sprite.spritecollide(self, bullets, False)
        for bullet in colliding_bullets:
            if self.hp > 0:
                self.hp -= 1
                bullet.kill()
                if self.hp == 0:
                    self.kill()
                    break

        """
        # Wall collision detection
        walls = [sprite for sprite in all_sprites if isinstance(sprite, Wall)]
        self.rect.y += y
        for wall in pygame.sprite.spritecollide(self, walls, False):
            if y > 0:
                self.rect.bottom = wall.rect.top
            if y < 0:
                self.rect.top = wall.rect.bottom
        self.rect.x += x
        for wall in pygame.sprite.spritecollide(self, walls, False):
            if x > 0:
                self.rect.right = wall.rect.left
            if x < 0:
                self.rect.left = wall.rect.right
        """


class TestBoss(BaseEnemy):
    def __init__(self, center=(0, 0)):
        super().__init__(image_path='assets/cat.png', center=center)
        self.hp = 10

    def update(self, all_sprites, player):
        bullets = [sprite for sprite in all_sprites if isinstance(sprite, Bullet)]
        colliding_bullets = pygame.sprite.spritecollide(self, bullets, False)
        for bullet in colliding_bullets:
            if self.hp > 0:
                self.hp -= 1
                bullet.kill()
                if self.hp == 0:
                    self.kill()
                    break

