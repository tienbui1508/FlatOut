import pygame
from constants import  SCREEN_HEIGHT, SCREEN_WIDTH

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Flat Out")

clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("skyblue")

    pygame.draw.rect(screen, "darkgreen", (100, 300, 40, 60))
    pygame.draw.line(screen, "brown", (0, 360), (800, 360), 5)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
