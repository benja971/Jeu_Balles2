import pygame
from pygame.locals import *

from ctypes import windll
windll.shcore.SetProcessDpiAwareness(1)

pygame.init()

def images():
	bank={}
	bank["perso"] = pygame.image.load("Dragon1.png").convert_alpha()
	bank["mort"] = pygame.image.load("mort.png").convert_alpha()

	return bank


class Perso:
	"""docstring for Perso"""
	def __init__(self):
		self.v = 2
		self.image = bank["perso"]
		self.rect = self.image.get_rect()
		self.rect.x = 102
		self.rect.y = 102


	def move(self):
		if touches[K_LEFT] and self.rect.x - self.rect.w > -self.rect.w:
			self.rect.x -= self.v

		if touches[K_RIGHT] and self.rect.x + self.rect.w  < 1262:
			self.rect.x += self.v	

		if touches[K_UP] and self.rect.y - self.rect.h > -self.rect.h:
			self.rect.y -= self.v

		if touches[K_DOWN] and self.rect.y + self.rect.h < 632:
			self.rect.y += self.v	


class Ennemy:
	"""docstring for Ennemy"""
	def __init__(self):
		self.image = bank["mort"]
		self.v = 4
		self.rect = self.image.get_rect()
		self.rect.x = 500
		self.rect.y = 500
		
	def collisions(self, perso):
		if self.rect.colliderect(perso.rect):
			pass	

	def move(self, perso):
		if perso.rect.x < self.rect.x:
			self.rect.x -= self.v

		if perso.rect.x > self.rect.x:
			self.rect.x += self.v

		if perso.rect.y < self.rect.y:
			self.rect.y -= self.v

		if perso.rect.y > self.rect.y:
			self.rect.y += self.v



fenetre = pygame.display.set_mode((1262, 632))
horloge = pygame.time.Clock()

bank = images()
fond = pygame.image.load("bg2-bell.jpg").convert()

continuer = True
pygame.key.set_repeat(4, 4)

perso = Perso()
ennemy = Ennemy()
Prect = perso.rect
Mrect = ennemy.rect

i = 0
Tennemy = []
Tennemy.append(Ennemy())

while continuer:

	horloge.tick(60)
	i+=1
	# print(i, end ='\r')

	touches = pygame.key.get_pressed()
	events = pygame.event.get()

	perso.move()
	ennemy.collisions(perso)
	ennemy.move(perso)

	if touches[K_ESCAPE]:
			continuer = False
	

	if i%1000 == 0 and ennemy.v < 5:
		ennemy.v+=0.2

		if ennemy.v == 4:
			Tennemy.append(Ennemy())


	fenetre.blit(fond, (0 ,0))
	fenetre.blit(bank["perso"],Prect)

	for e in Tennemy:
		# print(Tennemy, end = '\r')
		fenetre.blit(bank["mort"], e)

	pygame.display.flip()	