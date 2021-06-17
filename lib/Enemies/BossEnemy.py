import pygame

from lib.Enemies import BaseEnemy, EnemyBullet, line_of_sight, get_blocking_walls


class BossEnemy(BaseEnemy):
    DIFFICULTY = 99  # How much this enemy is worth in spawning
    KNOCKBACK_MULTIPLIER = 0

    ATTACK_DELAY = 30
    ENTERED_LOS_ATTACK_DELAY = 10  # If the player enters LOS, how long to wait before shooting
    MAX_HP = 15

    SPEED = 4
    BULLET_SPEED = 10

    IMAGE_PATH = 'assets/cat.png'

    def __init__(self, center=(0, 0)):
        super().__init__(image_assets=self.IMAGE_PATH, center=center)
        self.current_attack_delay = self.ATTACK_DELAY

        self.hp = self.MAX_HP
        self.bullets = pygame.sprite.Group()

    def update(self, all_sprites, player, game_map):
        # Handle taking damage
        self.hp = self.handle_damage(player, self.hp)
        if not self.hp:
            return

        # Handle knockback
        self.handle_knockback(all_sprites)

        path = self.lazy_theta_star(player.rect.center, all_sprites)
        self.move_along_path(path, self.SPEED, all_sprites)

        # Tick down attack delay
        self.current_attack_delay -= 1

        # Check if bullet can reach the player without hitting a wall
        in_los = line_of_sight(self.rect.center, player.rect.center, get_blocking_walls(all_sprites))

        # Check if in LOS
        if in_los and self.rect.center != player.rect.center:
            # Shoot at player if attack delay is over and not on top of enemy
            if self.current_attack_delay <= 0 and self.rect.center != player.rect.center:
                # Reset attack delay
                self.current_attack_delay = self.ATTACK_DELAY

                # Add bullet
                all_sprites.remove(self.bullets)
                enemy_dir = pygame.Vector2(player.rect.center) - pygame.Vector2(self.rect.center)
                enemy_dir = enemy_dir.normalize() * self.BULLET_SPEED
                self.bullets.add(EnemyBullet(self.rect.center, enemy_dir))
                all_sprites.add(self.bullets)

        # If the enemy is out of LOS, don't tick down the attack delay to much
        elif self.current_attack_delay < self.ENTERED_LOS_ATTACK_DELAY:
            self.current_attack_delay = self.ENTERED_LOS_ATTACK_DELAY
