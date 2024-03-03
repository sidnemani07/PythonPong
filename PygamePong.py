import pygame
import random
from pygame.locals import(
    K_UP,
    K_DOWN,
    K_w,
    K_s,
    K_ESCAPE,
    KEYDOWN,
    QUIT
)
# Initialize Pygame
pygame.init()

# Set up the game window
window_width = 800
window_height = 600
game_window = pygame .display.set_mode((window_width, window_height))
pygame .display.set_caption("Pong Game")

# Colors
white = (255, 255, 255)
black = (0, 0, 0)

# Create a font object for the score
font = pygame.font.Font(None, 36)

# Initialize player scores
left_score = 0
right_score = 0

# Function to display scores
def display_scores():
    score_text = font.render(f'Player 1: {left_score}  Player 2: {right_score}', True, white)
    game_window.blit(score_text, (window_width // 2 - score_text.get_width() // 2, 20))

# Paddle and ball properties
paddle_width = 10
paddle_height = 100
ball_size = 10
ball_speed = 5
paddle_speed = 7

# Create the paddles
class Paddle:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = paddle_width
        self.height = paddle_height
        self.rect =  pygame.Rect(self.x, self.y, self.width, self.height)

    def draw(self):
         pygame.draw.rect(game_window, white, self.rect)

    def move(self, y_direction):
        self.y += y_direction
        self.rect.y = self.y

# Create the ball
class Ball:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.size = ball_size
        self.rect =  pygame.Rect(self.x, self.y, self.size, self.size)
        self.direction = [random.choice([-1, 1]), random.choice([-1, 1])]
        self.speed = ball_speed

    def draw(self):
         pygame.draw.rect(game_window, white, self.rect)

    def move(self):
        self.x += self.speed * self.direction[0]
        self.y += self.speed * self.direction[1]
        self.rect.x = self.x
        self.rect.y = self.y

# Create the paddles and ball
left_paddle = Paddle(50, window_height // 2 - paddle_height // 2)
right_paddle =  Paddle(window_width - 50 - paddle_width, window_height // 2 - paddle_height // 2)
ball = Ball(window_width // 2, window_height // 2)

# Game loop
running = True
clock = pygame.time.Clock()
while running:
    #check if quit game
    for event in pygame.event.get():
        #check for quit by ESC
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
        #check for other method of quit
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        left_paddle.move(-paddle_speed)
    if keys[pygame.K_s]:
        left_paddle.move(paddle_speed)
    if keys[pygame.K_UP]:
        right_paddle.move(-paddle_speed)
    if keys[pygame.K_DOWN]:
        right_paddle.move(paddle_speed)

    ball.move()

    # Ball collision with left and right sides
    if ball.rect.left <= 0:
        # Reset the ball position to the middle
        ball.x = window_width // 2
        ball.y = window_height // 2
        ball.rect.x = ball.x
        ball.rect.y = ball.y
        ball.direction = [random.choice([-1, 1]), random.choice([-1, 1])]
        #give right paddle 1 point
        right_score += 1

    if ball.rect.right >= window_width:
        ball.x = window_width // 2
        ball.y = window_height // 2
        ball.rect.x = ball.x
        ball.rect.y = ball.y
        ball.direction = [random.choice([-1, 1]), random.choice([-1, 1])]
        #give left paddle 1 point
        left_score += 1

    # Ball collision with top and bottom
    if ball.rect.top <= 0 or ball.rect.bottom >= window_height:
        ball.direction[1] *= -1

    # Ball collision with paddles
    if ball.rect.colliderect(left_paddle.rect) or ball.rect.colliderect(right_paddle.rect):
        ball.direction[0] *= -1

    # Drawing the game window
    game_window.fill(black)
    pygame.draw.rect(game_window, white, left_paddle.rect)
    pygame.draw.rect(game_window, white, right_paddle.rect)
    pygame.draw.ellipse(game_window, white, ball.rect)
    pygame.draw.aaline(game_window, white, (window_width // 2, 0), (window_width // 2, window_height))
    display_scores()
    pygame.display.flip()
    clock.tick(60)  # Limit the game to 60 frames per second

# Quit the game
pygame.quit()