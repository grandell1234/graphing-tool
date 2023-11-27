import pygame
import sys
import random

# Initialize Pygame.
pygame.init()

# Set up the display.
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Graph Visualization')

# Sample data.
points = [(50, 100), (100, 200), (150, 150), (200, 300), (250, 250)]
selected_point = None
dragging = False

# Button parameters.
button_width, button_height = 210, 30  # Adjusted width for "Toggle Visibility"
button_spacing = 40
button_offset = (width - (button_width + button_spacing) * 2) // 2
add_point_button_rect = pygame.Rect(button_offset, height - 40, button_width, button_height)
toggle_visibility_button_rect = pygame.Rect(add_point_button_rect.right + button_spacing, height - 40, button_width + 50, button_height)  # Adjusted width for "Toggle Visibility"
button_color = (0, 255, 0)

# Font for text.
button_font = pygame.font.Font(pygame.font.get_default_font(), 20)

# Toggle variable.
points_visible = True

# Main game loop.
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            for i, point in enumerate(points):
                if pygame.Rect(point[0] - 5, point[1] - 5, 10, 10).collidepoint(event.pos):
                    selected_point = i
                    dragging = True
            if add_point_button_rect.collidepoint(event.pos):
                # Add a new point
                new_point = (random.randint(10, width // 2), random.randint(10, height // 2))
                points.append(new_point)
            elif toggle_visibility_button_rect.collidepoint(event.pos):
                # Toggle points visibility
                points_visible = not points_visible
        elif event.type == pygame.MOUSEMOTION and dragging:
            # Update the position of the selected point while dragging
            points[selected_point] = event.pos
        elif event.type == pygame.MOUSEBUTTONUP:
            # Stop dragging when the mouse button is released
            dragging = False

    # Clear the screen.
    screen.fill((255, 255, 255))

    # Draw the points if they are visible.
    if points_visible:
        for point in points:
            pygame.draw.circle(screen, (0, 0, 255), point, 5)

    # Draw the lines.
    for i in range(len(points) - 1):
        pygame.draw.line(screen, (0, 0, 0), points[i], points[i + 1], 2)

    # Draw the "Add Point" button.
    pygame.draw.rect(screen, button_color, add_point_button_rect)
    text = button_font.render('Add Point', True, (0, 0, 0))
    text_rect = text.get_rect(center=add_point_button_rect.center)
    screen.blit(text, text_rect)

    # Draw the "Toggle Visibility" button.
    pygame.draw.rect(screen, button_color, toggle_visibility_button_rect)
    text = button_font.render('Toggle Visibility', True, (0, 0, 0))
    text_rect = text.get_rect(center=toggle_visibility_button_rect.center)
    screen.blit(text, text_rect)

    # Update the display.
    pygame.display.flip()

# Exit the program.
pygame.quit()
sys.exit()

