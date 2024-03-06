import pygame
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
FPS = 60
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Car constants
CAR_WIDTH, CAR_HEIGHT = 50, 100
CAR_SPEED = 5
ENEMY_CAR_SPEED = 7

# Create game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pygame Racing Game")
clock = pygame.time.Clock()

# Load images
player_car_img = pygame.image.load("player_car.png").convert_alpha()
player_car_img = pygame.transform.scale(player_car_img, (CAR_WIDTH, CAR_HEIGHT))

enemy_car_img = pygame.image.load("enemy_car.png").convert_alpha()
enemy_car_img = pygame.transform.scale(enemy_car_img, (CAR_WIDTH, CAR_HEIGHT))

# Functions
def draw_text(text, size, color, x, y):
    font = pygame.font.SysFont(None, size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.center = (x, y)
    screen.blit(text_surface, text_rect)

def draw_player_car(x, y):
    screen.blit(player_car_img, (x, y))

def draw_enemy_car(x, y):
    screen.blit(enemy_car_img, (x, y))

def game_over():
    screen.fill(BLACK)
    draw_text("Game Over", 64, RED, WIDTH / 2, HEIGHT / 2)
    pygame.display.update()
    pygame.time.delay(2000)
    main()

def main():
    player_car_x = WIDTH / 2 - CAR_WIDTH / 2
    player_car_y = HEIGHT - CAR_HEIGHT - 20
    enemy_car_x = random.randint(0, WIDTH - CAR_WIDTH)
    enemy_car_y = -CAR_HEIGHT
    score = 0

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            player_car_x -= CAR_SPEED
        if keys[pygame.K_RIGHT]:
            player_car_x += CAR_SPEED

        screen.fill(WHITE)
        
        draw_player_car(player_car_x, player_car_y)
        draw_enemy_car(enemy_car_x, enemy_car_y)

        enemy_car_y += ENEMY_CAR_SPEED
        if enemy_car_y > HEIGHT:
            enemy_car_y = -CAR_HEIGHT
            enemy_car_x = random.randint(0, WIDTH - CAR_WIDTH)
            score += 1

        if (player_car_x + CAR_WIDTH > enemy_car_x and player_car_x < enemy_car_x + CAR_WIDTH and
                player_car_y + CAR_HEIGHT > enemy_car_y and player_car_y < enemy_car_y + CAR_HEIGHT):
            game_over()

        draw_text(f"Score: {score}", 32, BLACK, WIDTH / 2, 20)

        pygame.display.update()
        clock.tick(FPS)

    pygame.quit()

if _name_ == "_main_":
    main()