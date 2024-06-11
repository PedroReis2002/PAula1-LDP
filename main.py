import pygame
from pygame import Surface, Rect

# Variáveis para alterar o tamanho da janela
W_WIDTH = 576
W_HEIGHT = 324

# Inicializar o modulo Pygame
pygame.init()
print("Setup Start")

# Criação de janela do PYgame
window: Surface = pygame.display.set_mode(size=(W_WIDTH, W_HEIGHT))

# Carregar imagem e gerar uma superfície
Background_surface = pygame.image.load("./Asset/Background.png").convert_alpha()
# Carregar a imagem que gera a nave
Player_Surf = pygame.image.load("./Asset/Nave1.png").convert_alpha()

# Obter o retângulo da superfície
Background_retangulo: Rect = Background_surface.get_rect(left=0, top=0)
Player1_retangulo: Rect = Player_Surf.get_rect(left=30, top=150)

# Desenhar na janela (window)
window.blit(Background_surface, dest=Background_retangulo)
window.blit(Player_Surf, dest=Player1_retangulo)

# Atualizar a janela
pygame.display.flip()

# Colocar um relógio/ Definir framerate
clock = pygame.time.Clock()

# Carrega a música e loopa
pygame.mixer_music.load("./Asset/fase1.mp3")
pygame.mixer_music.play(-1)
pygame.mixer.music.set_volume(0.1)

print("Setup End")
print("Loop Start")
while True:
    clock.tick(60) # Coloca a framerate máxima do jogo em 120 FPS
    # print(clock.get_fps()) # Mostra o FPS no terminal o FPS
    window.blit(Background_surface, dest=Background_retangulo)
    window.blit(source=Player_Surf, dest=Player1_retangulo)
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("Loop End")
            pygame.quit()
            quit()
    pressed_key = pygame.key.get_pressed()
    if pressed_key[pygame.K_w]:
        Player1_retangulo.centery -= 2
    if pressed_key[pygame.K_s]:
        Player1_retangulo.centery += 2
    if pressed_key[pygame.K_d]:
        Player1_retangulo.centerx += 2
    if pressed_key[pygame.K_a]:
        Player1_retangulo.centerx -= 2
        pass
