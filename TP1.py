import pygame
import json
from random import randint, random

pygame.init()

largeur, hauteur = 1920, 1080
fenetre=pygame.display.set_mode((largeur,hauteur), flags = pygame.FULLSCREEN)

scores = {}

def images(font, font2):
	bank = {}
	bank["imageFondJeu"] = pygame.image.load("background.jpg")
	bank["imageFondM"] = pygame.image.load("test.jpg").convert_alpha()
	bank["perso"] = pygame.image.load("perso.png").convert_alpha()
	bank["bonus"] = pygame.image.load("bonus.png").convert_alpha()
	bank["coeur"] = pygame.image.load("coeur.png").convert_alpha()
	bank["mort"] = pygame.image.load("mort.png").convert_alpha()
	bank["balle"] = pygame.image.load("balle.png").convert_alpha()
	bank["play"] = font2.render("Play", 1, (255, 0, 0)).convert_alpha()
	bank["exit"] = font2.render("Exit", 1, (255, 0, 0)).convert_alpha()		
	return bank

class ElementGraphique():
	# Le constructeur basique
	def __init__(self, img: pygame.Surface, x, y):
		self.image = img
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y

	def Afficher(self, window) :
		window.blit(self.image, self.rect)

	
class Perso(ElementGraphique):
	def __init__(self, img, x, y, largeur, hauteur):
		ElementGraphique.__init__(self, img, x, y)
		self.vie = 1
		self.vitesse = 10

	def Deplacer(self, touches):
		if touches[pygame.K_d] and self.rect.x <= largeur-self.rect.w:
			self.rect.x += self.vitesse
		if touches[pygame.K_a] and self.rect.x >= 0:
			self.rect.x -= self.vitesse
		if touches[pygame.K_w] and self.rect.y >= 0:
			self.rect.y -= self.vitesse
		if touches[pygame.K_s] and self.rect.y <= hauteur-self.rect.h:
			self.rect.y += self.vitesse

	def enVie(self):
		if self.vie <= 0:
			return False
		return True
		

class Enemys(ElementGraphique):
	def __init__(self, img, x, y, pouvoir, v, rebmax):
		ElementGraphique.__init__(self, img, x, y)
		self.vx = v
		self.vy = v
		self.reb = 0
		self.pouvoir = pouvoir
		self.rebmax = rebmax
	
	def Deplacer(self):
		rebond = False
		if self.rect.y + self.rect.h >= hauteur:
			self.vy = -abs(self.vy)
			rebond = True
		
		if self.rect.y < 0:
			self.vy = abs(self.vy)
			rebond = True

		if self.rect.x +self.rect.w >= largeur:
			self.vx = -abs(self.vx)
			rebond = True

		if self.rect.x <= 0:
			self.vx = abs(self.vx)
			rebond = True

		if rebond:
			self.reb += 1

		if self.reb == self.rebmax:
			enemys.remove(balle)

		self.rect.y += self.vy
		self.rect.x += self.vx
	
	
	def Collisions(self, Perso):
		if self.rect.colliderect(Perso.rect):
			if self.pouvoir == 0:
				enemys.remove(balle)
				Perso.vie -= 1
			
			if self.pouvoir == 1:
				enemys.clear()

			if self.pouvoir == 2:
				enemys.remove(balle)
				Perso.vie -= 2
			
			if self.pouvoir == 3:
				enemys.remove(balle)
				Perso.vie += 1


def NewBalle(enemys):
	nbr = random()
	if 0 <= nbr < 0.5:
		enemys.append(Enemys(bank["balle"] ,randint(0, largeur), randint(0, hauteur), 0, randint(1, 4), randint(5, 15)))

	if 0.5 <= nbr < 0.7:
		enemys.append(Enemys(bank["bonus"] ,randint(0, largeur), randint(0, hauteur), 1, randint(1, 4), randint(5, 15)))

	if 0.7 <= nbr < 0.85:
		enemys.append(Enemys(bank["mort"],randint(0, largeur), randint(0, hauteur), 2, randint(1, 4), randint(5, 15)))

	if 0.85 <= nbr <= 1:
		enemys.append(Enemys(bank["coeur"],randint(0, largeur), randint(0, hauteur), 3, randint(1, 4), randint(5, 15)))

font = pygame.font.Font(None, 30)
font2 = pygame.font.Font(None, 70)
bank = images(font, font2)

fondjeu = ElementGraphique(bank["imageFondJeu"], 0, 0)
fondmenu = ElementGraphique(bank["imageFondM"], 0, 0)
perso = Perso(bank["perso"], 50, 70, largeur, hauteur)
Play = ElementGraphique(bank["play"], largeur//2, hauteur//5)
Play.rect.x -= Play.rect.w//2
Exit = ElementGraphique(bank["exit"], largeur//2 ,3 * hauteur//5)
Exit.rect.x -= Exit.rect.w//2

horloge = pygame.time.Clock()

i=0
secondes = 0
continuer = 1
state = "Menu"

enemys = []

while continuer:
	horloge.tick(30)
	i+=1

	touches = pygame.key.get_pressed()

	if touches[pygame.K_ESCAPE] :
		continuer=0

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			continuer = 0

	if state == "Menu":

		perso.vie = 1
		secondes = 0
		fondmenu.Afficher(fenetre)
		Play.Afficher(fenetre)
		Exit.Afficher(fenetre)

		if touches[pygame.K_RETURN]:
			state = "Jeu"

	if state == "Jeu":

		imagevie = font.render("Vies: "+str(perso.vie), 1, (255, 255, 255))		
		vie = ElementGraphique(imagevie, 0,5)

		imagetemps = font.render("Secondes: "+str(secondes), 1, (255, 255, 255))
		temps = ElementGraphique(imagetemps, 0,25)

		if i %60 == 0:
			secondes += 1

		if i %75 == 0:
			NewBalle(enemys)


		fondjeu.Afficher((fenetre))
		perso.Afficher((fenetre))
		perso.Deplacer(touches)
		vie.Afficher(fenetre)
		temps.Afficher(fenetre)

		if perso.enVie():
			state = "Jeu"
		
		else:
			state = "Menu"

			name = input("Quel est votre nom: ")

			with open('data.json') as json_data:
					scores = json.load(json_data)
					scores.update({"Best score": 0})
					
			if name not in scores:
					scores.update({name: str(secondes)})

			if int(scores[str(name)]) < int(secondes):
					scores.update({name: str(secondes)})

			s = []

			for sc in scores:
				s.append(int(scores[sc]))

			s = sorted(s)

			scores.update({"Best score": (s[-1])}) 

			with open('data.json', 'w') as fp:
				json.dump(scores, fp, indent=4)

		for balle in enemys:
			balle.Afficher((fenetre))
			balle.Deplacer()
			balle.Collisions(perso)

	pygame.display.flip()

pygame.quit()