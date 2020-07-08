import pygame
import turtle
import random 
from pygame.locals import MOUSEBUTTONDOWN, Rect, QUIT
from sys import exit
import operator


def ApagarArq(nomes_arq):
       os.remove(nomes_arq) 
       
       
def lerArq(nomes_arq):
       #Lê todas as linhas do arquivo
       Texto = []
       arq = open(nomes_arq,"r")
       while True:
              linha = arq.readline()
              if linha == "":
                     break
              else:
                     Texto.append(linha.rstrip())

       arq.close()
       return Texto

def salvarScore (nome,pontos,nomes_arq):
       scores  = lerArq(nomes_arq)
    
       arq = open("Score.txt",'w')
       

       for i in range(len(scores)):
              arq.write(str(scores[i]) + "\n")
                 
                 
       arq.write(nome + "\n")
       arq.write(str(pontos) + "\n")
            
       arq.close()
     

def OrganizarArq(nomes_arq):
       
       score = lerArq(nomes_arq)
       
       nomes = []
       pontos = []
       
       for i in range(0,len(score),2):
              
              nomes.append(score[i])
              pontos.append(score[i+1])
              
       
       dicionario = {}
       for i in range(len(nomes)):
              dicionario.update({nomes[i]: pontos[i]})

 
       
       dicionario = sorted(dicionario.items(), key=operator.itemgetter(1),reverse= True)
       
 
       nomes = []
       pontos = []
       
         
       for i in range(0,len(dicionario),1):
             
              nomes.append(dicionario[i][0])
              pontos.append(dicionario[i][1])



       return nomes,pontos


def Ia():
    if VEZ == "JOGADOR2":
        lista = []
        for i in range(len(marca_tabu)):
            if marca_tabu[i] != "X" and marca_tabu[i] != "O":
                lista.append(i)

       
        escolha = random.choice(lista)
        print(lista,escolha)
        if escolha == 0:
             confimar(0, [100, 100])
        if escolha == 1:
            confimar(1, [300, 100])
        if escolha == 2:
            confimar(2, [500, 100])
        if escolha == 3:
            confimar(3, [100, 300])
        if escolha == 4:
            confimar(4, [300, 300])
        if escolha == 5:
            confimar(5, [500, 300])
        if escolha == 6:
            confimar(6, [100, 500])
        if escolha == 7:
            confimar(7, [300, 500])
        if escolha == 8:
            confimar(8, [500, 500])
        
    


def desenhar_linhas():
    WHITE = (0,0,0)
    pygame.draw.line(tela, (WHITE), (200, 0), (200, 600), 10)
    pygame.draw.line(tela, (WHITE), (400, 0), (400, 600), 10)
    pygame.draw.line(tela, (WHITE), (0, 200), (600, 200), 10)
    pygame.draw.line(tela, (WHITE), (0, 400), (600, 400), 10)


    
def testa_pos():
    for p in rec:
        if e.type == MOUSEBUTTONDOWN and p.collidepoint(mouse_pos):
            if p == rect1:
                confimar(0, [100, 100])
            if p == rect2:
                confimar(1, [300, 100])
            if p == rect3:
                confimar(2, [500, 100])
            if p == rect4:
                confimar(3, [100, 300])
            if p == rect5:
                confimar(4, [300, 300])
            if p == rect6:
                confimar(5, [500, 300])
            if p == rect7:
                confimar(6, [100, 500])
            if p == rect8:
                confimar(7, [300, 500])
            if p == rect9:
                confimar(8, [500, 500])
    

def desenhar_peca(pos):
    global VEZ
    x, y = pos
    if VEZ == 'JOGADOR2':
        img = pygame.image.load('bola.png').convert_alpha()
        imgR = pygame.transform.scale(img, (100, 100))
        tela.blit(imgR, (x - 50, y - 50))
    else:
        img = pygame.image.load('x.png').convert_alpha()
        imgR = pygame.transform.scale(img, (100, 100))
        tela.blit(imgR, (x - 50, y - 50))

def desenhar_fundo():
   
    img = pygame.image.load('fundo-azul.png').convert_alpha()
    imgR = pygame.transform.scale(img, (1000, 1000))
    tela.blit(imgR, (-190, -70))
    pygame.draw.line(tela, (0,0,0), (0, 0), (600, 0),75)


