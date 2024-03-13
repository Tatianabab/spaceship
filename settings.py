import pygame.image
import math
from button import Button
from sounds import Sounds

class Settings:
    def __init__(self):
        self.screen_width = 480
        self.screen_height = 720
        self.fps = 60
        self.icon = pygame.image.load('images/ava.jpg')
        self.background = pygame.image.load('images/game_back.png')
        self.background = pygame.transform.scale(self.background,(self.screen_width, self.screen_height))

        self.menu_background = pygame.image.load('images/menu_back.png')
        self.menu_background = pygame.transform.scale(self.menu_background,(self.screen_width, self.screen_height))

        self.scroll = 0
        self.scroll_step = 2
        self.background_height = self.background.get_height()
        self.background_rect = self.background.get_rect()
        self.tiles = math.ceil(self.screen_width / self.background_height) + 1

        # self.icon = pygame.image.load('images/ship_1.png')

        self.player_ships = []
        for i in range(1, 4):
            self.player_ship = pygame.image.load(f'images/ship_{i}.png')
            self.player_ship = pygame.transform.scale(self.player_ship, (80, 80))
            self.player_ships.append(self.player_ship)
        self.ship_speed = 10

        self.bullet_image = pygame.image.load('images/bullet.png')
        self.bullet_image = pygame.transform.scale(self.bullet_image, (10, 20))
        self.bullet_speed = 5

        self.button_start = pygame.image.load("images/button_start.png")
        self.button_start = Button(self.button_start, 0.5, self)
        self.button_start.set_position((self.screen_width - self.button_start.rect.width) // 2,
                                       (self.screen_height - self.button_start.rect.height) // 2 - self.button_start.rect.height * 2)

        self.button_exit = pygame.image.load("images/button_exit.png")
        self.button_exit = Button(self.button_exit, 0.5, self)
        self.button_exit.set_position((self.screen_width - self.button_exit.rect.width) // 2,
                                      (self.screen_height - self.button_exit.rect.height) // 2 + self.button_exit.rect.height * 2)

        self.options_button = pygame.image.load('images/button_options.png')
        self.options_button = Button(self.options_button, 0.5, self)
        self.options_button.set_position((self.screen_width - self.options_button.rect.width) // 2,
                                         (self.screen_height - self.options_button.rect.height) // 2)

        self.button_back = pygame.image.load("images/button_back.png")
        self.button_back = Button(self.button_back, 0.3, self)
        self.button_back.set_position((self.screen_width - self.button_back.rect.width * 2),
                                      (self.screen_height - self.button_back.rect.height * 2))

        self.music_active_image = pygame.image.load("images/button_music_active.png")
        self.music_deactive_image = pygame.image.load("images/button_music_deactive.png")
        self.button_music = Button(self.music_active_image, 0.3, self)
        self.button_music.width_pos = 63
        self.button_music.height_pos = 63

        self.sound_active_image = pygame.image.load("images/button_sound_active.png")
        self.sound_deactive_image = pygame.image.load("images/button_sound_deactive.png")
        self.button_sound = Button(self.sound_active_image, 0.3, self)
        self.button_sound.width_pos = 158
        self.button_sound.height_pos = 63

        self.music_active = True
        self.sound_active = True
        self.menu_music = Sounds("sounds/menu_theme.mp3", 0.5, self)
        self.game_music = Sounds("sounds/game_theme.mp3", 0.2, self)
        self.shot_sound = Sounds("sounds/shot.wav", 0.2, self)
        self.button_click_sound = Sounds("sounds/button_click.mp3", 0.2, self)

        self.backward = pygame.image.load("images/backward.png")
        self.backward_button = Button(self.backward, 0.3, self)
        self.backward_button.set_position(63, (self.screen_height - self.backward_button.rect.height) // 2)

        self.forward = pygame.image.load("images/forward.png")
        self.forward_button = Button(self.forward, 0.3, self)
        self.forward_button.set_position(self.screen_width - 126, (self.screen_height - self.forward_button.rect.height) // 2)