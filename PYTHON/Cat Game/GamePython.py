import pygame
import random
import math
import os

pygame.init()

# Cores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Dimensões da tela
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Cat Fish')

# Variáveis do jogador
player_size = 75
player_x = SCREEN_WIDTH // 2
player_y = SCREEN_HEIGHT - player_size
player_speed = 21

# Configurações de círculos e triângulos
circle_radius = 30
triangle_size = 80
circle_speed = 5
triangle_speed = 5
circle_list = []
triangle_list = []

# Carregar e redimensionar imagens
img_circle = pygame.transform.scale(pygame.image.load(os.path.join(os.path.dirname(__file__), 'IMG/fish.png')).convert_alpha(), (80, 80))
img_triangle_B = pygame.transform.scale(pygame.image.load(os.path.join(os.path.dirname(__file__),"IMG/ball.png")).convert_alpha(), (80, 80))
img_triangle_C = pygame.transform.scale(pygame.image.load(os.path.join(os.path.dirname(__file__),"IMG/knife.png")).convert_alpha(), (80, 80))
img_triangle_D = pygame.transform.scale(pygame.image.load(os.path.join(os.path.dirname(__file__),"IMG/pc.png")).convert_alpha(), (80, 80))
img_player_idle = pygame.transform.scale(pygame.image.load(os.path.join(os.path.dirname(__file__),"IMG/catStop.png")).convert_alpha(), (80, 80))
img_player_move = pygame.transform.scale(pygame.image.load(os.path.join(os.path.dirname(__file__),"IMG/catWalk.png")).convert_alpha(), (80, 80))
background_img = pygame.transform.scale(pygame.image.load(os.path.join(os.path.dirname(__file__),"IMG/fundo.png")).convert(), (SCREEN_WIDTH, SCREEN_HEIGHT))

# Carregar som
pygame.mixer.music.load(os.path.join(os.path.dirname(__file__),"SOUND/catGameMusic.mp3"))
pygame.mixer.music.play(-1)  # Toca em loop

# Funções de criação
def create_circle():
    x_pos = random.randint(circle_radius, SCREEN_WIDTH - circle_radius)
    circle_list.append([x_pos, 0])  # Círculo começa do topo da tela (y=0)

def create_triangle():
    x_pos = random.randint(0, SCREEN_WIDTH - triangle_size)
    triangle_img = random.choice([img_triangle_B, img_triangle_C, img_triangle_D])
    triangle_list.append([x_pos, 0, triangle_img])  # Triângulo começa do topo (y=0)

# Função para mover objetos
def move_objects(objects, speed):
    for obj in objects:
        obj[1] += speed

