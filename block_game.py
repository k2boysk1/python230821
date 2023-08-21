import pygame
import random

# ... (Same code as before up to the game loop)

# Game settings
lives = 3  # Number of lives
ball_speed = [random.choice([-5, 5]), -5]

# Game loop
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move the paddle
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        paddle.x -= 5
    if keys[pygame.K_RIGHT]:
        paddle.x += 5

    # Move the ball
    ball.x += ball_speed[0]
    ball.y += ball_speed[1]

    # Ball collision with walls
    if ball.left <= 0 or ball.right >= screen_width:
        ball_speed[0] = -ball_speed[0]
    if ball.top <= 0:
        ball_speed[1] = -ball_speed[1]

    # Ball collision with paddle
    if ball.colliderect(paddle):
        ball_speed[1] = -ball_speed[1]

    # Ball goes below the paddle
    if ball.top > screen_height:
        lives -= 1
        if lives > 0:
            # Reset ball and paddle positions
            ball.center = (screen_width // 2, screen_height // 2)
            paddle.x = (screen_width - paddle_width) // 2
        else:
            running = False  # No lives left, end the game

    # Ball collision with blocks
    for block in blocks[:]:
        if ball.colliderect(block):
            blocks.remove(block)
            ball_speed[1] = -ball_speed[1]

    # Clear the screen
    screen.fill(black)

    # Draw the paddle, ball, and blocks
    pygame.draw.rect(screen, white, paddle)
    pygame.draw.circle(screen, white, ball.center, ball_radius)
    for idx, block in enumerate(blocks):
        pygame.draw.rect(screen, block_colors[idx // block_cols], block)

    # Draw lives
    font = pygame.font.Font(None, 36)
    lives_text = font.render(f"Lives: {lives}", True, white)
    screen.blit(lives_text, (10, 10))

    # Update the display
    pygame.display.flip()

    # Limit the frame rate
    clock.tick(60)

# Quit the game
pygame.quit()
