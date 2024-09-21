import pygame
import random
import math


pygame.init()


WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
BLUE = (0, 191, 255)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Pegar Círculos e Desviar de Triângulos')


player_size = 50
player_x = SCREEN_WIDTH // 2
player_y = SCREEN_HEIGHT - player_size
player_speed = 10


circle_radius = 30
triangle_size = 40
circle_speed = 5
triangle_speed = 5
circle_list = []
triangle_list = []

def create_circle():
    x_pos = random.randint(circle_radius, SCREEN_WIDTH - circle_radius)
    circle_list.append([x_pos, 0])

def create_triangle():
    x_pos = random.randint(triangle_size, SCREEN_WIDTH - triangle_size)
    triangle_list.append([x_pos, 0])


def move_objects(objects, speed):
    for obj in objects:
        obj[1] += speed


def check_collision_circle(player_x, player_y, circle_list):
    for circle in circle_list:
        circle_x, circle_y = circle
        distance = math.sqrt((circle_x - (player_x + player_size // 2))**2 + (circle_y - (player_y + player_size // 2))**2)
        if distance < circle_radius + player_size // 2:
            circle_list.remove(circle)
            return True
    return False


def check_collision_triangle(player_x, player_y, triangle_list):
    for triangle in triangle_list:
        triangle_x, triangle_y = triangle
        distance = math.sqrt((triangle_x - (player_x + player_size // 2))**2 + (triangle_y - (player_y + player_size // 2))**2)
        if distance < triangle_size:
            return True
    return False


def draw_triangle(x, y):
    points = [(x, y), (x - triangle_size, y + triangle_size), (x + triangle_size, y + triangle_size)]
    pygame.draw.polygon(screen, RED, points)

def show_text(text, font_size, color, x, y):
    font = pygame.font.Font(None, font_size)
    rendered_text = font.render(text, True, color)
    screen.blit(rendered_text, (x, y))

def draw_gradient():
    for i in range(SCREEN_HEIGHT):
       
        r = int(0 + (255 * i / SCREEN_HEIGHT))  
        g = int(191 + (64 * i / SCREEN_HEIGHT)) 
        b = 255  # Azul fixo
        pygame.draw.line(screen, (r, g, b), (0, i), (SCREEN_WIDTH, i))

def game_over_screen(score):
    screen.fill(WHITE)
    show_text("Game Over", 64, RED, SCREEN_WIDTH // 2 - 150, SCREEN_HEIGHT // 2 - 100)
    show_text(f"Você fez {score} pontos!", 36, BLACK, SCREEN_WIDTH // 2 - 120, SCREEN_HEIGHT // 2)
    show_text("Pressione 'R' para jogar novamente ou 'Q' para sair", 28, BLACK, SCREEN_WIDTH // 2 - 230, SCREEN_HEIGHT // 2 + 50)
    pygame.display.flip()

    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                waiting = False
                return False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    return True
                if event.key == pygame.K_q:
                    return False


clock = pygame.time.Clock()

def main_game():
    game_over = False
    score = 0
    player_x = SCREEN_WIDTH // 2
    player_y = SCREEN_HEIGHT - player_size
    circle_list.clear()
    triangle_list.clear()
    circle_speed = 5
    triangle_speed = 5

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player_x - player_speed > 0:
            player_x -= player_speed
        if keys[pygame.K_RIGHT] and player_x + player_speed < SCREEN_WIDTH - player_size:
            player_x += player_speed

       
        if random.randint(1, 20) == 1:
            create_circle()
        if random.randint(1, 25) == 1:
            create_triangle()

        move_objects(circle_list, circle_speed)
        move_objects(triangle_list, triangle_speed)

  
        if check_collision_circle(player_x, player_y, circle_list):
            score += 1
        if check_collision_triangle(player_x, player_y, triangle_list):
            game_over = True

        if score % 10 == 0 and score > 0:
            circle_speed += 0.5
            triangle_speed += 0.5

        draw_gradient()


        pygame.draw.rect(screen, BLACK, (player_x, player_y, player_size, player_size))


        for circle in circle_list:
            pygame.draw.circle(screen, GREEN, (circle[0], circle[1]), circle_radius)


        for triangle in triangle_list:
            draw_triangle(triangle[0], triangle[1])


        circle_list[:] = [circle for circle in circle_list if circle[1] < SCREEN_HEIGHT]
        triangle_list[:] = [triangle for triangle in triangle_list if triangle[1] < SCREEN_HEIGHT]


        show_text(f'Score: {score}', 36, BLACK, 10, 10)

        pygame.display.flip()
        clock.tick(30)

    return score


while True:
    score = main_game()
    if not game_over_screen(score):
        break

pygame.quit()
