import pygame
from bullet import Bullet

class Player():
    def __init__(self, game):
        self.player_ship = None
        self.game = game
        self.screen = game.screen
        self.settings = game.settings
        self.screen_rect = game.screen.get_rect()
        self.current_ship_index = 0
        self.switch_ship(0)

        self.move_left = False
        self.move_right = False
        self.ship_speed = self.settings.ship_speed
        self.bullets = pygame.sprite.Group()

    def switch_ship(self, direction):
        total_ships = len(self.settings.player_ships)
        if total_ships > 0:
            if direction == 1:
                self.current_ship_index = (self.current_ship_index + 1) % total_ships
            elif direction == -1:
                self.current_ship_index = (self.current_ship_index - 1) % total_ships
            self.player_ship = self.settings.player_ships[self.current_ship_index]
            self.rect = self.player_ship.get_rect()
            self.rect.midbottom = (self.screen_rect.midbottom[0], self.screen_rect.midbottom[1] - 10)
        return self.current_ship_index

    def fire_bullet(self):
        bullet = Bullet(self.game)
        self.bullets.add(bullet)

    def update(self):
        if self.move_left and self.rect.left > 0:
            self.rect.x -= self.ship_speed
        if self.move_right and self.rect.right < self.screen_rect.right:
            self.rect.x += self.ship_speed

    def blit_player(self):
        self.screen.blit(self.player_ship, self.rect)