import pygame

pygame.init()

largeur, hauteur = 1920, 1080
fenetre=pygame.display.set_mode((largeur,hauteur), flags = pygame.FULLSCREEN)

f = pygame.image.load("background.jpg")
i = 0

while i<300:
    i+=1
    print(i)
    fenetre.blit(f, (0,0))
    pygame.display.flip()