import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    def __init__(self, game):
        super().__init__()
        self.game = game
        self.screen = game.screen
        self.settings = game.settings
        self.rect = self.settings.bullet_image.get_rect()
        self.rect.midtop = game.player.rect.midtop


    def update(self):
        self.rect.y -= self.settings.bullet_speed
        for bullet in self.game.player.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.game.player.bullets.remove(bullet)

    def draw_bullet(self):
        self.screen.blit(self.settings.bullet_image, self.rect)