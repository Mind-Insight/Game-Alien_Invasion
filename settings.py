class Settings:
    """Класс для хранения всех настроек игры Alien Invasion"""

    def __init__(self):
        """Инициализирует статические настройки игры"""
        # Параметры экрана
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (128, 0, 200)
        self.ship_width = 60
        self.ship_height = 65

        # Настройка корабля
        self.ship_limit = 3

        # Параметры снаряда
        self.bullet_width = 4
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 4

        # Настройки пришельца
        self.alien_width = 65
        self.alien_height = 65
        self.fleet_drop_speed = 15

        # Темп ускорения игры
        self.speedup_scale = 1.1
        # Темп роста стоимости пришельцев
        self.score_scale = 1.1
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Инициализирует настрйоки, изменяющиеся в ходе игры"""
        self.bullet_speed = 1.3
        self.ship_speed = 1.4
        self.alien_speed = 1.3

        # fleet_direction = 1, означает движение вправо; влево = -1
        self.fleet_direction = 1

        # Подсчет очков
        self.alien_points = 50

    def _increase_speed(self):
        """Увеличивает найстройки скорости и стоимости пришельцев"""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)
