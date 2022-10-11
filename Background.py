import pygame
class Background():
    def __init__(self,img,x,y,WINDOWWIDTH,WINDOWHEIGHT):
        self.x = x
        self.y = y
        self.WINDOWWIDTH = WINDOWWIDTH
        self.BG = pygame.transform.scale(img,(1000,WINDOWHEIGHT))
        self.scroll_x = 0
    def draw(self,DISPLAYSURF):
        DISPLAYSURF.blit(self.BG,(self.x,self.y))
        
    def move(self, player):
        self.scroll_x = 0
        if player.player_rect.right > self.WINDOWWIDTH - self.x:
            self.scroll_x = -player.speed
            self.x += self.scroll_x
        if player.player_rect.left < -self.x:
            self.scroll_x = -player.speed
            self.x += self.scroll_x