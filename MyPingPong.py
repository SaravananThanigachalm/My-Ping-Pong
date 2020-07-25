import pygame, time

pygame.init()

screenWidth = 800
screenHeight = 600
screen = pygame.display.set_mode((screenWidth,screenHeight))
pygame.display.set_caption("My Ping Pong")
clock = pygame.time.Clock()

WHITE = (255,255,255)
BLACK = (0,0,0)
#Screen Dimensions
screenWidth = 800
screenHeight = 600
#Defining Bar
x1 = screenWidth/2
y1 = screenHeight - 50
x2 = screenWidth/2
y2 =  30
#Bar Dimensions
w = 150
h = 20
vel = 10
#Defining Ball
ballX = screenWidth/2
ballY = screenHeight/2
ballW = 20
ballH = 20
#Ball movement
ballVel = 5
balldx = ballVel
balldy = ballVel
#Scores
ScoresP1 = 0
ScoresP2 = 0

def Ball(ballX, ballY, ballW, ballH):
    pygame.draw.rect(screen, WHITE, (ballX, ballY , ballW, ballH))
    
def Bar(x, y, w, h):
    pygame.draw.rect(screen, WHITE, (x, y, w, h))

def text_objects(text, font, color):
    textSurface = font.render(text, True, color)
    return textSurface, textSurface.get_rect()

def GameIntro():
    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        screen.fill(BLACK)
        text1 = pygame.font.SysFont("Roboto",32)
        TextSurf, TextRect = text_objects("My Ping Pong V1", text1, WHITE)
        TextRect.center = ((screenWidth/2, screenHeight/2 - 50))
        screen.blit(TextSurf,TextRect)
        text2 = pygame.font.SysFont("Arial",22)
        TextSurf, TextRect = text_objects("By Saravanan T", text2, WHITE)
        TextRect.center = ((screenWidth/2, screenHeight/2))
        screen.blit(TextSurf,TextRect)

        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        text3 = pygame.font.SysFont("Poppins",18)
        text4 = pygame.font.SysFont("Poppins",18)
        text5 = pygame.font.SysFont("Poppins",18)

        if 150+130 > mouse[0] > 150 and 400+50 > mouse[1] > 400:
            pygame.draw.rect(screen, BLACK, (150, 400, 130, 50))
            TextSurf, TextRect = text_objects("1 Player", text3, WHITE)
            TextRect.center = ((210, 425))
            screen.blit(TextSurf,TextRect)
            if click[0] == 1:
                GameLoop1P()
        else:
            pygame.draw.rect(screen, WHITE, (150, 400, 130, 50))
            TextSurf, TextRect = text_objects("1 Player", text3, BLACK)
            TextRect.center = ((210, 425))
            screen.blit(TextSurf,TextRect)
        
        if 350+130 > mouse[0] > 350 and 400+50 > mouse[1] > 400:
            pygame.draw.rect(screen, BLACK, (350, 400, 130, 50))
            TextSurf, TextRect = text_objects("2 Player", text4, WHITE)
            TextRect.center = ((410, 425))
            screen.blit(TextSurf,TextRect)
            if click[0] == 1:
                GameLoop2P()
        else:
            pygame.draw.rect(screen, WHITE, (350, 400, 130, 50))
            TextSurf, TextRect = text_objects("2 Player", text4, BLACK)
            TextRect.center = ((410, 425))
            screen.blit(TextSurf,TextRect)

        if 550+130 > mouse[0] > 550 and 400+50 > mouse[1] > 400:
            pygame.draw.rect(screen, BLACK, (550, 400, 130, 50))
            TextSurf, TextRect = text_objects("How To", text5, WHITE)
            TextRect.center = ((610, 425))
            screen.blit(TextSurf,TextRect)
            if click[0] == 1:
                HowTo()
        else:
            pygame.draw.rect(screen, WHITE, (550, 400, 130, 50))
            TextSurf, TextRect = text_objects("How To", text5, BLACK)
            TextRect.center = ((610, 425))
            screen.blit(TextSurf,TextRect)

        pygame.display.update()
        clock.tick(45)

