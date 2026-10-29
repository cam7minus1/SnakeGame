import pygame
import random

board_size_x = 30
board_size_y = 20
food_chance = 50 # Higher number is lower chance
empty_tag = "EMPTY"
food_tag = "FOOD"

pygame.init()

# Create the window (width, height in pixels)
screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Snake")

is_running = True

def update_board():
    pass

def initialize_board():
    print("initializing board...")
    cells = []
    for x in range(0, board_size_x):
        print("Here")
        cells.append([])
        for y in range(0, board_size_y):
            cells[x].append(empty_tag)
            print(x, y)

    return cells

def do_spawn_food():
    if random.randint(1, food_chance) == 1:
        return True
    else:
        return False

def update_board(cells):
    # Iterate through all cells
    for x in range(0, board_size_x):
        for y in range(0, board_size_y):

            # Extract cell type
            cell_type = cells[x][y]

            # Check if cell is a valid place to spawn food
            if cell_type == empty_tag and do_spawn_food:
                cells[x][y] = food_tag

initialize_board()

while is_running:

    # Handle events, like clicking the window's X
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False
        if event.type == pygame.KEYDOWN:
            key = pygame.key.name(event.key)
            if key == "w":
                print("Up")
            elif key == "s":
                print("Down")
            elif key == "a":
                print("Left")
            elif key == "d":
                print("Right")
    # Draw
    screen.fill((200, 200, 200))
    pygame.display.flip()

pygame.quit()