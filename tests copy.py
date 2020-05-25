import pygame, os
from ctypes import windll
windll.shcore.SetProcessDpiAwareness(1)

pygame.init()

largeur, hauteur = 1920, 1080
fenetre = pygame.display.set_mode((largeur,hauteur), flags = pygame.FULLSCREEN)

def getImgBank(path: str) -> dict:
	"""Return a dict containing all images in a folder with recursion."""
	d = {}
	for f in os.listdir(path):
		if len(f) > 4 and f[-4:] in ('.png', '.jpg'):
			d[f[:-4]] = pygame.image.load(f'{path}/{f}').convert_alpha()
		else:
			d[f] = getImgBank(f'{path}/{f}')
	return d

bank = getImgBank("images/Space")

continuer = True
i=0

N,S,E,W,NE,NW,SE,SW = True,False,False,False,False,False,False,False
angle = 0
anglemax = 0
x,y = 800, 400

while continuer:
	i+=1
	touches = pygame.key.get_pressed()

	if touches[pygame.K_ESCAPE] :
		continuer=False

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			continuer = False


	if touches[pygame.K_d]: #E
		N,S,E,W,NE,NW,SE,SW = False,False,True,False,False,False,False,False
		x+=5
		
	if touches[pygame.K_a]: #W
		N,S,E,W,NE,NW,SE,SW = False,False,False,True,False,False,False,False
		x-=5
	if touches[pygame.K_w]: #N
		N,S,E,W,NE,NW,SE,SW = True,False,False,False,False,False,False,False
		y-=5
		
	if touches[pygame.K_s]: #S
		N,S,E,W,NE,NW,SE,SW = False,True,False,False,False,False,False,False
		y+=5
			
	if touches[pygame.K_w] and touches[pygame.K_a]: #NW
		N,S,E,W,NE,NW,SE,SW = False,False,False,False,False,True,False,False
		
	if touches[pygame.K_w] and touches[pygame.K_d]: #NE
		N,S,E,W,NE,NW,SE,SW = False,False,False,False,True,False,False,False

	if touches[pygame.K_s] and touches[pygame.K_a]: #SW
		N,S,E,W,NE,NW,SE,SW = False,False,False,False,False,False,False,True

	if touches[pygame.K_s] and touches[pygame.K_d]: #SE
		N,S,E,W,NE,NW,SE,SW = False,False,False,False,False,False,True,False


	fenetre.blit(bank["background"],(0,0))

	if N:
		if 46<=angle<=180:
			anglemax = 0

		elif 180<angle<=316:
			anglemax = 360

		if angle < anglemax:
			angle+=2
			fenetre.blit(pygame.transform.rotate(bank["tile000"], -angle), (x, y))

		elif angle > anglemax:
			angle-=2
			fenetre.blit(pygame.transform.rotate(bank["tile000"], -angle), (x, y))
		
		elif angle == anglemax:
			fenetre.blit(pygame.transform.rotate(bank["tile000"], -angle), (x, y))


	if S:
		anglemax = 180

		if angle < anglemax:
			angle+=2
			fenetre.blit(pygame.transform.rotate(bank["tile000"], -angle), (x, y))

		elif angle > anglemax:
			angle-=2
			fenetre.blit(pygame.transform.rotate(bank["tile000"], -angle), (x, y))
		
	
		elif angle == anglemax:
			fenetre.blit(pygame.transform.rotate(bank["tile000"], -angle), (x, y))

	if E:
		if angle == 360:
			angle = 0
		anglemax = 90

		if angle < anglemax:
			angle+=2
			fenetre.blit(pygame.transform.rotate(bank["tile000"], -angle), (x, y))

		elif angle > anglemax:
			angle-=2
			fenetre.blit(pygame.transform.rotate(bank["tile000"], -angle), (x, y))
		
		elif angle == anglemax:
			fenetre.blit(pygame.transform.rotate(bank["tile000"], -angle), (x, y))


	if W:
		if angle == 0:
			angle = 360
			
		anglemax = 270

		if angle < anglemax:
			angle+=2
			fenetre.blit(pygame.transform.rotate(bank["tile000"], -angle), (x, y))

		elif angle > anglemax:
			angle-=2
			fenetre.blit(pygame.transform.rotate(bank["tile000"], -angle), (x, y))
		
		elif angle == anglemax:
			fenetre.blit(pygame.transform.rotate(bank["tile000"], -angle), (x, y))


	if NW:
		if angle == 0:
			angle = 360
		anglemax = 316

		if angle < anglemax:
			angle+=2
			fenetre.blit(pygame.transform.rotate(bank["tile000"], -angle), (x, y))

		elif angle > anglemax:
			angle-=2
			fenetre.blit(pygame.transform.rotate(bank["tile000"], -angle), (x, y))
		
		elif angle == anglemax:
			fenetre.blit(pygame.transform.rotate(bank["tile000"], -angle), (x, y))

	if NE:
		anglemax = 46

		if angle < anglemax:
			angle+=2
			fenetre.blit(pygame.transform.rotate(bank["tile000"], -angle), (x, y))

		elif angle > anglemax:
			angle-=2
			fenetre.blit(pygame.transform.rotate(bank["tile000"], -angle), (x, y))
		
		elif angle == anglemax:
			fenetre.blit(pygame.transform.rotate(bank["tile000"], -angle), (x, y))


	if SE:
		anglemax = 136

		if angle < anglemax:
			angle+=2
			fenetre.blit(pygame.transform.rotate(bank["tile000"], -angle), (x, y))

		elif angle > anglemax:
			angle-=2
			fenetre.blit(pygame.transform.rotate(bank["tile000"], -angle), (x, y))
		
		elif angle == anglemax:
			fenetre.blit(pygame.transform.rotate(bank["tile000"], -angle), (x, y))

	if SW:
		anglemax = 226

		if angle < anglemax:
			angle+=2
			fenetre.blit(pygame.transform.rotate(bank["tile000"], -angle), (x, y))

		elif angle > anglemax:
			angle-=2
			fenetre.blit(pygame.transform.rotate(bank["tile000"], -angle), (x, y))
		
		elif angle == anglemax:
			fenetre.blit(pygame.transform.rotate(bank["tile000"], -angle), (x, y))
	
	

	pygame.display.update()