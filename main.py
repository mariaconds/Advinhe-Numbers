import pygame
import sys

# Inicializa o Pygame
pygame.init()

# Define as cores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PURPLE = (139, 0, 139)

# Define as dimensões da tela
WIDTH = 1000
HEIGHT = 800

# Cria a tela
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Define o título da janela
pygame.display.set_caption("Tela Inicial do Jogo")

# Carrega a imagem de fundo
background_image = pygame.image.load("fundo1.png")
background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))

# Define a fonte para os botões
font = pygame.font.Font(None, 36)

# Cria os botões
class Button:
    def __init__(self, x, y, width, height, text, color):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = font.render(text, True, BLACK)
        self.color = color

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)
        screen.blit(self.text, (self.rect.x + 50, self.rect.y + 10))

duvidas_button = Button(WIDTH / 2 - 100, HEIGHT / 2 - 50, 200, 50, "Dúvidas", PURPLE)
jogo_button = Button(WIDTH / 2 - 100, HEIGHT / 2 + 50, 200, 50, "Jogo", PURPLE)

click = False

#editar menu para click - https://docs.google.com/document/d/1JxJGtLIPXa3yoAMUmnSKJuk2KK_1tRQuoKuUeNOroP0/edit 

def main_menu():
# Loop principal
    while True:
     for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if duvidas_button.rect.collidepoint(event.pos):
                #print("Botão 'Dúvidas' clicado")
            if click:#editar esssa parte
                duvida() #editar esssa parte


            elif jogo_button.rect.collidepoint(event.pos):
                #print("Botão 'Jogo' clicado")
                jogo() #editar esssa parte
                # Adicione aqui a lógica para direcionar para outra tela
"""
        #editar esssa parte
        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
"""



    # Desenha a imagem de fundo
     screen.blit(background_image, (0, 0))

    # Desenha os botões
     duvidas_button.draw(screen)
     jogo_button.draw(screen)

    # Atualiza a tela
     pygame.display.flip()

    # Limita a taxa de quadros
     pygame.time.Clock().tick(60)


#Definições dos Submenus dos Botões - Game - Opções - Sair --------------------#
def jogo():
   
        screen.fill((0,0,0))

def duvida():
   
        screen.fill((0,0,0))

       
main_menu()

