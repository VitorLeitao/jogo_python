from turtle import update
import pygame
from pygame.locals import *
from sys import exit
import sys

pygame.init()
fonte = pygame.font.SysFont('arial', 40, True, False)
fonteover = pygame.font.Font('SpaceMission.otf', 70)
backgroundgameover = pygame.image.load('morte.jpg')
luara = pygame.time.Clock()
fonteinicio = fonteover = pygame.font.Font('SpaceMission.otf', 70)
# Classes

fimdejogo = True
quantidade = 0
class item(pygame.sprite.Sprite):
    def __init__(self, tipo,  x, y):
        # salvar os atributos do item
        self.tipo = tipo
        if self.tipo == 'tipo1':
            pygame.sprite.Sprite.__init__(self)
            self.sprites = []
            self.sprites.append(pygame.image.load('imagens/municao.png'))
            
            self.atual = 0
            self.image = self.sprites[self.atual]
            self.image = pygame.transform.scale(self.image, (32, 29))

            self.rect = self.image.get_rect()
            self.x = x
            self.y = y
            self.rect.topleft = self.x, self.y
        if self.tipo == 'tipo2':
            pygame.sprite.Sprite.__init__(self)
            self.sprites = []
            self.sprites.append(pygame.image.load('imagens/municao2.png'))
            
            self.atual = 0
            self.image = self.sprites[self.atual]
            self.image = pygame.transform.scale(self.image, (32, 29))

            self.rect = self.image.get_rect()
            self.x = x
            self.y = y
            self.rect.topleft = self.x, self.y
        if self.tipo == 'tipo3':
            pygame.sprite.Sprite.__init__(self)
            self.sprites = []
            self.sprites.append(pygame.image.load('imagens/municao3.png'))
            
            self.atual = 0
            self.image = self.sprites[self.atual]
            self.image = pygame.transform.scale(self.image, (32, 29))

            self.rect = self.image.get_rect()
            self.x = x
            self.y = y
            self.rect.topleft = self.x, self.y


