import pygame
import pgzrun
import random
import math
WIDTH = 1000
global l
l=1
HEIGHT = 400
TITLE = "vou fazer um desenho muito legal e essa fonte doi meu olho"
class Heroi(Actor):
    def __init__(self,image,x,y):
        super().__init__(image,(x,y))
        self.pontos=0
        self.fase=0
        self.morreu= 1
        self.estado_jogo="espera"
        self.vida=3
heroi = Heroi("heroy",1,200)
global moelas
moelas=[]
def mudar_cor():
    a=random.randint(0,200)
    b=random.randint(0,200)
    c=random.randint(0,200)
    global d
    d=(a,b,c)
def redimensionar(ator,altura):
    escala=altura/ator.height
    novo=pygame.transform.smoothscale(
        ator._orig_surf,(int(ator.width*escala),altura)
    )
    ator._orig_surf = ator._surf = novo
    ator._update_pos()
def criar_uva(): 
    global moelas 
    posiçãox=300 
    posiçãoy=random.randint(10,390)
    moela= Actor("uvapassa",(posiçãox,posiçãoy))
    for i in range(1,8):
        moelas.append(moela)
        posiçãox+=100
        posiçãoy= random.randint((posiçãoy-15),(posiçãoy+15))
        while posiçãoy <=10 or posiçãoy>= 390:
            posiçãoy= random.randint((posiçãoy-15),(posiçãoy+15))
        moela= Actor("uvapassa",(posiçãox, posiçãoy))
class Pepino(Actor):
    def __init__(self,image):
        super().__init__(image)
        self.no_topo=True
        self.direito= True
    def pingo_pong(self):
        if self.no_topo == True:
            self.y+= 1
        elif self.no_topo == False:
            self.y-= 1
        if self.direito == True:
            self.x -=1
        elif self.direito == False:
            self.x +=1
pepino = Pepino("pepino")
pepino.y = 200
pepino.x = 999
redimensionar(pepino,80)
class Coruja(Actor):
    def __init__(self,image):
        super().__init__(image)
        self.raio_visão = 160
        self.passo_raio = 10
        self.waypoints = ((500,200),(125,200),(0,75,),(250,325),(500,75),(750,325),(1000,85))
        self.waypoint_atual=0
        self.obstaculos=[
        Rect((200,80),(500,200))
        ]
    def visao (self,heroi):
        dx=self.x-heroi.x
        dy=self.y-heroi.y
        diagonal=math.hypot(dx,dy)

        if self.raio_visão<diagonal:
            return False
        if self.raio_visão>diagonal:
            return True
        if diagonal == 0:
            return True
        dir_x = dx/diagonal
        dir_y = dy/diagonal
        andos=int (diagonal/self.passo_raio)
        for p in range (1,andos):
            circulinhos_x= self.x+ dir_x * (p*self.passo_raio)
            circulinhos_y= self.y+ dir_y * (p*self.passo_raio)
            for reangulo in self.obstaculos:
                if retangulo.collidepoint ((circulinhos_x,circulinhos_y)):
                    return False
        return True
        

    def movimentacao(self,heroi):
        if self.visao(heroi)== True:
            alvo_x = heroi.x
            alvo_y = heroi.y
        else:
            alvo_x,alvo_y = self.waypoints[self.waypoint_atual]
            longe_waypoint=math.hypot(alvo_x-self.x,alvo_y-self.y)
            if longe_waypoint<5:
                self.waypoint_atual=(self.waypoint_atual+1)% 7
        if self.x!= alvo_x:
            if alvo_x<self.x:
                self.x-=2
            elif alvo_x>self.x:
                self.x+=2
        if self.y != alvo_y:
            if alvo_y<self.y:
                self.y-=2
            elif alvo_y>self.y:
                self.y+=2
        
corujinha= Coruja("coruja")
corujinha.x=500
corujinha.y=200
d = (225,59,93)
def update():
    global l, moelas
    if heroi.estado_jogo=="jogando":
        corujinha.movimentacao(heroi)
        if heroi.vida<=0:
            heroi.fase-=1
            heroi.vida=3
            heroi.estado_jogo="espera"
        if heroi.pontos>=35:
            heroi.pontos=0
            heroi.fase+=1
            heroi.estado_jogo="espera"
        if keyboard.o:
            heroi.pontor=0
            heroi.fase+=1
            heroi.estado_jogo="espera"
        if keyboard.left:
            heroi.x-=7
        if keyboard.right:
            heroi.x+=1*l
            l+=0.2
        if keyboard.up:
            heroi.y-=5
        if keyboard.down:
            heroi.y+=5
        if not keyboard.right:
            l=1
        if heroi.x >=1000:
            heroi.x=1
            criar_uva()
        elif heroi.x<=0:
            heroi.x+=10
        if heroi.y>=400:
            heroi.y=1
        if heroi.y<=0:
            heroi.y=399
        if not keyboard.i:
            if pepino.x >= (WIDTH - 10):
                pepino.direito = True
            elif pepino.x <=10:
                pepino.direito = False
            if pepino.y >= (HEIGHT - 10):
                mudar_cor()
                pepino.no_topo= False
            elif pepino.y <= 10:
                mudar_cor()
                pepino.no_topo=True
            pepino.pingo_pong()
           
        if heroi.colliderect(pepino) or heroi.colliderect(corujinha):
            heroi.vida-=1
            heroi.morreu = 3
            heroi.estado_jogo="espera"
        for moela in moelas[:]: 
            if moela.colliderect(heroi):
                heroi.pontos+=1
                moelas.remove(moela) 
    if heroi.estado_jogo=="espera":
        heroi.pos=(1,200)
        pepino.pos=(999,200)
        moelas=[]
        if keyboard.p:
            heroi.estado_jogo="jogando"
            heroi.morreu = 2
            corujinha.x=500
        



def draw():
    if heroi.estado_jogo == "jogando":
        screen.fill(d)
        heroi.draw()  
        pepino.draw()
        corujinha.draw()
        for retangulo in corujinha.obstaculos:
            screen.draw.rect(Rect,"mediumvioletred")
        #for i,wp in enumerate (corujinha.waypoints):
            #screen.draw.filled_circle(wp,14,"yellowgreen")
        screen.draw.circle((corujinha.x,corujinha.y),corujinha.raio_visão,"mediumslateblue")
        for moela in moelas:
            moela.draw()
        screen.draw.text(f"Pontos: {heroi.pontos}", topleft=(20, 20), fontsize=32, color="black", shadow=(1, 1), scolor="pink")
        screen.draw.text(f"Vidas:  {heroi.vida*" - <3"}", topright=(800, 20), fontsize=32, color="black", shadow=(1, 1), scolor="pink")
    if heroi.estado_jogo =="espera":
        if heroi.morreu == 2:
            screen.fill((0,200,0))
            screen.draw.text("^.^",center=(WIDTH/2,HEIGHT/2),fontsize = 50, color="black")
        elif heroi.morreu == 3:
            screen.fill((200,0,0))
            screen.draw.text("vc morreu",center=(WIDTH/2,HEIGHT/2),fontsize = 50, color="black")
        elif heroi.morreu == 1:
            screen.fill((0,0,200))
            screen.draw.text("precione 'p' para começar",center=(WIDTH/2,HEIGHT/4),fontsize = 50, color="black")
    
pgzrun.go()
