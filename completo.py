import pygame
import random

# Inicializa o Pygame
pygame.init()

# Define as constantes
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BUTTON_COLOR = (139, 0, 139)  # Cor do botão (verde)

# Carrega a imagem de fundo
background_image = pygame.image.load('fundo.jpg')
background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))

# Cria a tela do jogo
tela = pygame.display.set_mode((WIDTH, HEIGHT))

# Define a fonte
font = pygame.font.Font(None, 36)

# Cria o botão de início
start_button = pygame.Rect(WIDTH // 2 - 50, HEIGHT - 50, 100, 30)

# Loop principal do jogo
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            break
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if start_button.collidepoint(event.pos):
                # Reinicia o jogo
                print("Botão Início clicado!")           

                # INICIO PROGRAMA JOGO
                # Define as constantes
                MIN_NUMBER = 1
                MAX_NUMBER = 100
                MAX_ATTEMPTS = 6

                # Gera um número aleatório entre MIN_NUMBER e MAX_NUMBER
                secret_number = random.randint(MIN_NUMBER, MAX_NUMBER)

                # Inicializa a variável de tentativas
                attempts = 0

                # Cria a tela do jogo
                tela = pygame.display.set_mode((800, 600))

                # Define as cores
                WHITE = (255,255,255)
                BLACK = (0, 0, 0)

                # Define a fonte
                font = pygame.font.Font(None, 36)

                # Função para desenhar o texto na tela
                def draw_text(text, x, y):
                    text_surface = font.render(text, True, BLACK)
                    tela.blit(text_surface, (x, y))

                # Função para desenhar o input field
                def draw_input_field(x, y, width, height):
                    pygame.draw.rect(tela, BLACK, (x, y, width, height), 2)

                # Função para lidar com o input do usuário
                def handle_input(input_str):
                    global attempts
                    global secret_number
                    try:
                        user_number = int(input_str)
                        if user_number < MIN_NUMBER:
                            return f"Erro: O número deve ser maior ou igual a {MIN_NUMBER}!"
                        elif user_number > MAX_NUMBER:
                            return f"Erro: O número deve ser menor ou igual a {MAX_NUMBER}!"
                        elif user_number == secret_number:
                            return "Parabéns! Você adivinhou o número!"
                        elif user_number > secret_number:
                            attempts += 1
                            return "O número é menor que isso. Tente novamente!"
                        else:
                            attempts += 1
                            return "O número é maior que isso. Tente novamente!"
                    except ValueError:
                        return "Erro: Insira um número válido!"

                # Cria o input field
                input_field = pygame.Rect(100, 100, 200, 30)

                # Variável para armazenar o input do usuário
                input_str = ""
                mensagem = ""

                # Cria o botão de início
                start_button = pygame.Rect(350, 550, 100, 30)

                # Loop principal do jogo
                while True:
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            pygame.quit()
                            break
                        elif event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_RETURN:
                                mensagem = handle_input(input_str)
                                input_str = ""
                                if attempts == MAX_ATTEMPTS:
                                    mensagem = f"Você não adivinhou o número. O número secreto era {secret_number}."
                            elif event.key == pygame.K_BACKSPACE:
                                input_str = input_str[:-1]
                            else:
                                input_str += event.unicode
                        elif event.type == pygame.MOUSEBUTTONDOWN:
                            if start_button.collidepoint(event.pos):
                                # Reinicia o jogo
                                secret_number = random.randint(MIN_NUMBER, MAX_NUMBER)
                                attempts = 0
                                input_str = ""
                                mensagem = ""

                    # Desenha a tela do jogo
                    tela.fill(WHITE)
                    draw_text("Bem-vindo ao jogo de Adivinhe Numbers!", 100, 50)
                    draw_text(f"Eu estou pensando em um número entre {MIN_NUMBER} e {MAX_NUMBER}.", 100, 80)
                    draw_input_field(100, 100, 200, 30)
                    draw_text("Insira um número:", 100, 130)
                    draw_text(input_str, 110, 110)
                    draw_text(mensagem, 100, 200)

                    # Desenha o botão de início
                    pygame.draw.rect(tela, BLACK, start_button, 2)
                    draw_text("RECOMEÇAR", 355, 555)

                    # Atualiza a tela
                    pygame.display.update()

                # FIM PROGRAMA JOGO


    # Desenha a tela do jogo
    tela.blit(background_image, (0, 0))
    pygame.draw.rect(tela, BUTTON_COLOR, start_button)  # Desenha o botão com a cor escolhida
    draw_text = font.render("Início", True, BLACK)
    tela.blit(draw_text, (start_button.x + 10, start_button.y + 5))

    # Atualiza a tela
    pygame.display.update()