# classe para os itens que vão afetar a vida do personagem, seja aumentanto, seja diminuindo
class item_modificador_vida(pygame.sprite.Sprite):
    def __init__(self, nome, tipo, x, y):
        self.nome = nome
        self.tipo = tipo
    
        if self.nome == 'armadilha':
            if self.tipo == 'tipo1':
                pygame.sprite.Sprite.__init__(self)
                self.dano = 1
                self.sprites = []
                self.sprites.append(pygame.image.load('imagens/porcaomorte.png'))
                
                self.atual = 0
                self.image = self.sprites[self.atual]
                self.image = pygame.transform.scale(self.image, (255/7, 255/7))

                self.rect = self.image.get_rect()
                self.x = x
                self.y = y
                self.rect.topleft = self.x, self.y
            if self.tipo == 'tipo2':
                pygame.sprite.Sprite.__init__(self)
                self.dano = 1.5
                self.sprites = []
                self.sprites.append(pygame.image.load('imagens/porcaomorte.png'))
                
                self.atual = 0
                self.image = self.sprites[self.atual]
                self.image = pygame.transform.scale(self.image, (255/7, 255/7))

                self.rect = self.image.get_rect()
                self.x = x
                self.y = y
                self.rect.topleft = self.x, self.y
            if self.tipo == 'tipo3':
                pygame.sprite.Sprite.__init__(self)
                self.dano = 2
                self.sprites = []
                self.sprites.append(pygame.image.load('imagens/porcaomorte.png'))
                
                self.atual = 0
                self.image = self.sprites[self.atual]
                self.image = pygame.transform.scale(self.image, (255/7, 255/7))

                self.rect = self.image.get_rect()
                self.x = x
                self.y = y
                self.rect.topleft = self.x, self.y
            if self.tipo == 'tipo4':
                pygame.sprite.Sprite.__init__(self)
                self.dano = 3
                self.sprites = []
                self.sprites.append(pygame.image.load('imagens/porcaomorte.png'))
                
                self.atual = 0
                self.image = self.sprites[self.atual]
                self.image = pygame.transform.scale(self.image, (255/10, 255/10))

                self.rect = self.image.get_rect()
                self.x = x
                self.y = y
                self.rect.topleft = self.x, self.y
            if self.tipo == 'tipo5':
                pygame.sprite.Sprite.__init__(self)
                self.dano = 2.5
                self.sprites = []
                self.sprites.append(pygame.image.load('imagens/porcaomorte.png'))
                
                self.atual = 0
                self.image = self.sprites[self.atual]
                self.image = pygame.transform.scale(self.image, (255/7, 255/7))

                self.rect = self.image.get_rect()
                self.x = x
                self.y = y
                self.rect.topleft = self.x, self.y
        elif self.nome == 'pocao':
            if tipo == 'tipo1':
                self.recuperar = 1
                pygame.sprite.Sprite.__init__(self)
                self.sprites = []
                self.sprites.append(pygame.image.load('imagens/porcaovida1.png'))
                
                self.atual = 0
                self.image = self.sprites[self.atual]
                self.image = pygame.transform.scale(self.image, (255/5, 255/5))

                self.rect = self.image.get_rect()
                self.x = x
                self.y = y
                self.rect.topleft = self.x, self.y
            if tipo == 'tipo2':
                self.recuperar = 1.5
                pygame.sprite.Sprite.__init__(self)
                self.sprites = []
                self.sprites.append(pygame.image.load('imagens/pocaovida2.png'))
                
                self.atual = 0
                self.image = self.sprites[self.atual]
                self.image = pygame.transform.scale(self.image, (255/7, 255/7))

                self.rect = self.image.get_rect()
                self.x = x
                self.y = y
                self.rect.topleft = self.x, self.y
            if tipo == 'tipo3':
                self.recuperar = 2
                pygame.sprite.Sprite.__init__(self)
                self.sprites = []
                self.sprites.append(pygame.image.load('imagens/pocaovida3.png'))
                
                self.atual = 0
                self.image = self.sprites[self.atual]
                self.image = pygame.transform.scale(self.image, (255/7, 255/7))

                self.rect = self.image.get_rect()
                self.x = x
                self.y = y
                self.rect.topleft = self.x, self.y
        elif self.nome == 'pocao_especial':
            self.nova_vida = 4
            pygame.sprite.Sprite.__init__(self)
            self.sprites = []
            self.sprites.append(pygame.image.load('imagens/pocaoespecial.png'))
            
            self.atual = 0
            self.image = self.sprites[self.atual]
            self.image = pygame.transform.scale(self.image, (255/7, 255/7))

            self.rect = self.image.get_rect()
            self.x = x
            self.y = y
            self.rect.topleft = self.x, self.y
    def update(self):
        self.rect.topleft = self.x, self.y


class personagens(pygame.sprite.Sprite):
    todos_personagens = []

    def __init__(self):
        self.nome = 'jhonny'
        self.vida = 2
        self.vidamaxima = 4
        self.vidadesejada = 3
        self.velocidade = 0.05
        self.velocidadedecaimento = 0.001
        pygame.sprite.Sprite.__init__(self)
        self.sprites = []
        self.sprites.append(pygame.image.load('imagens/boneco.png'))
        
        self.atual = 0
        self.image = self.sprites[self.atual]
        self.image = pygame.transform.scale(self.image, (131/8, 136/8))

        self.rect = self.image.get_rect()
        self.x = 20
        self.y = 10
        self.rect.topleft = self.x, self.y

        personagens.todos_personagens.append(self)
    def update(self):
        # Movimentação
        keys = pygame.key.get_pressed() 
      
        if keys[pygame.K_a] : 
            self.x -= 1
            
        if keys[pygame.K_d]: 
            self.x += 1
            
        if keys[pygame.K_w]: 
            self.y -= 1
            
        if keys[pygame.K_s]: 
            self.y += 1
        self.rect.topleft = self.x, self.y
    
    def voltar_inicio(self):
        self.x = 20
        self.y = 10
        self.rect.topleft = self.x, self.y


