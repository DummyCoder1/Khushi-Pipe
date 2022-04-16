import pygame, sys,random

pygame.init()
#pygame.mixer.init()

clock=pygame.time.Clock()
width=400
height=600
screen = pygame.display.set_mode((width,height))
  
#load the images in dict
images={}
images["bg"] = pygame.image.load("bg.png").convert_alpha()
images["base"] = pygame.image.load("base.png").convert_alpha()
images["bee"] = pygame.image.load("bee.png").convert_alpha()
images["pipe"] = pygame.image.load("pipe.png").convert_alpha()
groundx=0

class Bee:
    speed=5
    g=0.5
    bee= pygame.Rect(100,250,30,30)

    def gravity(self):
        self.speed=self.speed+self.g
        self.bee.y= self.bee.y + self.speed

    def flap(self):
        self.speed=-10
    
    def display(self):
        screen.blit(images["bee"],self.bee) 

class Pipe:
    def __init__(self,x):
        self.gap=random.randint(150, 400)
        self.topPipe=pygame.Rect(x,self.gap-400,40,320)
        #Create a rect named bottomPipe
        self.bottomPipe=pygame.Rect(x,self.gap+100,40,320)
        
    def display(self):
        screen.blit(images["pipe"],self.topPipe)
        #Display the pipe image on bottomPipe 
        screen.blit(images["pipe"],self.bottomPipe)
        #pygame.draw.rect(screen,(250,150,50),pygame.Rect(200,self.gap,100,100))
        
bee=Bee()
pipe1= Pipe(200)
#Create second pipe object at 300
pipe2=Pipe(300)

while True:    
    screen.fill((50,150,255))
    screen.blit(images["bg"],[0,0])
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            pygame.quit()
            sys.exit() 
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bee.flap()
                        
    bee.gravity() 
    groundx =groundx-5
    if groundx< -330:
        groundx=0

    bee.display()  
    pipe1.display()
    #Display second pipe
    screen.blit(images["base"],[groundx,550])
    pipe2.display()
    
    pygame.display.update()
    clock.tick(30) 
