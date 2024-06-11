import pygame
from pygame import Surface

# Inicializar o modulo Pygame
pygame.init()
print("Setup Start")
# Criação de janela do PYgame
window: Surface = pygame.display.set_mode(size=(600, 400))

# Carregar imagem e gerar uma superfície
Background_surface = pygame.image.load("./Asset/Background.png")
# 48,35

print("Setup End")
print("Loop Start")
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("Loop End")
            pygame.quit()
            quit()
