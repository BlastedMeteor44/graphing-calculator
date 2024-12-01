import pygame
import math

# Initialize Pygame
pygame.init()
win = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Graph Equation")


def display_point(x, y):
    """Draws a small rectangle at (x, y)."""
    pygame.draw.rect(win, (255, 0, 0), (x, y, 2, 2))

def space_to_screen_pos(x, y, cam_pos):
    return [cam_pos[0] - x, cam_pos[1] - y]

def screen_to_space_pos(x, y, cam_pos):
    return [cam_pos[0] - x, cam_pos[1] - y]

# Position tuple for the center (modifiable during runtime)
position = [250, 250]  # Use a list so it's mutable (easier to edit)

# Main loopimport pygame
import math

# Initialize Pygame
pygame.init()
win = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Graph Equation")

def display_point(x, y):
    """Draws a small rectangle at (x, y) on the screen."""
    pygame.draw.rect(win, (255, 0, 0), (x, y, 2, 2))

def space_to_screen_pos(x, y, cam_pos):
    """Convert space coordinates to screen coordinates."""
    screen_x = cam_pos[0] + x
    screen_y = cam_pos[1] - y  # Invert Y-axis for proper graphing
    return [screen_x, screen_y]

def screen_to_space_pos(x, y, cam_pos):
    """Convert screen coordinates to space coordinates."""
    space_x = x - cam_pos[0]
    space_y = cam_pos[1] - y  # Invert Y-axis for proper graphing
    return [space_x, space_y]

# Position tuple for the center (modifiable during runtime)
position = [250, 250]  # Screen center (acts as camera position)

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Adjust position with arrow keys
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                position[0] += 10  # Move graph left
            if event.key == pygame.K_RIGHT:
                position[0] -= 10  # Move graph right
            if event.key == pygame.K_UP:
                position[1] += 10  # Move graph up
            if event.key == pygame.K_DOWN:
                position[1] -= 10  # Move graph down

    win.fill((255, 255, 255))  # Clear the screen

    # Render the sine wave
    for x in range(-250, 250):
        # Convert x to space coordinates and calculate y
        space_x = x
        space_y = math.sin(space_x / 50) * 100  # Scale the sine wave

        # Convert space coordinates to screen coordinates
        screen_x, screen_y = space_to_screen_pos(space_x, space_y, position)

        # Draw the point on the screen
        display_point(screen_x, screen_y)

    pygame.display.update()  # Update the display

pygame.quit()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Adjust position with arrow keys
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                position[0] += 10  # Move graph left
            if event.key == pygame.K_RIGHT:
                position[0] -= 10  # Move graph right
            if event.key == pygame.K_UP:
                position[1] += 10  # Move graph up
            if event.key == pygame.K_DOWN:
                position[1] -= 10  # Move graph down

    win.fill((255, 255, 255))  # Clear the screen

    # Uncomment the below loop to render the line
    # Define the space range for the sine wave
    space_x_start = screen_to_space_pos(-250, 0, position)[0]
    space_x_end = screen_to_space_pos(250, 0, position)[0]

    # Render the sine wave dynamically based on screen and position
    screen_width = 500
    for screen_x in range(0, screen_width):
        # Convert the screen x-coordinate to space coordinates (world space)
        space_x = screen_to_space_pos(screen_x, 0, position)[0]
        
        # Calculate the sine value in space coordinates
        space_y = math.sin(space_x / 50) * 100  # Adjust frequency and amplitude
        
        # Convert space coordinates back to screen coordinates
        screen_pos = space_to_screen_pos(space_x, space_y, position)
        
        # Draw the point only if it's within the visible screen range
        if 0 <= screen_pos[0] < screen_width and 0 <= screen_pos[1] < 500:
            display_point(screen_pos[0], screen_pos[1])




    pygame.display.update()  # Update the display

pygame.quit()