def HowTo():
    info = True
    while info:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        screen.fill(BLACK)
        text1 = pygame.font.SysFont("Roboto",36)
        TextSurf, TextRect = text_objects("Thanks for Playing my Game", text1, WHITE)
        TextRect.center = ((screenWidth/2, screenHeight/2 - 250))
        screen.blit(TextSurf,TextRect)
        text2 = pygame.font.SysFont("Arial",28)
        TextSurf, TextRect = text_objects("Instructions", text2, WHITE)
        TextRect.center = ((screenWidth/2, screenHeight/2 - 200))
        screen.blit(TextSurf,TextRect)
        text3 = pygame.font.SysFont("Arial",26)
        TextSurf, TextRect = text_objects("Player 1 controls:", text3, WHITE)
        TextRect.center = ((100, 200))
        screen.blit(TextSurf,TextRect)
        text4 = pygame.font.SysFont("Arial",22)
        TextSurf, TextRect = text_objects("Left Arrow moves the Bar Left", text4, WHITE)
        TextRect.center = ((140, 230))
        screen.blit(TextSurf,TextRect)
        TextSurf, TextRect = text_objects("Right Arrow moves the Bar Right", text4, WHITE)
        TextRect.center = ((150, 260))
        screen.blit(TextSurf,TextRect)

        TextSurf, TextRect = text_objects("Player 2 controls:", text3, WHITE)
        TextRect.center = ((100, 300))
        screen.blit(TextSurf,TextRect)
        TextSurf, TextRect = text_objects("Left ALT moves the Bar Left", text4, WHITE)
        TextRect.center = ((130, 330))
        screen.blit(TextSurf,TextRect)
        TextSurf, TextRect = text_objects("Right CTRL moves the Bar Right", text4, WHITE)
        TextRect.center = ((150, 360))
        screen.blit(TextSurf,TextRect)

        TextSurf, TextRect = text_objects("Scoring:", text3, WHITE)
        TextRect.center = ((50, 410))
        screen.blit(TextSurf,TextRect)
        TextSurf, TextRect = text_objects("When the Player manage to hit the Bar,", text4, WHITE)
        TextRect.center = ((200, 440))
        screen.blit(TextSurf,TextRect)
        TextSurf, TextRect = text_objects("Ponits will be added to the Player, ", text4, WHITE)
        TextRect.center = ((200, 470))
        screen.blit(TextSurf,TextRect)
        TextSurf, TextRect = text_objects("But in the end Playing matters than Winning,", text4, WHITE)
        TextRect.center = ((200, 500))
        screen.blit(TextSurf,TextRect)
        TextSurf, TextRect = text_objects(" So all Players are Winners ", text4, WHITE)
        TextRect.center = ((200, 530))
        screen.blit(TextSurf,TextRect)

        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        text8 = pygame.font.SysFont("Poppins",18)
        if 510+130 > mouse[0] > 510 and 500+50 > mouse[1] > 500:
            pygame.draw.rect(screen, BLACK, (510, 500, 130, 50))
            TextSurf, TextRect = text_objects("Play", text8, WHITE)
            TextRect.center = ((570, 525))
            screen.blit(TextSurf,TextRect)
            if click[0] == 1:
                GameIntro()
        else:
            pygame.draw.rect(screen, WHITE, (510, 500, 130, 50))
            TextSurf, TextRect = text_objects("Play", text8, BLACK)
            TextRect.center = ((570, 525))
            screen.blit(TextSurf,TextRect)

        pygame.display.update()
        clock.tick(45)

def GameOver():
    global screenWidth, screenHeight, ScoresP1, ScoresP2, BLACK, WHITE
    Over = True
    Scores1 = ScoresP1
    Scores2 = ScoresP2
    while Over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        screen.fill(BLACK)
        text6 = pygame.font.SysFont("Roboto",48)
        TextSurf, TextRect = text_objects("Game Over !!!", text6, WHITE)
        TextRect.center = ((int(screenWidth/2) + 20, int(screenHeight/2 - 120)))
        screen.blit(TextSurf,TextRect)

        if Scores2 != -1:
            text7 = pygame.font.SysFont("Arial",26)
            TextSurf, TextRect = text_objects("Player 1 Score = " + str(Scores1) , text7, WHITE)
            TextRect.center = ((int(screenWidth/2 - 50), int(screenHeight/2)))
            screen.blit(TextSurf,TextRect)

            TextSurf, TextRect = text_objects("Player 2 Score = " + str(Scores2) , text7, WHITE)
            TextRect.center = ((int(screenWidth/2 - 50), int(screenHeight/2 + 50)))
            screen.blit(TextSurf,TextRect)
        else:
            text7 = pygame.font.SysFont("Arial",26)
            TextSurf, TextRect = text_objects("Player Score = " + str(Scores1) , text7, WHITE)
            TextRect.center = ((screenWidth/2, screenHeight/2))
            screen.blit(TextSurf,TextRect)

        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        text8 = pygame.font.SysFont("Poppins",18)

        if 400+130 > mouse[0] > 400 and 500+50 > mouse[1] > 500:
            pygame.draw.rect(screen, BLACK, (400, 500, 130, 50))
            TextSurf, TextRect = text_objects("Play Again ?", text8, WHITE)
            TextRect.center = ((470, 525))
            screen.blit(TextSurf,TextRect)
            if click[0] == 1:
                GameIntro()
                ScoresP1 = 0
                ScoresP2 = 0
        else:
            pygame.draw.rect(screen, WHITE, (400, 500, 130, 50))
            TextSurf, TextRect = text_objects("Play Again ?", text8, BLACK)
            TextRect.center = ((470, 525))
            screen.blit(TextSurf,TextRect)
        
        pygame.display.update()
        clock.tick(45)