def placar(nomes,pontos):
    
    pygame.draw.rect(tela,(255,255,255),(50,38,500,530))
    pygame.draw.rect(tela,(52,4,204),(50,38,500,50))
    
    arial = pygame.font.SysFont('timesnewroman', 35)
    Nomes = 'Nomes'
    Pontos = 'Pontos'

    nome_t = arial.render(Nomes, True, (255, 255, 255))
    ponto_t = arial.render(Pontos, True, (255, 255, 255))
    tela.blit(nome_t, (140, 40))
    tela.blit(ponto_t, (380, 40))


    altura = 100

    maximo = len(nomes)
    if maximo > 10:
           maximo = 10
    for i in range(maximo):
           pos_t = str(i+1) + '-'
           pos_t = arial.render(pos_t, True, (181, 13, 108))
           tela.blit(pos_t, (80, altura))
             
           nomes_t  = str(nomes[i])
           nomes_t = arial.render(nomes_t, True, (0, 0, 0))
           tela.blit(nomes_t,(140,altura))
                   
         
           pontos_t  = str(pontos[i])
           pontos_t = arial.render(pontos_t, True, (0, 0, 0))
           tela.blit(pontos_t,(415,altura))

           
           altura += 45
           
           
    
   
       
    
def confimar(indice, pos):
    global ESCOLHA, VEZ, espaco
    if marca_tabu[indice] == 'X':
        
        print('X')
        
    elif marca_tabu[indice] == 'O':
        print('O')
        
    else:
        marca_tabu[indice] = ESCOLHA
        if VEZ == 'JOGADOR1':
            ClickSound()
        else:
            ClickSound2()
            
        desenhar_peca(pos)
        print(marca_tabu)
        if VEZ == 'JOGADOR1':
            VEZ = 'JOGADOR2'
        else:
            VEZ = 'JOGADOR1'
        espaco +=1



def texto_vitoria(v):
    arial = pygame.font.SysFont('arial', 50)
    mensagem = 'JOGADOR {} VENCEU'.format(v)

    if v == 'EMPATE':
        mens_vitoria = arial.render('DEU VELHA', True, (255, 255, 255), 0)
        tela.blit(mens_vitoria, (158, 265))
    else:
        mens_vitoria = arial.render(mensagem, True, (255, 255, 255), 0)
        tela.blit(mens_vitoria, (40, 265))


def teste_vitoria(l):
    return ((marca_tabu[0] == l and marca_tabu[1] == l and marca_tabu[2] == l) or
        (marca_tabu[3] == l and marca_tabu[4] == l and marca_tabu[5] == l) or
        (marca_tabu[6] == l and marca_tabu[7] == l and marca_tabu[8] == l) or
        (marca_tabu[0] == l and marca_tabu[3] == l and marca_tabu[6] == l) or
        (marca_tabu[1] == l and marca_tabu[4] == l and marca_tabu[7] == l) or
        (marca_tabu[2] == l and marca_tabu[5] == l and marca_tabu[8] == l) or
        (marca_tabu[0] == l and marca_tabu[4] == l and marca_tabu[8] == l) or
        (marca_tabu[2] == l and marca_tabu[4] == l and marca_tabu[6] == l))

def reset():
        global ESCOLHA, ESTADO, VEZ, marca_tabu, espaco
        ESTADO = 'JOGANDO'
        VEZ = 'JOGADOR1'
        ESCOLHA = 'X'
        espaco = 0
        marca_tabu = [
            0, 1, 2,
            3, 4, 5,
            6, 7, 8
        ]
        tela.fill(0)

def pontos(pontos1, pontos2):
    arial = pygame.font.SysFont('timesnewroman', 30)
    arial2 = pygame.font.SysFont('timesnewroman', 20)
    
    jogador1 = 'Player = {}'.format(pontos1)
    jogador2 = 'Maquina = {}'.format(pontos2)
    placar = "Aperte P para ver o placar"


    plc = arial2.render(placar, True, (255, 255, 255))
    jd1 = arial.render(jogador1, True, (255, 255, 255))
    jd2 = arial.render(jogador2, True, (255, 255, 255))
    tela.blit(jd1, (10, 0))
    tela.blit(jd2, (435, 0))
    tela.blit(plc, (190,5))

