import pygame
import sys

pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Changing Text Color")

# Font setup
FONT = pygame.font.Font(None, 74)
TEXT_STRING = "Hello Pygame!"

# Color cycling parameters
COLORS = [(255, 0, 0), (0, 255, 0), (0, 0, 255)]  # Red, Green, Blue
color_index = 0
transition_time = 2000  # Milliseconds for each color transition
start_time = pygame.time.get_ticks()

def lerp_color(color1, color2, amount):
    """Linear interpolation between two RGB colors."""
    r = int(color1[0] + (color2[0] - color1[0]) * amount)
    g = int(color1[1] + (color2[1] - color1[1]) * amount)
    b = int(color1[2] + (color2[2] - color1[2]) * amount)
    return (r, g, b)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Calculate current color based on time
    current_time = pygame.time.get_ticks()
    elapsed_time = current_time - start_time

    # Determine the "amount" for LERP (0.0 to 1.0)
    amount = min(1.0, elapsed_time / transition_time)

    # Get current and next color in the cycle
    current_color_base = COLORS[color_index]
    next_color_index = (color_index + 1) % len(COLORS)
    next_color_target = COLORS[next_color_index]

    # Interpolate the color
    current_text_color = lerp_color(current_color_base, next_color_target, amount)

    # If a transition is complete, move to the next color
    if amount >= 1.0:
        color_index = next_color_index
        start_time = current_time  # Reset start time for the new transition

    # Render the text with the current interpolated color
    text_surface = FONT.render(TEXT_STRING, True, current_text_color)
    text_rect = text_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2))

    # Drawing
    SCREEN.fill((0, 0, 0))  # Black background
    SCREEN.blit(text_surface, text_rect)
    pygame.display.flip()

    pygame.time.Clock().tick(60) # Limit to 60 FPS

pygame.quit()
sys.exit()