# Função para colisões
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
        triangle_x, triangle_y = triangle[:2]
        distance = math.sqrt((triangle_x - (player_x + player_size // 2))**2 + (triangle_y - (player_y + player_size // 2))**2)
        if distance < triangle_size // 2:
            return True
    return False

# Função para desenhar triângulos (agora com imagens)
def draw_triangle(x, y, image):
    screen.blit(image, (x, y))

# Função para desenhar o jogador
def draw_player(x, y, moving):
    if moving:
        screen.blit(img_player_move, (x, y))
    else:
        screen.blit(img_player_idle, (x, y))

# Mostrar texto na tela
def show_text(text, font_size, color, x, y):
    font = pygame.font.Font(None, font_size)
    rendered_text = font.render(text, True, color)
    screen.blit(rendered_text, (x, y))

# Função para exibir tela de fim de jogo
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

# Função para animação de título com efeito de escala e transparência
def animate_title(text, font_size, x, y):
    font = pygame.font.Font(None, font_size)
    scale_factor = 1.0
    alpha = 0
    color = RED

    for i in range(60):  # Animação em 60 frames
        screen.blit(background_img, (0, 0))

        # Desenhar uma camada preta semi-transparente
        dark_layer = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
        dark_layer.set_alpha(128)  # Transparência de 50%
        dark_layer.fill(BLACK)
        screen.blit(dark_layer, (0, 0))

        title_surface = font.render(text, True, color)
        title_surface = pygame.transform.rotozoom(title_surface, 0, scale_factor)
        title_surface.set_alpha(alpha)

        screen.blit(title_surface, (x - title_surface.get_width() // 2, y - title_surface.get_height() // 2))

        pygame.display.flip()
        pygame.time.delay(50)

        scale_factor += 0.02  # Aumentar a escala a cada frame
        alpha += 4  # Aumentar transparência até 255

        if alpha > 255:
            alpha = 255

# Função do menu principal
def main_menu():
    menu_running = True

    while menu_running:
        screen.blit(background_img, (0, 0))

        # Desenhar uma camada preta semi-transparente
        dark_layer = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
        dark_layer.set_alpha(128)  # Transparência de 50%
        dark_layer.fill(BLACK)
        screen.blit(dark_layer, (0, 0))

        # Mostrar título animado
        animate_title("CAT FISH", 100, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 4)

        # Mostrar instrução para começar
        show_text("Press ENTER to Start", 48, WHITE, SCREEN_WIDTH // 2 - 180, SCREEN_HEIGHT // 2 + 100)
        
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    menu_running = False  # Iniciar o jogo


def animate_title(text_parts, font_size, x, y):
    font = pygame.font.Font(None, font_size)
    color = WHITE
    delay = 500  # Delay entre palavras (em milissegundos)

    for index, word in enumerate(text_parts):
        # Limpar a tela antes de mostrar cada palavra
        screen.blit(background_img, (0, 0))

        # Desenhar uma camada preta semi-transparente
        dark_layer = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
        dark_layer.set_alpha(128)  # Transparência de 50%
        dark_layer.fill(BLACK)
        screen.blit(dark_layer, (0, 0))

        # Exibir as palavras que já apareceram
        for i in range(index + 1):
            rendered_text = font.render(text_parts[i], True, color)
            word_x = x - rendered_text.get_width() // 2
            word_y = y + i * 80  # Espaço entre palavras
            screen.blit(rendered_text, (word_x, word_y))

        pygame.display.flip()
        pygame.time.delay(delay)

# Função do menu principal
def main_menu():
    menu_running = True

    # Realizar a animação do título antes de exibir o texto "Press ENTER to Start"
    animate_title(["CAT", "FISH"], 100, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 4)

    while menu_running:
        screen.blit(background_img, (0, 0))

        # Desenhar uma camada preta semi-transparente
        dark_layer = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
        dark_layer.set_alpha(128)  # Transparência de 50%
        dark_layer.fill(BLACK)
        screen.blit(dark_layer, (0, 0))

        # Exibir o título e o texto "Press ENTER to Start" estático após a animação
        show_text("CAT", 100, WHITE, SCREEN_WIDTH // 2 - 68, SCREEN_HEIGHT // 4)
        show_text("FISH", 100, WHITE, SCREEN_WIDTH // 2 - 80, SCREEN_HEIGHT // 4 + 80)

        # Mostrar instrução para começar
        show_text("Press ENTER to Start", 48, WHITE, SCREEN_WIDTH // 2 - 180, SCREEN_HEIGHT // 2 + 100)
        
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    menu_running = False  # Iniciar o jogo

# Relógio do jogo
clock = pygame.time.Clock()


# Função principal do jogo
def main_game():
    game_over = False
    score = 0
    player_x = SCREEN_WIDTH // 2
    player_y = SCREEN_HEIGHT - player_size
    circle_list.clear()
    triangle_list.clear()
    circle_speed = 5
    triangle_speed = 5
    moving = False

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True

        keys = pygame.key.get_pressed()
        moving = False
        if keys[pygame.K_LEFT] and player_x - player_speed > 0:
            player_x -= player_speed
            moving = True
        if keys[pygame.K_RIGHT] and player_x + player_speed < SCREEN_WIDTH - player_size:
            player_x += player_speed
            moving = True

        # Criar círculos e triângulos
        if random.randint(1, 20) == 1:
            create_circle()
        if random.randint(1, 25) == 1:
            create_triangle()

        move_objects(circle_list, circle_speed)
        move_objects(triangle_list, triangle_speed)

        # Verificar colisões
        if check_collision_circle(player_x, player_y, circle_list):
            score += 1
        if check_collision_triangle(player_x, player_y, triangle_list):
            game_over = True

        # Aumentar a dificuldade
        if score % 10 == 0 and score > 0:
            circle_speed += 0.5
            triangle_speed += 0.5

        # Desenhar fundo
        screen.blit(background_img, (0, 0))

        # Desenhar uma camada preta semi-transparente
        dark_layer = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
        dark_layer.set_alpha(128)  # Transparência de 50%
        dark_layer.fill(BLACK)
        screen.blit(dark_layer, (0, 0))

        # Desenhar jogador
        draw_player(player_x, player_y, moving)

        # Desenhar círculos e triângulos
        for circle in circle_list:
            screen.blit(img_circle, (circle[0] - circle_radius, circle[1] - circle_radius))
        for triangle in triangle_list:
            draw_triangle(triangle[0], triangle[1], triangle[2])

        # Exibir pontuação
        show_text(f"Pontos: {score}", 36, WHITE, 10, 10)

        pygame.display.flip()

        clock.tick(30)

    return score

# Exibir o menu antes de começar o jogo
main_menu()

# Loop principal do jogo
while True:
    score = main_game()
    if not game_over_screen(score):
        break

pygame.quit()
