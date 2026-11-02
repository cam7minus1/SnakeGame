import pygame
import random

board_size_x = 30
board_size_y = 20
food_chance = 5000
empty_tag = "EMPTY"
food_tag = "FOOD"
snake_tail_tag = "TAIL"
snake_head_tag = "HEAD"
window_width = 450
window_height = 300
snake_size = 1
direction = "x+"
padding = 0.01

pygame.init()

# Create the window (width, height in pixels)
screen = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Snake")

is_running = True

def get_next_cell_indicies(cell_x, cell_y, direction):

    next_cell_x = cell_x
    next_cell_y = cell_y

    if direction == "x+":
        next_cell_x += 1
    elif direction == "x-":
        next_cell_x -= 1
    elif direction == "y+":
        next_cell_y += 1
    elif direction == "y-":
        next_cell_y -= 1

    if next_cell_x < 0 or next_cell_x > board_size_x:
        return
    elif next_cell_y < 0 or next_cell_y > board_size_y:
        return
    else:
        return next_cell_x, next_cell_y

def draw_square(color_tuple, udim_tuple):
    # color_tuple = (R [0-255], B, G)
    # (xPosition, yPosition, xSize, ySize)
    pygame.draw.rect(screen, color_tuple, udim_tuple)

def draw_board(cells):

    size_x_cell = window_width/board_size_x
    size_y_cell = window_height/board_size_y
    size = 1 - padding

    for x in range(0, board_size_x):
        for y in range(0, board_size_y):

            # Extract cell type
            cell_type = cells[x][y]["cell_type"]
            cell_color = (255,255,255)
            if cell_type == food_tag:
                cell_color = (0, 255, 0)
            elif cell_type == snake_tail_tag or cell_type == snake_head_tag:
                cell_color = (0, 0, 255)

            draw_square(cell_color, (size_x_cell*x, size_y_cell*y, size_x_cell*size, size_y_cell*size) )

def initialize_board():
    print("initializing board...")
    cells = []

    # Initialize an empty board
    for x in range(0, board_size_x):
        cells.append([])
        for y in range(0, board_size_y):
            cells[x].append({"cell_type": empty_tag})

    # Next we spawn the snake
    cells[int(board_size_x/2)][int(board_size_y/2)]["cell_type"] = snake_head_tag
    
    return cells

def do_spawn_food():
    if random.randint(1, food_chance) == 1:
        return False
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
                if do_spawn_food():
                    cells[x][y]["cell_type"] = food_tag
                else:
                    continue

            # if snake head then set length to 1 and set to tail
            # Then create a new snake head at the direction offset +1
            if cell["cell_type"] == snake_head_tag:
                cell["cell_type"] = snake_tail_tag
                cell["order"] = 1 # Default to 1
                n_x, n_y = get_next_cell_indicies()

                if n_x is None or n_y is None:
                    print("You lose!")
                    return False

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

clock = pygame.time.Clock()

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

    clock.tick(2)

    # Fill the screen
    screen.fill((200, 200, 200))
    

    cells = update_board(cells)
    if cells is False:
        print(f"Game Over! Reached length: {snake_size}")
        is_running = False

    draw_board(cells)

    # Draw all the items requested to draw
    pygame.display.flip()

pygame.quit()