largura = 600
altura = 600
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('jogo projeto ip')
x = 20
y = 50

# Criando objetos
desenhar_armadilha_1 = True
desenhar_armadilha_2 = True
desenhar_armadilha_3 = True
desenhar_armadilha_4 = True
desenhar_armadilha_5 = True
desenhar_pocao_1 = True
desenhar_pocao_2 = True
desenhar_pocao_3 = True
desenhar_fragmento_1 = True
desenhar_fragmento_2 = True
desenhar_fragmento_3 = True
desenhar_pocao_especial = True
armadilha1 = item_modificador_vida('armadilha', 'tipo1', 100, 35)
armadilha2 = item_modificador_vida('armadilha', 'tipo2',  380, 75)
armadilha3 = item_modificador_vida('armadilha', 'tipo3', 160, 275)
armadilha4 = item_modificador_vida('armadilha', 'tipo4', 420, 530)
armadilha5 = item_modificador_vida('armadilha','tipo5', 535, 270)

sprite_armadilha1 = pygame.sprite.Group()
sprite_armadilha1.add(armadilha1)
sprite_armadilha2 = pygame.sprite.Group()
sprite_armadilha2.add(armadilha2)
sprite_armadilha3 = pygame.sprite.Group()
sprite_armadilha3.add(armadilha3)
sprite_armadilha4 = pygame.sprite.Group()
sprite_armadilha4.add(armadilha4)
sprite_armadilha5 = pygame.sprite.Group()
sprite_armadilha5.add(armadilha5)


pocao1 = item_modificador_vida('pocao',  'tipo1',30, 90)  
pocao2 = item_modificador_vida('pocao',  'tipo2',125, 380)
pocao3 = item_modificador_vida('pocao',  'tipo3',488, 450)

sprite_pocao1 = pygame.sprite.Group()
sprite_pocao1.add(pocao1)
sprite_pocao2 = pygame.sprite.Group()
sprite_pocao2.add(pocao2)
sprite_pocao3 = pygame.sprite.Group()
sprite_pocao3.add(pocao3)

pocaoespecial = item_modificador_vida('pocao_especial', 1, 110, 100)
sprite_super_pocao = pygame.sprite.Group()
sprite_super_pocao.add(pocaoespecial)


fragmento1 = item('tipo1', 470, 7)
fragmento2 = item('tipo2', 430, 230)
fragmento3 = item('tipo3', 120, 550)

sprite_frag1 = pygame.sprite.Group()
sprite_frag1.add(fragmento1)
sprite_frag2 = pygame.sprite.Group()
sprite_frag2.add(fragmento2)
sprite_frag3 = pygame.sprite.Group()
sprite_frag3.add(fragmento3)

