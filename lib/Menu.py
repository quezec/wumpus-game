from lib.helpers import BaseSprite

from config import WINDOW_HEIGHT, WINDOW_WIDTH


class GameButton(BaseSprite):
    def __init__(self):
        super().__init__(image_assets='assets/menu/play.png', center=(WINDOW_WIDTH/2, WINDOW_HEIGHT/2 + 30))

class ContinueButton(BaseSprite):
    def __init__(self):
        super().__init__(image_assets='assets/menu/continue.png', center=(WINDOW_WIDTH/2, WINDOW_HEIGHT/2 + 30))

class ExitButton(BaseSprite):
    def __init__(self):
        super().__init__(image_assets='assets/menu/exit.png', center=(WINDOW_WIDTH/2, WINDOW_HEIGHT/2 + 120))

class GameCloseButton(BaseSprite):
    def __init__(self):
        super().__init__(image_assets='assets/menu/gameclose.png', center=(WINDOW_WIDTH/2, WINDOW_HEIGHT/2 + 120))

class Title(BaseSprite):
    def __init__(self):
        super().__init__(image_assets='assets/menu/TITLE.png', center=(WINDOW_WIDTH/2, 80))

class DeathTitle(BaseSprite):
    def __init__(self):
        super().__init__(image_assets='assets/menu/youdie.png', center=(WINDOW_WIDTH/2, 80))

class Paused(BaseSprite):
    def __init__(self):
        super().__init__(image_assets='assets/menu/PAUSED.png', center=(WINDOW_WIDTH/2, 80))