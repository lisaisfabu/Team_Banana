from pygame.locals import *
import pygame

iron = {1:'grassF.png', 2:'spinach.png', 3:'tofu.png', 4:'pistachios.png',
        5:'amaranth.png', 6:'coconutmilk.png',
        7:'coffee.png', 8:'tea.png', 9:'dairy.png', 10:'eggs.png',
        11:'thyme.png'}

class Player:
    x = 57
    y = 57
    speed = 57
 
    def moveRight(self):
        self.x = self.x + self.speed
 
    def moveLeft(self):
        self.x = self.x - self.speed
 
    def moveUp(self):
        self.y = self.y - self.speed
 
    def moveDown(self):
        self.y = self.y + self.speed
 
class Maze:
    def __init__(self):
       self.M = 12
       self.N = 12
       
       self.maze = [ 1,1,1,1,1,1,1,1,1,1,1,1,
                     1,0,0,0,0,0,0,0,0,0,0,1,
                     1,0,1,1,1,0,1,1,1,0,1,1,
                     1,0,1,0,0,0,0,0,1,0,1,1,
                     1,0,1,2,1,0,0,0,0,1,0,1,
                     1,0,0,0,1,0,1,0,0,0,0,1,
                     1,0,1,1,1,0,1,0,0,1,1,1,
                     1,0,0,0,0,0,1,1,0,0,0,1,
                     1,0,0,1,1,0,0,1,1,0,1,1,
                     1,1,0,1,1,1,0,1,1,0,1,1,
                     1,0,0,1,0,0,0,0,0,0,0,1,
                     1,1,1,1,1,1,1,1,1,1,0,0,]
 
    def draw(self,display_surf):
       bx = 0
       by = 0
       
       for i in range(0,self.M*self.N):
           #index = self.maze[ bx + (by*self.M) ]
           
           if self.maze[ bx + (by*self.M) ] == 1:
               display_surf.blit(pygame.image.load.(iron.get(1)).covert(),( bx * 57, by * 57))
           elif self.maze[ bx + (by*self.M) ] == 2:
               display_surf.blit(pygame.image.load.(iron.get(2)).covert(),( bx * 57, by * 57))
           elif self.maze[ bx + (by*self.M) ] == 3:
               display_surf.blit(pygame.image.load.(iron.get(3)).covert(),( bx * 57, by * 57))
           elif self.maze[ bx + (by*self.M) ] == 4:
               display_surf.blit(pygame.image.load.(iron.get(4)).covert(),( bx * 57, by * 57))
           elif self.maze[ bx + (by*self.M) ] == 5:
               display_surf.blit(pygame.image.load.(iron.get(5)).covert(),( bx * 57, by * 57))
           elif self.maze[ bx + (by*self.M) ] == 6:
               display_surf.blit(pygame.image.load.(iron.get(6)).covert(),( bx * 57, by * 57))
           elif self.maze[ bx + (by*self.M) ] == 7:
               display_surf.blit(pygame.image.load.(iron.get(7)).covert(),( bx * 57, by * 57))
           elif self.maze[ bx + (by*self.M) ] == 8:
               display_surf.blit(pygame.image.load.(iron.get(8)).covert(),( bx * 57, by * 57))
           elif self.maze[ bx + (by*self.M) ] == 9:
               display_surf.blit(pygame.image.load.(iron.get(9)).covert(),( bx * 57, by * 57))
           elif self.maze[ bx + (by*self.M) ] == 10:
               display_surf.blit(pygame.image.load.(iron.get(10)).covert(),( bx * 57, by * 57))
           elif self.maze[ bx + (by*self.M) ] == 11:
               display_surf.blit(pygame.image.load.(iron.get(11)).covert(),( bx * 57, by * 57))

               
           bx = bx + 1
           if bx > self.M-1:
               bx = 0 
               by = by + 1
        
 
 
class App:
 
    windowWidth = 684
    windowHeight = 684
    player = 0
 
    def __init__(self):
        self._running = True
        self._display_surf = None
        self._image_surf = None
        self._block_surf = None
        self.player = Player()
        self.maze = Maze()
 
    def on_init(self):
        pygame.init()
        self._display_surf = pygame.display.set_mode((self.windowWidth,self.windowHeight), pygame.HWSURFACE)
 
        pygame.display.set_caption('Pygame pythonspot.com example')
        self._running = True
        self._image_surf = pygame.image.load("person.png").convert()
        self._block_surf = pygame.image.load("grassF.png").convert()
 
    def on_event(self, event):
        if event.type == QUIT:
            self._running = False
 
    def on_loop(self):
        pass
 
    def on_render(self):
        self._display_surf.fill((255,255,255))
        self._display_surf.blit(self._image_surf,(self.player.x,self.player.y))
        self.maze.draw(self._display_surf)
        pygame.display.flip()
 
    def on_cleanup(self):
        pygame.quit()
 
    def on_execute(self):
        if self.on_init() == False:
            self._running = False
 
        
        while (self._running):
            for event in pygame.event.get():
                if event.type == QUIT:
                    self._running = False
                if event.type == KEYDOWN:
                    if event.key == K_DOWN:
                        self.player.moveDown()
                    if event.key == K_UP:
                        self.player.moveUp()
                    if event.key == K_LEFT:
                        self.player.moveLeft()
                    if event.key == K_RIGHT:
                        self.player.moveRight()
                    if event.key == K_ESCAPE:
                        self._running = False
     
            self.on_loop()
            self.on_render()
        self.on_cleanup()
 
if __name__ == "__main__" :
    theApp = App()
    theApp.on_execute()
