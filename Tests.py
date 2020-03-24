import pygame
import random

pygame.init()

largeur, hauteur = 700, 700
fenetre=pygame.display.set_mode((largeur,hauteur))

def images():
	bank = {}
	bank["fond"] = pygame.image.load("background.jpg")
	bank["coeur"] = pygame.image.load("coeur.png").convert_alpha()
	bank["mort"] = pygame.image.load("mort.png").convert_alpha()
	return bank

bank = images()

horloge = pygame.time.Clock()

CoeurX = 150
CoeurY = 150

MortX = 200
MortY = 500

vX = 5
vY = 5

i = 0
continuer = True
while continuer:
	horloge.tick(30)
	touches = pygame.key.get_pressed()

	i+=1

	if i%70 == 0:
		MortX = random.randint(50, 650)
		MortY = random.randint(50, 650)

	if touches[pygame.K_ESCAPE] :
		continuer=0

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			continuer = 0
	
	if CoeurX > MortX:
		if vX > -5:
			vX -= 1

	if CoeurY > MortY:
		if vY > -5:
			vY -= 1
	
	if CoeurX < MortX:
		if vX < 5:
			vX += 1

	if CoeurY < MortY:
		if vY < 5:
			vY += 1

	if CoeurY == MortY:
		vY = 0

	if CoeurX == MortX:
		vX = 0

	CoeurX += vX
	CoeurY += vY
	CoCoeur = (CoeurX, CoeurY)
	CoMort = (MortX, MortY)

	fenetre.blit(bank["fond"], (0,0))
	fenetre.blit(bank["coeur"], CoCoeur)
	fenetre.blit(bank["mort"], CoMort)
	pygame.display.update()