quantidadedesejada = 0
personagem = personagens()
todas_sprites = pygame.sprite.Group()
todas_sprites.add(personagem)
moldura = 1*100
while True:
    vidaprabarra = personagem.vida *100
    vidamaxprabarra = (personagem.vida/personagem.vidamaxima) * 100
    tela.fill((0,0,0))
    perdi = False
    tela.fill((0, 0,0))
    mensagem = f'LP: {personagem.vida}'
    texto_formatado = fonte.render(mensagem, False, (255, 255,255))
    mensagem_fragmentos = f'Frags: {quantidade}'
    texto_formatado_fragmento = fonte.render(mensagem_fragmentos, False, (255, 255,255))
    for c in pygame.event.get():
        if c.type == QUIT:
            pygame.quit()
            exit()

    if quantidadedesejada == 3:
        vitoria = True
        while vitoria:
            i = 0
            while fimdejogo:
                textogameover = fonteover.render("RECEBA", True, (0, 100, 200))
                tela.fill((0, 0, 0))
                tela.blit(backgroundgameover, (i, 0))
                i += 1
                tela.blit(textogameover, (100, 200))
                luara.tick(60)
                pygame.display.update()
                for c in pygame.event.get():
                    if c.type == QUIT:
                        fimdejogo = False
                        vitoria = False
                        pygame.quit()
                        exit()
    if personagem.vidadesejada <= 0:
        perdi = True
    # Protagonista
    while perdi:
        i = 0
        while fimdejogo:
            textogameover = fonteover.render("RECEBA", True, (0, 100, 200))
            tela.fill((0,0,0))
            tela.blit(backgroundgameover, (i,0))
            i += 1
            tela.blit(textogameover, (100, 200))
            luara.tick(60)
            pygame.display.update()
            for c in pygame.event.get():
                if c.type == QUIT:
                    fimdejogo = False
                    perdi = False
                    pygame.quit()
                    exit()

    todas_sprites.draw(tela)
    personagem.update()
    # Desenhando o labirinto
    #barra de vida animada
    transicao = 0
    transicaocor = (255,0,0)
    if personagem.vida < personagem.vidadesejada:
        personagem.vida += personagem.velocidadedecaimento
        janela = int(((personagem.vidadesejada - personagem.vida)/(personagem.vidadesejada/personagem.vidamaxima)))
        janelacor = (0,255,0)
    if personagem.vida > personagem.vidadesejada:
        personagem.vida -= personagem.velocidadedecaimento
        if personagem.vida == 0 or personagem.vidadesejada == 0:
            personagem.vida = 0
        else: 
            janela = int(((personagem.vidadesejada - personagem.vida)/(personagem.vidadesejada/personagem.vidamaxima)))
            janelacor = (255, 255, 0)
    if quantidade < quantidadedesejada:
        quantidade += personagem.velocidadedecaimento
    barraanimada = pygame.Rect(10, 20, (personagem.vida/personagem.vidamaxima)*100, 5)
    transicaobarra = pygame.Rect(barraanimada.right, 20, janela, 5)
    pygame.draw.rect(tela, (255,0,0) , barraanimada)
    pygame.draw.rect(tela, janelacor , transicaobarra)
    molduraemsi = pygame.draw.rect(tela, (255, 255, 255), (10, 20, 100, 5), 1)
    fragmentoanimado = pygame.Rect(10, 30, (quantidade/3)*100, 5)
    transicaofrag = pygame.Rect(fragmentoanimado.right, 45, janela, 5)
    pygame.draw.rect(tela, (0, 255, 255), fragmentoanimado)
    pygame.draw.rect(tela, (0,255,255), transicaobarra)
    moldurafragmento = pygame.draw.rect(tela, (255, 255, 255), (10, 30, 100, 5), 1)
    lista_linhas = []
    linha_1 = pygame.draw.line(tela, (255, 0,0), (0,0), (600,0), 10) 
    lista_linhas.append(linha_1)
    linha_2 = pygame.draw.line(tela, (255, 0,0), (600,0 ), (600, 530), 10)
    lista_linhas.append(linha_2)
    linha_3 = pygame.draw.line(tela, (255, 0,0), (0, 600), (600, 600), 10)
    lista_linhas.append(linha_3)
    linha_4 = pygame.draw.line(tela, (255, 0,0), (0, 70), (0, 600), 10)
    lista_linhas.append(linha_4)
    linha_5 = pygame.draw.line(tela, (255, 0,0), (0, 70), (100, 70), 5)
    lista_linhas.append(linha_5)
    linha_6 = pygame.draw.line(tela, (255, 0,0), (100, 70), (100, 140), 5)
    lista_linhas.append(linha_6)
    linha_7 = pygame.draw.line(tela, (255, 0,0), (100, 140), (150, 140), 5)
    lista_linhas.append(linha_7)
    linha_8 = pygame.draw.line(tela, (255, 0,0), (150, 140), (150, 70), 5)
    lista_linhas.append(linha_8)
    linha_9 = pygame.draw.line(tela, (255, 0,0), (150, 70), (350, 70), 5)
    lista_linhas.append(linha_9)
    linha_10 = pygame.draw.line(tela, (255, 0,0), (450, 0), (450, 70), 5)
    lista_linhas.append(linha_10)
    linha_11 = pygame.draw.line(tela, (255, 0,0), (450, 70), (530, 70), 5)
    lista_linhas.append(linha_11)
    linha_12 = pygame.draw.line(tela, (255, 0,0), (530, 70), (530, 140), 5)
    lista_linhas.append(linha_12)
    linha_13 = pygame.draw.line(tela, (255, 0,0), (225, 140), (530, 140), 5)
    lista_linhas.append(linha_13)
    linha_14 = pygame.draw.line(tela, (255, 0,0), (100, 210), (100, 340), 5)
    lista_linhas.append(linha_14)
    linha_15 = pygame.draw.line(tela, (255, 0,0), (100, 340), (150, 340), 5)
    lista_linhas.append(linha_15)
    linha_16 = pygame.draw.line(tela, (255, 0,0), (150, 210), (150, 340), 5)
    lista_linhas.append(linha_16)
    linha_17 = pygame.draw.line(tela, (255, 0,0), (150, 340), (410, 340), 5)
    lista_linhas.append(linha_17)
    linha_18 = pygame.draw.line(tela, (255, 0,0), (410, 340), (410, 460), 5)
    lista_linhas.append(linha_18)
    linha_19 = pygame.draw.line(tela, (255, 0,0), (225, 140), (225, 280), 5)
    lista_linhas.append(linha_19)
    linha_20 = pygame.draw.line(tela, (255, 0,0), (225, 280), (480, 280), 5)
    lista_linhas.append(linha_20)
    linha_21 = pygame.draw.line(tela, (255, 0,0), (295, 210), (480, 210), 5)
    lista_linhas.append(linha_21)
    linha_22 = pygame.draw.line(tela, (255, 0,0), (480, 210), (480, 280), 5)
    lista_linhas.append(linha_22)
    linha_23 = pygame.draw.line(tela, (255, 0,0), (480, 280), (480, 530), 5)
    lista_linhas.append(linha_23)
    linha_24 = pygame.draw.line(tela, (255, 0,0), (480, 530), (550, 530), 5)
    lista_linhas.append(linha_24)
    linha_25 = pygame.draw.line(tela, (255, 0,0), (550, 340), (550, 530), 5)
    lista_linhas.append(linha_25)
    linha_26 = pygame.draw.line(tela, (255, 0,0), (100, 340), (100, 460), 5)
    lista_linhas.append(linha_26)
    linha_27 = pygame.draw.line(tela, (255, 0,0), (100, 460), (295, 460), 5)
    lista_linhas.append(linha_27)
    linha_28 = pygame.draw.line(tela, (255, 0,0), (295, 460), (295, 530), 5)
    lista_linhas.append(linha_28)
    linha_29 = pygame.draw.line(tela, (255, 0,0), (295, 530), (410, 530), 5)
    lista_linhas.append(linha_29)
    linha_30 = pygame.draw.line(tela, (255, 0,0), (410, 530), (410, 600), 5)
    lista_linhas.append(linha_30)
    linha_31 = pygame.draw.line(tela, (255, 0,0), (100, 530), (100, 600), 5)
    lista_linhas.append(linha_31)
    linha_32 = pygame.draw.line(tela, (255, 0,0), (100, 530), (225, 530), 5)
    lista_linhas.append(linha_32)
    linha_33 = pygame.draw.line(tela, (255, 0,0), (530, 140), (530, 280), 5)
    lista_linhas.append(linha_33)
    linha_34 = pygame.draw.line(tela, (255, 0,0), (0, 0), (0, 70), 10)
    lista_linhas.append(linha_34)
    

    def colidiu():
        for c in lista_linhas:
            if personagem.rect.colliderect(c):
                return True
                
        else:
            return False
    # Desenhando itens
    if desenhar_armadilha_1 == True:
        sprite_armadilha1.draw(tela)
        armadilha_1 = armadilha1.rect

    if desenhar_armadilha_2 == True:
        sprite_armadilha2.draw(tela)
        armadilha_2 = armadilha2.rect

    if desenhar_armadilha_3 == True:
        sprite_armadilha3.draw(tela)
        armadilha_3 = armadilha3.rect
        
    if desenhar_armadilha_4 == True:
        sprite_armadilha4.draw(tela)
        armadilha_4 = armadilha4.rect

    if desenhar_armadilha_5 == True:
        sprite_armadilha5.draw(tela)
        armadilha_5 = armadilha5.rect

    if desenhar_pocao_1 == True:
        sprite_pocao1.draw(tela)
        pocao_1 = pocao1.rect

    if desenhar_pocao_2 == True:
        sprite_pocao2.draw(tela)
        pocao_2 = pocao2.rect

    if desenhar_pocao_3 == True:
        sprite_pocao3.draw(tela)
        pocao_3 = pocao3.rect

    if desenhar_pocao_especial == True:
        sprite_super_pocao.draw(tela)
        pocao_especial = pocaoespecial.rect

    if desenhar_fragmento_1 == True:
        sprite_frag1.draw(tela)
        fragmento_1 = fragmento1.rect

    if desenhar_fragmento_2 == True:
        sprite_frag2.draw(tela)
        fragmento_2 = fragmento2.rect

    if desenhar_fragmento_3 == True:
        sprite_frag3.draw(tela)
        fragmento_3 = fragmento3.rect

    # Movimentação
    

    # colidir com itens
    if desenhar_armadilha_1 == True:
        if personagem.rect.colliderect(armadilha_1):
            personagem.vidadesejada -= armadilha1.dano
            desenhar_armadilha_1 = False
    if desenhar_armadilha_2 == True:
        if personagem.rect.colliderect(armadilha_2):
            personagem.vidadesejada -= armadilha2.dano
            desenhar_armadilha_2 = False
    if desenhar_armadilha_3 == True:
        if personagem.rect.colliderect(armadilha_3):
            personagem.vidadesejada -= armadilha3.dano
            desenhar_armadilha_3 = False
    if desenhar_armadilha_4 == True:
        if personagem.rect.colliderect(armadilha_4):
            personagem.vidadesejada -= armadilha4.dano
            desenhar_armadilha_4 = False
    if desenhar_armadilha_5 == True:
        if personagem.rect.colliderect(armadilha_5):
            personagem.vidadesejada -= armadilha5.dano
            desenhar_armadilha_5 = False
    if desenhar_pocao_1 == True:
        if personagem.rect.colliderect(pocao_1):
            if personagem.vidadesejada < 3:
                personagem.vidadesejada += pocao1.recuperar
            desenhar_pocao_1 = False
    if desenhar_pocao_2 == True:
        if personagem.rect.colliderect(pocao_2):
            if personagem.vidadesejada < 3:
                personagem.vidadesejada += pocao2.recuperar
            desenhar_pocao_2 = False
    if desenhar_pocao_3 == True:
        if personagem.rect.colliderect(pocao_3):
            if personagem.vidadesejada < 3:
                personagem.vidadesejada += pocao3.recuperar
            desenhar_pocao_3 = False
    if desenhar_pocao_especial == True:
        if personagem.rect.colliderect(pocao_especial):
            personagem.vidadesejada = pocaoespecial.nova_vida
            desenhar_pocao_especial = False
    if desenhar_fragmento_1 == True:
        if personagem.rect.colliderect(fragmento_1):
            quantidadedesejada += 1
            desenhar_fragmento_1 = False
    if desenhar_fragmento_2 == True:
        if personagem.rect.colliderect(fragmento_2):
            quantidadedesejada += 1
            desenhar_fragmento_2 = False
    if desenhar_fragmento_3 == True:
        if personagem.rect.colliderect(fragmento_3):
            quantidadedesejada += 1
            desenhar_fragmento_3 = False
    
    teste = colidiu()
    if teste == True:
        personagem.voltar_inicio()



    #tela.blit(texto_formatado, (450, 40))
    #tela.blit(texto_formatado_fragmento, (50, 40))
    pygame.display.update()