def GameLoop1P():
    global screenWidth, screenHeight, x1, x2, y1, y2, w, h, vel, ballX, balldx, ballY, balldy, ballH, ballW, ballVel, ScoresP1, ScoresP2, Over
    ScoresP2 = -1
    ScoresP1 = 0
    run = True
    while run:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    pygame.quit()
                    quit()

        screen.fill(BLACK)

        #Ball Logic
        ballX += balldx
        ballY += balldy
        if ballX < ballVel:
            balldx *= -1
        elif ballX > screenWidth - ballW - ballVel:
            balldx *=-1
        elif ballY > screenHeight - ballH - ballVel:
            ballY = screenHeight/2
            ballX = screenWidth/2
            balldy *=-1
            GameOver()
            run = False
        elif ballY < 0:
            ballY = screenHeight/2
            ballX = screenWidth/2
            balldy *=-1
        elif (ballX > x1 and ballX < x1 + w and ballY == y1 - ballVel):
            balldy *=-1
            ScoresP1 += 1
        elif (ballX > x2 and ballX < x2 + w and ballY == y2 + ballVel):
            balldy *=-1 

        #Comp Autoplay
        if ballX >= vel + w/2 and ballX <= screenWidth - w/2 - vel:
            x2 = ballX - w/2
        #Player 1
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT] and x1 > vel:
            x1 -= vel
        if keys[pygame.K_RIGHT] and x1 < screenWidth - w - vel:
            x1 += vel

        Ball(ballX, ballY, ballW, ballH)
        Bar(x1, y1, w, h)
        Bar(x2, y2, w, h)
    
        pygame.display.update()         
        clock.tick(60)
    
def GameLoop2P():
    global screenWidth, screenHeight, x1, x2, y1, y2, w, h, vel, ballX, balldx, ballY, balldy, ballH, ballW, ballVel, ScoresP1, ScoresP2, Over
    ScoresP1 = 0
    ScoresP2 = 0
    run = True
    while run:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    pygame.quit()
        screen.fill(BLACK)
        
        #Ball Logic
        ballX += balldx
        ballY += balldy
        if ballX < ballVel:
            balldx *= -1
        elif ballX > screenWidth - ballW - ballVel:
            balldx *=-1
        elif ballY > screenHeight - ballH - ballVel:
            ballY = screenHeight/2
            ballX = screenWidth/2
            balldy *=-1
            GameOver()
            run = False
        elif ballY < 0:
            ballY = screenHeight/2
            ballX = screenWidth/2
            balldy *=-1
            GameOver()
            run = False
        elif (ballX > x1 and ballX < x1 + w and ballY == y1 - ballVel):
            balldy *=-1
            ScoresP1 += 1
        elif (ballX > x2 and ballX < x2 + w and ballY == y2 + ballVel):
            balldy *=-1
            ScoresP2 += 1

        #Player 1
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and x1 > vel:
            x1 -= vel
        if keys[pygame.K_RIGHT] and x1 < screenWidth - w - vel:
            x1 += vel
        #Player 2
        if keys[pygame.K_LCTRL] and x2 > vel:
            x2 -= vel
        if keys[pygame.K_LALT] and x2 < screenWidth - w - vel:
            x2 += vel

        Ball(ballX, ballY, ballW, ballH)
        Bar(x1, y1, w, h)
        Bar(x2, y2, w, h)
    
        pygame.display.update()         
        clock.tick(60)

    pygame.quit()

GameIntro()