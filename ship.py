import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
    """Класс для управления кораблем"""

    def __init__(self, ai_game, screen):
        """Инициализирует корабль и задает его начальную позицию"""
        super().__init__()
        self.screen = screen
        self.ai_game = ai_game

        # Загружает изображение корабля

        self.image = pygame.image.load("C:\\Users\\nskti\\Desktop\\Project1\\images\\battle_ship.png")

        # устанавливает размер корабля
        self.image = pygame.transform.scale(self.image, (self.ai_game.ship_width, self.ai_game.ship_height))

        # получает прямоугольник
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Каждый новый корабль появляется у нижнего края экрана.
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # Сохранение вещественной координаты центра корабля.
        self.x = float(self.rect.centerx)

        # Все пиксели, цвет которых совпадает с переданным в set_colorkey() значением, станут прозрачными
        self.image.set_colorkey((255, 255, 255))

        # Флаг перемещения
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Обновляет позицию корабля с учетом флага"""
        # Обновляется атрибут x, не rect.
        # Устанавливаем границы экрана
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.ai_game.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.ai_game.ship_speed

        # Обновление атрибута rect на основании self.x
        self.rect.x = self.x

    def center_ship(self):
        """Размещает корабль в центре нижней стороны"""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)

    def blitme(self):
        """Рисует корабль в текущей позиции"""
        self.screen.blit(self.image, self.rect)
