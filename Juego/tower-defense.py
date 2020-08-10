import pygame

pygame.init()

flecha = False

pantalla = pygame.display.set_mode([400, 400])

NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)
VERDE = (0, 255, 0)
ROJO = (255, 0, 0)

imagen_de_fondo = pygame.image.load("fondoprehistoria.png").convert()
defensor = pygame.image.load("wachinprehistoria.jpg").convert()
flecha = pygame.image.load("lanzaprehistoria.png").convert()

personaje = defensor

pos = pygame.mouse.get_pos()

while not hecho:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            hecho = True
        if evento.type == pygame.MOUSEBUTTONDOWN:
            flecha = True
        if evento.type == pygame.MOUSEBUTTONUP:
            flecha = False

reloj = pygame.time.Clock()

hecho = False

    # Copia la imagen en pantalla:
    pantalla.blit(imagen_de_fondo, [x, y])

    pygame.display.flip()

    reloj.tick(60)

pygame.quit()
