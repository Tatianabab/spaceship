import pygame
import random
from settings import Settings
from player import Player
from enemy import Enemy
from level import Level

class Game:
    def __init__(self):
        self.last_enemy_spawn_time = 0
        pygame.init()
        self.settings = Settings()
        self.settings.load_bd()
        self.levels = []
        for level in self.settings.levels_in_bd:
            self.levels.append(Level(level['level'],
                                     level['enemy_speed'],
                                     level['enemy_hp'],
                                     level['enemy_damage'],
                                     level['enemy_spawm_delay'], self))

        self.current_game_level = 1
        self.level_now = self.levels[self.current_game_level - 1]
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption('star wars')
        pygame.display.set_icon(self.settings.icon)
        self.player = Player(self)
        self.game_begin = False
        self.in_menu = True
        self.in_options = False
        self.game_over = False

    def run_game(self):
        clock = pygame.time.Clock()

        while True:
            if not self.game_begin:
                self._check_menu_events()
                if self.in_menu:
                    self.settings.menu_music.run_music()
                    self._update_menu_screen()
                elif self.in_options:
                    self._update_options_screen()
            else:
                self.settings.menu_music.stop_music()
                self.settings.game_music.run_music()
                self._check_game_events()
                self.player.update()
                self.player.bullets.update()
                self._update_game_screen()

            clock.tick(self.settings.fps)
    def _check_game_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.settings.update_bd('players', 'score', self.settings.player_record_score)
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.settings.shot_sound.run_sound_effect()
                    self.player.fire_bullet()

        keys = pygame.key.get_pressed()

        self.player.move_left = keys[pygame.K_LEFT]
        self.player.move_right = keys[pygame.K_RIGHT]
    def _check_menu_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
    def _update_game_screen(self):
        if not self.game_over:
            self.level_now.level_background_update()
            self.level_now.explosion_group.draw(self.screen)
            self.level_now.explosion_group.update()
            self.level_now.level_enemy_spawn()
            self.player.blit_player()
            self.player.bullets.draw(self.screen)
        else:
            print("Game over")
        pygame.display.update()
    def _update_menu_screen(self):
        self.screen.blit(self.settings.menu_background, (0,0))
        self.player_record_score_text = self.settings.player_score_font.render(
            f'Рекорд: {self.settings.player_record_score}', True, (180, 0, 0))
        self.player_record_score_text_rect = self.player_record_score_text.get_rect()
        self.player_record_score_text_rect.centerx = self.screen.get_rect().centerx
        self.player_record_score_text_rect.top = 100
        self.screen.blit(self.player_record_score_text, self.player_record_score_text_rect)
        if self.settings.button_start.draw(self.screen):
            self.game_begin = True
            self.in_menu = False
        if self.settings.options_button.draw(self.screen):
            self.in_options = True
            self.in_menu = False
        if self.settings.button_exit.draw(self.screen):
            exit()
        pygame.display.update()

    def _update_options_screen(self):
        self.screen.fill('black')
        if self.settings.button_back.draw(self.screen):
            self.in_menu = True
            self.in_options = False
        if self.settings.music_active:
            self.settings.button_music.set_image(self.settings.music_active_image)
            self.settings.button_music.set_position(self.settings.button_music.width_pos,
                                                    self.settings.button_music.height_pos)
            if self.settings.button_music.draw(self.screen):
                self.settings.music_active = False
                self.settings.menu_music.stop_music()
                self.settings.update_bd('players', 'music_status', 0)
        else:
            self.settings.button_music.set_image(self.settings.music_deactive_image)
            self.settings.button_music.set_position(self.settings.button_music.width_pos,
                                                    self.settings.button_music.height_pos)
            if self.settings.button_music.draw(self.screen):
                self.settings.music_active = True
                self.settings.menu_music.run_music()
                self.settings.update_bd('players', 'music_status', 1)

        if self.settings.sound_active:
            self.settings.button_sound.set_image(self.settings.sound_active_image)
            self.settings.button_sound.set_position(self.settings.button_sound.width_pos, self.settings.button_sound.height_pos)
            if self.settings.button_sound.draw(self.screen, sound=False):
                self.settings.sound_active = False
                self.settings.update_bd('players', 'sound_status', 0)
        else:
            self.settings.button_sound.set_image(self.settings.sound_deactive_image)
            self.settings.button_sound.set_position(self.settings.button_sound.width_pos, self.settings.button_sound.height_pos)
            if self.settings.button_sound.draw(self.screen, sound=True, force_sound=True):
                self.settings.sound_active = True
                self.settings.update_bd('players', 'sound_status', 1)

        if self.settings.backward_button.draw(self.screen):
            self.player.switch_ship('backward')
        if self.settings.forward_button.draw(self.screen):
            self.player.switch_ship('forward')
        self.screen.blit(self.player.ship_description, self.player.ship_description_rect)
        self.screen.blit(self.player.player_ship, self.player.player_ship.get_rect(center=self.screen.get_rect().center))
        pygame.display.update()

if __name__ == '__main__':
    game = Game()
    game.run_game()