import pygame, sys
from pygame.locals import*
from Background import Background
from Player import Player
pygame.init()

#fps
fpsclock=pygame.time.Clock()
Fps = 45

#Variable
WINDOWWIDTH = 960
WINDOWHEIGHT = 504

#screen
DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH,WINDOWHEIGHT))
#dir
pygame.display.set_caption('Pico Park')
screen = pygame.display.set_mode((WINDOWWIDTH,WINDOWHEIGHT))

pl_img = pygame.image.load('phai.png')
BG = pygame.image.load('bg.png').convert_alpha()

bg = Background(BG,0,0,WINDOWWIDTH,WINDOWHEIGHT)
player = Player(pl_img,0,int(WINDOWHEIGHT-112),40,47,WINDOWHEIGHT)

left,right = False,False
gravity = 1
while True:
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
		if event.type == KEYDOWN:
			if player.flag_jump:
				if event.key == K_UP:
					player.movement = 0
					player.movement -=18
					player.flag_jump = False
			if event.key == K_LEFT:
				left = True
			if event.key == K_RIGHT:
				right = True
			if event.key == K_p:#pause
				pass
			if event.key == K_n:#new game
				pass
		if event.type == KEYUP:
			if event.key == K_LEFT:
				left = False
			if event.key == K_RIGHT:
				right = False
	player.movement += gravity
	bg.draw(DISPLAYSURF)
	bg.move(player)
	player.draw(DISPLAYSURF)
	player.move(bg,left,right)
	pygame.display.update()
	fpsclock.tick(Fps)