class Settings:

    def __init__(self):
        self.screen_width = 1366
        self.screen_height = 786
        self.bg_color = (16, 7, 52)

        # Ship Settings
        self.ship_limits = 3

        # Bullet Settings
        self.bullet_width = 4
        self.bullet_height = 15
        self.bullet_color = ('#B31312')
        self.bullets_allowed = 3
        # Alien Settings
        self.fleet_drop_speed = 10
    
        # Velocidade do jogo
        self.speed_scale = 1.1
        self.score_scale = 1.5

        # Configuração de pontuação
        self.alien_point = 50

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        self.ship_speed = 1.5
        self.bullet_speed = 2.5
        self.alien_speed = 1.0
        self.fleet_direction = 1  
    
    def increase_speed(self):
        self.ship_speed *= self.speed_scale
        self.bullet_speed *= self.speed_scale
        self.alien_speed *= self.speed_scale
        self.alien_point = int(self.alien_point * self.score_scale)
        