import pygame
import random
pygame.init()

largeur, hauteur = 600, 400
fenetre=pygame.display.set_mode((largeur,hauteur))


class ElementGraphique():
	# Le constructeur basique
	def __init__(self, img, x, y):
		self.image = img
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y

	def Afficher(self, window) :
		window.blit(self.image, self.rect)

	
	
class Perso(ElementGraphique):
	def __init__(self, img, x, y, largeur, hauteur):
		ElementGraphique.__init__(self, img, x, y)
		self.vie = 2.5
		self.vitesse = 1

	def Deplacer(self, touches):
		if touches[pygame.K_RIGHT] and self.rect.x <= largeur-self.rect.w:
			self.rect.x += self.vitesse
		if touches[pygame.K_LEFT] and self.rect.x >= 0:
			self.rect.x -= self.vitesse
		if touches[pygame.K_UP] and self.rect.y >= 0:
			self.rect.y -= self.vitesse
		if touches[pygame.K_DOWN] and self.rect.y <= hauteur-self.rect.h:
			self.rect.y += self.vitesse

	def enVie(self):
		if self.vie <= 0:
			return False
		return True

	def move(self, objectif):
		if objectif.rect.x > self.rect.x:
			self.rect.x += self.vitesse

		if objectif.rect.x < self.rect.x:
			self.rect.x -= self.vitesse

		if objectif.rect.y > self.rect.y:
			self.rect.y += self.vitesse

		if objectif.rect.y < self.rect.y:
			self.rect.y -= self.vitesse


		

class Enemys(ElementGraphique):
	def __init__(self, img, x, y, pouvoir, v, rebmax):
		ElementGraphique.__init__(self, img, x, y)
		self.vx = v
		self.vy = v
		self.reb = 0
		self.pouvoir = pouvoir
		self.rebmax = rebmax
	
	def Deplacer(self):
		if self.rect.x 

	
	def CheckSkins(self):
		if self.pouvoir == 0:
			self.image = pygame.image.load("balle.png")

		if self.pouvoir == 1:
			self.image = pygame.image.load("bonus.png")

		if self.pouvoir == 2:
			self.image = pygame.image.load("mort.png")

		if self.pouvoir == 3:
			self.image = pygame.image.load("coeur.png")
	
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


font = pygame.font.Font(None, 30)
font2 = pygame.font.Font(None, 70)

imageFondJeu = pygame.image.load("background.jpg").convert_alpha()
imageFondM = pygame.image.load("BackgroundM.png").convert_alpha()
imagePerso = pygame.image.load("perso.png").convert_alpha()
imageobjectif = pygame.image.load("coeur.png").convert_alpha()

imagePlay = font2.render("Play", 1, (255, 0, 0))
imageExit = font2.render("Exit", 1, (255, 0, 0))

fondjeu = ElementGraphique(imageFondJeu, 0, 0)
objectif = Enemys(imageobjectif, 150, 100, largeur, hauteur, 0)
fondmenu = ElementGraphique(imageFondM, 0, 0)
perso = Perso(imagePerso, random.randint(0, 600), random.randint(0, 400), largeur, hauteur)

Play = ElementGraphique(imagePlay, largeur//2, hauteur//5)
Play.rect.x -= Play.rect.w//2

Exit = ElementGraphique(imageExit,largeur//2 ,3 * hauteur//5)
Exit.rect.x -= Exit.rect.w//2

horloge = pygame.time.Clock()

i=0
secondes = 0
continuer = 1
state = "Menu"

enemys = []

while continuer:

	horloge.tick(60)
	i+=1

	touches = pygame.key.get_pressed()

	if touches[pygame.K_ESCAPE] :
		continuer=0

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			continuer = 0

	if state == "Menu":

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

		fondjeu.Afficher((fenetre)) 
		perso.Afficher((fenetre))
		perso.move(objectif)
		vie.Afficher(fenetre)
		temps.Afficher(fenetre)
		objectif.Afficher(fenetre)

		if perso.enVie():
			state = "Jeu"
		
		else:
			state = "Menu"

	pygame.display.flip()

pygame.quit()