pygame.init()

tela = pygame.display.set_mode((600, 600), 0, 32,pygame.RESIZABLE)
pygame.display.set_caption('Jogo da Velha')

#Sons

music = pygame.mixer.music.load('Venkatesananda.ogg')
click = pygame.mixer.Sound('click.ogg.wav')
click2 = pygame.mixer.Sound('click2.wav')


pygame.mixer.music.set_volume(0.8)
pygame.mixer.music.play(-1)

def ClickSound():
    click.play()
    
def ClickSound2():
    click2.play()
    

ESTADO = 'JOGANDO'
VEZ = 'JOGADOR1'
ESCOLHA = 'X'
espaco = 0
marca_tabu = [
    0, 1, 2,
    3, 4, 5,
    6, 7, 8
]

rect1 = Rect((0, 0), (200, 200))
rect2 = Rect((200, 0), (200, 200))
rect3 = Rect((400, 0), (200, 200))
rect4 = Rect((0, 200), (200, 200))
rect5 = Rect((200, 200), (200, 200))
rect6 = Rect((400, 200), (200, 200))
rect7 = Rect((0, 400), (200, 200))
rect8 = Rect((200, 400), (200, 200))
rect9 = Rect((400, 400), (200, 200))

rec = [
    rect1,rect2,rect3,rect4,
    rect5,rect6,rect7,rect8,rect9,
]

pontos1, pontos2 = 0, 0

print(pygame.font.get_fonts())

desenhar_fundo()

exibido = False
flag = True
inicio_jogo = False
nomes_arq = OrganizarArq("Score.txt")[0]
pontos_arq = OrganizarArq("Score.txt")[1]
while True:
    
    
    mouse_pos = pygame.mouse.get_pos()
    if ESTADO == 'JOGANDO':

        nomes_arq = OrganizarArq("Score.txt")[0]
        pontos_arq = OrganizarArq("Score.txt")[1]
        #BAGULHO LOUCO

        pressed = pygame.key.get_pressed()
      
        
        if pressed[pygame.K_p] and inicio_jogo == False :
    
              exibido = False
             
              placar(nomes_arq,pontos_arq)
              
              flag = False
              
       
        if flag == False:
              pygame.display.update()
              desenhar_fundo()
              flag = True
              
        desenhar_linhas()
        
        pontos(pontos1, pontos2)

        for e in pygame.event.get():
            if e.type == QUIT:
                nome = turtle.textinput("Escreva o seu nome", "Este nome ficara salvo")
                if nome == "":
                    nome = "Vazio"
                salvarScore(nome,pontos1,"Score.txt")
                pygame.quit()
                exit()
            if e.type == MOUSEBUTTONDOWN:
                inicio_jogo = True
                pygame.time.delay(50)
                
                if VEZ == 'JOGADOR1':
                    ESCOLHA = 'X'
                    testa_pos()
                       
        
                else:   
                    ESCOLHA = 'O'
                    #testa_pos()
                    Ia()
        """ 
        nomes_arq = OrganizarArq("Score.txt")[0]
        pontos_arq = OrganizarArq("Score.txt")[1]
        
        pressed = pygame.key.get_pressed()
        
        if pressed[pygame.K_w]:
              print("w is pressed")
              placar(nomes_arq,pontos_arq)
       
        """
              

        if teste_vitoria('X'):
            print('X VENCEU')
            texto_vitoria('X')
            ESTADO = 'RESET'
            pontos1 += 1

        elif teste_vitoria('O'):
            print('O VENCEU')
            texto_vitoria('O')
            ESTADO = 'RESET'
            pontos2 +=1

        elif espaco >= 9:
            print('EMPATE')
            texto_vitoria('EMPATE')
            ESTADO = 'RESET'

    else:
        inicio_jogo = False
        for u in pygame.event.get():
            if u.type == QUIT:
                nome = turtle.textinput("Escreva o seu nome", "Este nome ficara salvo")
                if nome == "":
                       nome = "Vazio"
                salvarScore(nome,pontos1,"Score.txt")
                pygame.quit()
                exit()
            if u.type == MOUSEBUTTONDOWN:
    
                reset()
                desenhar_linhas()
                desenhar_fundo()

    pygame.display.flip()
