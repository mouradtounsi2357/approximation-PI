#!/usr/bin/python3
#-------------------------------------------------------------------#
# MOURAD TOUNSI                                                     #
#-------------------------------------------------------------------#
import math, pygame, sys, random

# initiation pygame ------------------------$
pygame.init()
display=pygame.display.set_mode((400,500))
pygame.display.set_caption("approximation de PI")
clock=pygame.time.Clock()
fps=60

# classes ----------------------------------$
class Random_point():
    def __init__(self):
        self.pos=(0,0)
        self.color=(0,200,0)

    def draw(self):
        pygame.draw.rect(display,self.color,(self.pos[0],self.pos[1],1,1))
    
    def update(self):
        self.pos=(random.randrange(0,401,1),random.randrange(0,401,1))

class Image_pi_ap():
    def __init__(self):
        self.pos=(0,400)
        self.image=pygame.image.load("images/image_pi_ap.png")
    
    def draw(self):
        display.blit(self.image,self.pos)

class Calcul():
    def __init__(self):
        self.pos=(80,435)
        self.p_in=0
        self.p_all=0
        self.val_ap_pi=0

        self.font=pygame.font.Font(None,50)
        self.text=''
        self.color=(0,0,0)
        self.surface=self.font.render(self.text,True,self.color)
    
    def draw(self):
        display.blit(self.surface,self.pos)

    def update(self):
        self.val_ap_pi=4*(self.p_in/self.p_all)
        self.text=str("%.12f"%self.val_ap_pi)
        self.surface=self.font.render(self.text,True,self.color)


# setup ------------------------------------$
display.fill((0,0,40))
pygame.draw.circle(display, (200,0,0), (200,200), 200,1)
point=Random_point()
image_pi=Image_pi_ap()
calc=Calcul()

# main loop --------------------------------$
while 1:
    # logic --------------------------------$
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    point.update()
    if math.sqrt((point.pos[0]-200)**2+(point.pos[1]-200)**2) <= 200:
        calc.p_all+=1
        calc.p_in+=1
    else:
        calc.p_all+=1
    calc.update()

    # draw ---------------------------------$
    point.draw()
    image_pi.draw()
    calc.draw()
    
    # update screen ------------------------$
    pygame.display.flip()
    clock.tick(fps)
