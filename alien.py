import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """Класс, представляющий одного пришельца"""

    def __init__(self, ai_game):
        """Инициализирует пришельца и задает его начальную позицию"""
        super(Alien, self).__init__()
        self.screen = ai_game.screen
        self.ai_game = ai_game.settings

        # Загрузка изображение пришельца и назначение атрибута rect
        self.image = pygame.image.load("C:\\Users\\nskti\\Desktop\\Project1\\images\\pix_alien2.jpg")
        self.image = pygame.transform.scale(self.image, (self.ai_game.alien_width, self.ai_game.alien_height))
        self.rect = self.image.get_rect()

        # Каждый новый пришелец появляется в левом верхнем углу
        self.rect.x = 0
        self.rect.y = 0

        # Сохранение точной горизонтальной позиции пришельца
        self.x = float(self.rect.x)
        self.image.set_colorkey((255, 255, 255))

    def update(self):
        """Перемещает пришельца вправо"""
        self.x += (self.ai_game.alien_speed *
                   self.ai_game.fleet_direction)
        self.rect.x = self.x

    def check_edges(self):
        """Возвращает True, если пришелец находится у края экрана"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True
