import pygame
import sys

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((1200, 800))
clock = pygame.time.Clock()
pygame.display.set_caption("Chicken Dash Animation")

# Load and slice sprite sheet
sprite_sheet = pygame.image.load("chicken_sprite_sheet.png").convert_alpha()
frame_width = sprite_sheet.get_width() // 4
frame_height = sprite_sheet.get_height() // 2

chicken_frames = []
for row in range(2):
    for col in range(4):
        frame = sprite_sheet.subsurface(pygame.Rect(
            col * frame_width, row * frame_height, frame_width, frame_height
        ))
        chicken_frames.append(frame)

# Animation variables
frame_index = 0
frame_delay = 5
frame_counter = 0
chicken_x = 0
chicken_y = 150
dash_speed = 6
paused = False

# Game loop
running = True
while running:
    screen.fill((200, 200, 200))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            elif event.key == pygame.K_SPACE:
                paused = not paused

    if not paused:
        # Animation update
        frame_counter += 1
        if frame_counter >= frame_delay:
            frame_index = (frame_index + 1) % len(chicken_frames)
            frame_counter = 0

        chicken_x += dash_speed
        if chicken_x > 800:
            chicken_x = -frame_width

    # Draw the chicken
    screen.blit(chicken_frames[frame_index], (chicken_x, chicken_y))

    if paused:
        font = pygame.font.SysFont(None, 48)
        pause_text = font.render("PAUSED", True, (255, 0, 0))
        screen.blit(pause_text, (340, 180))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
