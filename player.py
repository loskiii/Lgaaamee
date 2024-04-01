# player.py
import pygame
from settings import WHITE, PLAYER_SPEED

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surf = pygame.Surface((25, 25))
        self.surf.fill(WHITE)
        self.rect = self.surf.get_rect(center=(400, 300))
    
    def update(self, pressed_keys):
        if pressed_keys[pygame.K_UP]:
            self.rect.move_ip(0, -PLAYER_SPEED)
        if pressed_keys[pygame.K_DOWN]:
            self.rect.move_ip(0, PLAYER_SPEED)
        if pressed_keys[pygame.K_LEFT]:
            self.rect.move_ip(-PLAYER_SPEED, 0)
        if pressed_keys[pygame.K_RIGHT]:
            self.rect.move_ip(PLAYER_SPEED, 0)

        # Keep player on the screen
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > 800:
            self.rect.right = 800
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= 600:
            self.rect.bottom = 600
