import pygame
import random

board_size_x = 30
board_size_y = 20
food_chance = 5000
empty_tag = "EMPTY"
food_tag = "FOOD"
snake_tail_tag = "TAIL"
snake_head_tag = "HEAD"
window_width = 600
window_height = 600
snake_size = 1
direction = "x+"

pygame.init()

# Create the window (width, height in pixels)
screen = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Snake")

is_running = True

def draw_square(color_tuple, udim_tuple):
    # color_tuple = (R [0-255], B, G)
    # (xPosition, yPosition, xSize, ySize)
    pygame.draw.rect(screen, color_tuple, udim_tuple)

def draw_board(cells):
    # color_tuple = (R [0-255], B, G)
    # (xPosition, yPosition, xSize, ySize)
    size_x_cell = window_width/board_size_x
    size_y_cell = window_height/board_size_y

    for x in range(0, board_size_x):
        for y in range(0, board_size_y):

            # Extract cell type
            cell_type = cells[x][y]["cell_type"]
            cell_color = (255,255,255)
            if cell_type == food_tag:
                cell_color = (0, 255, 0)
            else:
                cell_color = (0, 0, 255)

            draw_square(cell_color, (size_x_cell*x, size_y_cell*y, size_x_cell*0.75, size_y_cell*0.75) )

def initialize_board():
    print("initializing board...")
    cells = []
    for x in range(0, board_size_x):
        print("Here")
        cells.append([])
        for y in range(0, board_size_y):
            cells[x].append({"cell_type": empty_tag})
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
            cell = cells[x][y]

            # Check if cell is a valid place to spawn food
            # Skip empty that are not set to spawn food
            if cell["cell_type"] == empty_tag:
                if do_spawn_food:
                    cells[x][y]["cell_type"] = food_tag
                else:
                    continue

            # if snake head then set length to 1 and set to tail
            # Then create a new snake head at the direction offset +1
            if cell["cell_type"] == snake_head_tag:
                cell["cell_type"] = snake_tail_tag
                cell["order"] = 1 # Default to 1

            if cell["cell_type"] == snake_tail_tag:

                # If less than size increment
                if cell["order"] < snake_size:
                    cell["order"] += 1
                else:
                # if greater than size set to empty
                    cell["cell_type"] = empty_tag
                    cell["order"] = None


    return cells


cells = initialize_board()

while is_running:

    # Handle events, like clicking the window's X
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False
        if event.type == pygame.KEYDOWN:
            key = pygame.key.name(event.key)
            if key == "w":
                direction = "y+"
            elif key == "s":
                direction = "y-"
            elif key == "a":
                direction = "x-"
            elif key == "d":
                direction = "x+"

    # Fill the screen
    screen.fill((200, 200, 200))
    

    cells = update_board(cells)
    draw_board(cells)

    # Draw all the items requested to draw
    pygame.display.flip()

pygame.quit()