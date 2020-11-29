import random
import pygame
import math
pygame.init()

size = (1000,600)
screen = pygame.display.set_mode(size)
fps = 35
clock = pygame.time.Clock()
col = pygame.color.THECOLORS
list_airbots = []
boss_count = 0
phase = preview = 'preview'
phase_action = 'main'
naruto_y = 100
E_move = 0
elite_count = 0
class AirBots: #
    def __init__(self,x,y):
        self.y = y
        self.list = [i for i in range(x,x+101)] #координаты х по которым оно будет двигаться вперед
        self.reverse = self.list[::-1] # и обратно
        self.left = random.choice([True,False])
        self.c = 0
        self.count = random.randint(0,fps)
        self.rights = [pygame.transform.scale(pygame.image.load('bots img/bat_right_3.png'),(50,50)),
                       pygame.transform.scale(pygame.image.load('bots img/bat_right_2.png'),(50,50)),
                       pygame.transform.scale(pygame.image.load('bots img/bat_right_1.png'),(50,50))
                      ]
        self.lefts = [pygame.transform.scale(pygame.image.load('bots img/bat_left_3.png'),(50,50)),
                      pygame.transform.scale(pygame.image.load('bots img/bat_left_2.png'),(50,50)),
                      pygame.transform.scale(pygame.image.load('bots img/bat_left_1.png'),(50,50))
                      ]
    def blit(self):
        if self.c>=100:
            self.left = not self.left
            self.c = 0
        self.c += 2
        self.count %=fps
        if self.left:
            screen.blit(self.rights[self.count//12],(self.list[self.c],self.y))
        else:
            screen.blit(self.lefts[self.count//12],(self.reverse[self.c],self.y))
        self.count+=1
list_earthbots = []
class EarthBots:
    def __init__(self,x,y,animal):
        self.y = y
        self.list = [i for i in range(x,x+101)]
        self.reverse = self.list[::-1]
        self.c = 0
        self.animal = animal
        self.count = random.randint(0,fps)
        self.left = random.choice([True,False])
    def blit(self):
        if self.animal == 'bear':
            self.width,self.height = 80,70
        else:
            self.width,self.height = 60,50
        self.lefts = [
            pygame.transform.scale(pygame.image.load('bots img/' + self.animal + '_left_1.png'),(self.width,self.height)),
            pygame.transform.scale(pygame.image.load('bots img/' + self.animal + '_left_2.png'),(self.width,self.height)),
            pygame.transform.scale(pygame.image.load('bots img/' + self.animal + '_left_3.png'),(self.width,self.height)),
            pygame.transform.scale(pygame.image.load('bots img/' + self.animal + '_left_4.png'),(self.width,self.height)),
            pygame.transform.scale(pygame.image.load('bots img/' + self.animal + '_left_5.png'),(self.width,self.height)),
            pygame.transform.scale(pygame.image.load('bots img/' + self.animal + '_left_6.png'),(self.width,self.height))
        ]
        self.rights = [
            pygame.transform.scale(pygame.image.load('bots img/' + self.animal + '_right_1.png'),(self.width,self.height)),
            pygame.transform.scale(pygame.image.load('bots img/' + self.animal + '_right_2.png'),(self.width,self.height)),
            pygame.transform.scale(pygame.image.load('bots img/' + self.animal + '_right_3.png'),(self.width,self.height)),
            pygame.transform.scale(pygame.image.load('bots img/' + self.animal + '_right_4.png'),(self.width,self.height)),
            pygame.transform.scale(pygame.image.load('bots img/' + self.animal + '_right_5.png'),(self.width,self.height)),
            pygame.transform.scale(pygame.image.load('bots img/' + self.animal + '_right_6.png'),(self.width,self.height))
        ]
        self.count%=(fps+4)
        if self.c>=100:
            self.left = not self.left
            self.c = 0
        if self.left:
            screen.blit(self.lefts[self.count//7],(self.list[self.c],self.y))
        else:
            screen.blit(self.rights[self.count//7],(self.reverse[self.c],self.y))
        self.c+=2
        self.count+=1
list_shoot = []
class Shoot:
    def __init__(self,x,y,look=-1):
        self.x = x
        self.y = y
        self.look = look
    def blit(self):
        suriken = pygame.transform.scale(pygame.image.load('bots img/shuriken.png'),(40,30)) 
        #suriken = pygame.transform.rotate(suriken,self.angle)
        screen.blit(suriken,(self.x,self.y))
        self.x-=10
        
        #self.y += 10*math.sin(math.radians(self.angle))/math.sin(math.radians(90-self.angle))

def boss():
    global list_shoot
    global boss_count
    boss_x,boss_y = 300,size[1]*0.75 - 100
    steps = [pygame.transform.scale(pygame.image.load('bots img/step-1.png'),(70,100)),
             pygame.transform.scale(pygame.image.load('bots img/step-2.png'),(70,100)),
             pygame.transform.scale(pygame.image.load('bots img/step-3.png'),(70,100)),
             pygame.transform.scale(pygame.image.load('bots img/step-4.png'),(70,100))]
    steps += [pygame.transform.scale(pygame.image.load('bots img/step-1.png'),(70,100))]*4
    
    boss_count %= 2*fps
    screen.blit(steps[boss_count//10],(boss_x,boss_y))
    boss_count+=1
    if boss_count == 15:
        list_shoot.append(Shoot(boss_x,boss_y+30))
    
for i in range(3):
    list_airbots.append(AirBots(random.randint(100,500),size[1]*3//4-80))
    list_earthbots.append(EarthBots(random.randint(100,500),size[1]*3//4-60,random.choice(['bear','boar'])))
done = False
def Sure():
    global done
    sure = False
    subscreen = pygame.Surface((500,300))
    ans = pygame.font.SysFont('Segoe Script',50,True)
    quest = pygame.font.SysFont('Segoe Script',30,True,True)
    answers=[
        [100,180,'YES',col['black'],1],
        [300,180,'NO',col['black'],2]
    ]
    answer = 0
    question = quest.render('Are you sure to quit?',True,col['darkgreen'],col['palegreen4'])
    while not sure:
        screen.blit(subscreen,(250,150))
        subscreen.blit(pygame.transform.scale(pygame.image.load('subscreen.jpeg'),(500,300)),(0,0))
        subscreen.blit(question,(50,120))
        mouse = pygame.mouse.get_pos()
        for i in answers:
            if i[0]+250<=mouse[0]<=i[0]+80+250 and i[1]+150<=mouse[1]<=i[1]+60+150:
                answer = i[4]
            if answer == i[4]:
                subscreen.blit(ans.render(i[2],True,i[3],col['blueviolet']),(i[0],i[1]))
            else:
                subscreen.blit(ans.render(i[2],True,i[3]),(i[0],i[1]))
                answer = 0
        for i in pygame.event.get():
            if i.type == pygame.MOUSEBUTTONDOWN and i.button == pygame.BUTTON_LEFT:
                if 100+250<=i.pos[0]<=180+250 and 180+150<=i.pos[1]<=240+150:
                    done = True
                    sure = True
                if 300+250<=i.pos[0]<=380+250 and 180+150<=i.pos[1]<=240+150:
                    sure = True
            
        pygame.display.flip()
        clock.tick(fps)
def Preview():
    global E_move,elite_count
    shrift = pygame.font.SysFont('Times New Roman',100,True)
    E = shrift.render('E',True,col['red3'])
    Ǝ = shrift.render('Ǝ',True,col['red3'])
    sego = pygame.font.SysFont('Segoe UI Black',40,True,True)
    bracket = pygame.font.SysFont('Calibri',80,True)
    screen.fill(col['black'])
    screen.blit(shrift.render('    I     ',True,col['red3']),(380,250))
    if 10<elite_count<30:
        screen.blit(bracket.render('][',True,col['red3']),(475,268))
    if 30<elite_count<70:
        screen.blit(shrift.render('    Ξ    ',True,col['red3']),(365,250))
    if 70<elite_count<=110:
        screen.blit(E,(460+E_move,250))
        screen.blit(Ǝ,(460-E_move,250))
        E_move+=3
        if elite_count==110:
            E_move=0
    if 100<elite_count<130:
        screen.blit(shrift.render(' L I T  ',True,col['red3']),(365,250))
    if 120<elite_count:
        screen.blit(shrift.render('Ξ L I T Ξ ',True,col['red3']),(300,250))
        screen.blit(shrift.render('I',True,col['red3']),(310-E_move,250))
        screen.blit(shrift.render('I',True,col['red3']),(650+E_move,250))
        if 140>=elite_count:
            E_move+=1
    if 180<elite_count:
        screen.blit(sego.render('PRODUCTION',True,col['red3']),(340,370))
    elite_count+=1

while not done:
    if phase==preview:
        Preview()
        if elite_count==250:
            phase = phase_action
        for i in pygame.event.get():
            if i.type == pygame.QUIT:
                Sure()

    if phase == phase_action:
        screen.fill(col['white'])
        pygame.draw.line(screen,col['orange'],(100,size[1]*3//4),(size[0]*2//3,size[1]*3//4),50)
        for i in pygame.event.get():
            if i.type == pygame.QUIT:
                Sure()
        for i,j in zip(list_airbots,list_earthbots):
            i.blit()
            j.blit()
        boss()
        for i in list_shoot:
            i.blit()
            if i.x < 0:
                list_shoot.remove(i)
    pygame.display.flip()
    clock.tick(fps)
pygame.quit()
