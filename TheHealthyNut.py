# Team Banana 

from pygame.locals import *
import pygame

# Welcome page for the player!
def welcome():
    pygame.init()
    screen = pygame.display.set_mode((684, 684))

    # Fill background
    screen.fill((250, 250, 250))
    
    # Display some text
    font = pygame.font.Font(None, 36)
    text = font.render("TheHealthyNut", 1, (10, 10, 10))
    textpos = text.get_rect()
    textpos.centerx = screen.get_rect().centerx

    # Updating our page 
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                if event.key == K_SPACE:
                    return
                
        # Blinking image using timer
        image = pygame.image.load("healthynut.png")
        screen.blit(image,(0,0))
        pygame.time.delay(300)
        pygame.display.flip()
        image = pygame.image.load("healthynut1.png")
        screen.blit(image,(0,0))
        pygame.time.delay(300)
        pygame.display.flip()
        pygame.display.update()

# The player that you move around
class Player:
    # Initial position at the start
    x = 57
    y = 57

    # Change in movement 
    speed = 57
 
    def moveRight(self):
        self.x = self.x + self.speed
 
    def moveLeft(self):
        self.x = self.x - self.speed
 
    def moveUp(self):
        self.y = self.y - self.speed
 
    def moveDown(self):
        self.y = self.y + self.speed

# Maze class responsible for filling and updating
# the maze 
class Maze:

    def __init__(self):
       self.M = 12
       self.N = 12
       
       # One-dimensional array storing a 2-D maze
       self.maze = [ 1,1,1,1,1,1,1,1,1,1,1,1,
                     1,0,0,0,0,0,0,0,0,0,3,1,
                     1,5,1,1,2,0,1,1,1,0,0,1,
                     1,0,1,0,0,0,0,0,1,4,1,1,
                     1,0,1,0,1,0,7,0,0,1,0,12,
                     1,0,0,0,1,0,1,0,0,0,0,1,
                     1,0,1,3,1,0,1,11,0,1,1,1,
                     12,0,0,0,0,0,1,1,0,0,10,1,
                     1,8,0,1,1,0,0,6,1,0,0,1,
                     1,1,0,0,0,1,0,0,1,0,1,1,
                     1,0,0,9,0,0,5,0,0,0,0,1,
                     12,0,1,1,1,1,1,1,1,1,0,12,]


    # Draws the maze and items in the maze
    def draw(self, display_surf): 
       bx = 0
       by = 0
       
       for i in range(0,self.M*self.N):
           
           if self.maze[bx + (by*self.M)] == 1:
               image = pygame.image.load("grassF.png").convert()
               display_surf.blit(image, (bx*57, by*57))

           elif self.maze[bx + (by*self.M)] == 2:
               image = pygame.image.load("tofu.png").convert()
               display_surf.blit(image, (bx*57, by*57))

           elif self.maze[bx + (by*self.M)] == 3:
               image = pygame.image.load("thyme.png").convert()
               display_surf.blit(image, (bx*57, by*57))

           elif self.maze[bx + (by*self.M)] == 4:
               image = pygame.image.load("tea.png").convert()
               display_surf.blit(image, (bx*57, by*57))

           elif self.maze[bx + (by*self.M)] == 5:
               image = pygame.image.load("spinach.png").convert()
               display_surf.blit(image, (bx*57, by*57))

           elif self.maze[bx + (by*self.M)] == 6:
               image = pygame.image.load("pistachios.png").convert()
               display_surf.blit(image, (bx*57, by*57))

           elif self.maze[bx + (by*self.M)] == 7:
               image = pygame.image.load("eggs.png").convert()
               display_surf.blit(image, (bx*57, by*57))

           elif self.maze[bx + (by*self.M)] == 8:
               image = pygame.image.load("dairy.png").convert()
               display_surf.blit(image, (bx*57, by*57))

           elif self.maze[bx + (by*self.M)] == 9:
               image = pygame.image.load("coffee.png").convert()
               display_surf.blit(image, (bx*57, by*57))

           elif self.maze[bx + (by*self.M)] == 10:
               image = pygame.image.load("coconutmilk.png").convert()
               display_surf.blit(image, (bx*57, by*57))

           elif self.maze[bx + (by*self.M)] == 11:
               image = pygame.image.load("amaranth.png").convert()
               display_surf.blit(image, (bx*57, by*57))

           elif self.maze[bx + (by*self.M)] == 12:
               image = pygame.image.load("exit.png").convert()
               display_surf.blit(image, (bx*57, by*57))

           bx = bx + 1
           if bx > self.M-1:
               bx = 0 
               by = by + 1
 
class App:
 
    windowWidth = 684
    windowHeight = 684
    player = None

    
    # Initialize needed variables later used in updating the game 
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
        pygame.display.set_caption('Know your iron!')
        self._running = True
        self._image_surf = pygame.image.load("person1.png").convert()


    # Exit game by the red x on the top right corner
    def on_event(self, event):
        if event.type == QUIT:
            self._running = False
 
    def on_loop(self):
        pass

    #It renders the white background, the walls, the items, and the player
    def on_render(self):
        self._display_surf.fill((255,255,255))
        self._display_surf.blit(self._image_surf,(self.player.x,self.player.y))
        self.maze.draw(self._display_surf)
        pygame.display.flip()

    #exits the game
    def on_cleanup(self):
        pygame.quit()

    #Game start
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
    welcome()
    theApp = App()
    theApp.on_execute()
