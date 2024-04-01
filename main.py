# main.py
import pygame
import sys
from settings import SCREEN_WIDTH, SCREEN_HEIGHT, BLACK
from player import Player

def main():
    pygame.init()
    
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Simple Pygame Example")

    # Create a custom event for adding a new enemy
    ADDENEMY = pygame.USEREVENT + 1
    pygame.time.set_timer(ADDENEMY, 250)
    
    player = Player()

    # Create groups to hold enemy sprites, and all sprites
    # - enemies is used for collision detection and position updates
    # - all_sprites is used for rendering
    enemies = pygame.sprite.Group()
    all_sprites = pygame.sprite.Group()
    all_sprites.add(player)

    clock = pygame.time.Clock()
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        pressed_keys = pygame.key.get_pressed()
        player.update(pressed_keys)
        
        screen.fill(BLACK)
        
        for entity in all_sprites:
            screen.blit(entity.surf, entity.rect)
        
        pygame.display.flip()
        
        clock.tick(30)

if __name__ == "__main__":
    main()
