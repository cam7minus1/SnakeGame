import pygame

pygame.init()

# Create the window (width, height in pixels)
screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Snake")

is_running = True

while is_running:

    # Handle events, like clicking the window's X
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False

    # Draw
    screen.fill((0, 0, 0))
    pygame.display.flip()

pygame.quit()