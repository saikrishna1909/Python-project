import pygame as pg
import sys
from pygame.locals import *
from pygame import mixer
import time,shelve

#initialize global variables

pg.init()
mixer.init()
XO = 'x'
user_name_1 =""
user_name_2  =""
winner = None
draw = False
width  = 600
height = 600

white = (255, 255, 255)
line_color = (10,10,10)
global list_1
global list_2
list_1 = []
list_2 = []
#font = pg.font.SysFont(None,20)
smallfont = pg.font.SysFont("comicsansms", 20)
minifont = pg.font.SysFont("comicsansms",15)
font = pg.font.SysFont("cambria",32)
#smallfont = pg.font.Font("comicsansms", 14)
slategrey = (112, 128, 144)
lightgrey = (165, 175, 185)
blackish = (10, 10, 10)
white = (255, 255, 255)
black = (0, 0, 0)
SAVE_DATA = shelve.open("Save Data")
SAVE_DATA1 = shelve.open("Save Data1")
#TicTacToe 3x3 board
TTT = [[None]*3,[None]*3,[None]*3]
#initializing pygame window
fps = 30
CLOCK = pg.time.Clock()
screen = pg.display.set_mode((width, height+100))
pg.display.set_caption("Tic Tac Toe")
#loading the images
opening = pg.image.load('tic tac opening.png')
x_img = pg.image.load('x.png')
o_img = pg.image.load('o.png')
#resizing images
flag = True
x_img = pg.transform.scale(x_img, (80,80))
o_img = pg.transform.scale(o_img, (80,80))
opening = pg.transform.scale(opening, (width, height+100))
#
music1 = mixer.music.load("Doctor.mp3")
mixer.music.play()
def tic_tac_toe():
    def create_button(x, y, width, height, hovercolor, defaultcolor):
        mouse = pg.mouse.get_pos()
        # Mouse get pressed can run without an integer, but needs a 3 or 5 to indicate how many buttons
        click = pg.mouse.get_pressed(3)
        if x + width > mouse[0] > x and y + height > mouse[1] > y:
            pg.draw.rect(screen, hovercolor, (x, y, width, height))
            if click[0] == 1:
                return True
        else:
            pg.draw.rect(screen, defaultcolor, (x, y, width, height))
    def users():
        player1_name = ""
        player2_name = ""
        heading = ""

        p1_prompt = smallfont.render("Enter player-1 name:",True,(0,255,0))
        p2_prompt = smallfont.render("Enter player-2 name:",True,(0,255,0))
        
        p1_active = False
        p2_active = False
        screen.fill((255,255,255))
        
        heading = font.render("USER DETAILS",1,(0,50,0))

        Enter = font.render("START THE GAME!",1,(75,0,130))
        
        while True:
            screen.fill((255,255,255))
            screen.blit(heading,((width-heading.get_width())/2,5))
            userNameSurface_1 = smallfont.render(player1_name, True,slategrey)
            userNameBorder_1 = pg.Rect((width - userNameSurface_1.get_width())/2-10 ,height*.50, userNameSurface_1.get_width() + 10, 50)
            screen.blit(userNameSurface_1,((width - userNameSurface_1.get_width())/2 , height*.50))
            
            userNameSurface_2 = smallfont.render(player2_name, True, slategrey)
            userNameBorder_2 = pg.Rect((width - userNameSurface_2.get_width())/2-10, height*.80, userNameSurface_2.get_width() + 10, 50)
            screen.blit(userNameSurface_2, ((width - userNameSurface_2.get_width()) / 2, height*.80))

            
           
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()

                # Mouse and Keyboard events
                if event.type == pg.MOUSEBUTTONDOWN:
                    if userNameBorder_1.collidepoint(event.pos):
                        p1_active = True
                        p2_active = False
                    elif userNameBorder_2.collidepoint(event.pos):
                        p2_active = True
                        p1_active = False
                    else:
                        p1_active = False
                        p2_active = False

                if event.type == pg.KEYDOWN:
                    if p1_active:
                        if event.key == pg.K_BACKSPACE:
                            player1_name = player1_name[:-1]
                        else:
                            player1_name += event.unicode
                    elif  p2_active:
                        if event.key == pg.K_BACKSPACE:
                            player2_name = player2_name[:-1]
                        else:
                            player2_name += event.unicode
                
            
           
            if p1_active:
                pg.draw.rect(screen, white, userNameBorder_1, 2)
                p1_prompt = smallfont.render("Enter player-1 name:", True, (0,0,100))
            else:
                pg.draw.rect(screen, slategrey, userNameBorder_1, 2)
                p1_prompt = smallfont.render("Enter player-1 name:", True, slategrey)
            if p2_active:
                pg.draw.rect(screen, white, userNameBorder_2, 2)
                p2_prompt = smallfont.render("Enter player-2 name:", True, (0,0,100))
            else:
                pg.draw.rect(screen, slategrey, userNameBorder_2, 2)
                p2_prompt = smallfont.render("Enter player-2 name:", True, slategrey)
            screen.blit(p1_prompt,((width - p1_prompt.get_width())/2-60, height*.40))
            screen.blit(p2_prompt,((width - p2_prompt.get_width())/2-60, height*.70))
            submitButton = create_button((width / 2) - (Enter.get_width() / 2) - 5, height ,Enter.get_width() + 10, Enter.get_height(), lightgrey, slategrey)

            screen.blit(Enter, ((width / 2) - (Enter.get_width() / 2), int(height )))
                
            if submitButton:  
                if player1_name != "":
                    userName_1 = player1_name
                    SAVE_DATA["user_name1"] = userName_1
                    SAVE_DATA1["user_name1"]=  userName_1
                else:
                    print("Need to program a user warning")
                    
                if player2_name != "":
                    userName_2 = player2_name
                    SAVE_DATA["user_name2"] = userName_2
                    SAVE_DATA1["user_name2"]= userName_2
                else:
                    print("Need to program a user warning")
                SAVE_DATA.close()
                SAVE_DATA1.close()
                break
           
            pg.display.update()
            CLOCK.tick(15)
                
        
    #
    def game_opening():
        screen.blit(opening,(0,0))
        pg.display.update()
        time.sleep(1)
        pg.FULLSCREEN
        while True:
            screen.fill(white)
            # Drawing vertical lines
            pg.draw.line(screen,line_color,(width/3,0),(width/3, height),7)
            pg.draw.line(screen,line_color,(width/3*2,0),(width/3*2, height),7)
            # Drawing horizontal lines
            pg.draw.line(screen,line_color,(0,height/3),(width, height/3),7)
            pg.draw.line(screen,line_color,(0,height/3*2),(width, height/3*2),7)
            
            draw_status()
            break
    #
    def result():
        mixer.music.load("applause.mp3")
        mixer.music.play()
        screen.fill((255,255,255))
        
        pg.display.update()
        global  list_1 
        global  list_2 
        list_1,player1_name,player2_name=draw_status()
        congrats = pg.image.load("Congrats.jpg")
        congrats = pg.transform.scale(congrats, (300,300))
        END_GAME = smallfont.render("GAME ENDED!",1,(255,255,255))
        a = list_1.count(player1_name)
        b = list_1.count(player2_name)
        if a >b:
             winner = player1_name
             winner = font.render(winner,1,(0,0,0))
             screen.blit(congrats,((width-congrats.get_width())/2,0))
             text = smallfont.render("for winning more number of games",1,(0,0,0))
             screen.blit(winner,((width-winner.get_width())/2,300+10))
             screen.blit(text,((width-text.get_width())/2,300+40))
             screen.blit(END_GAME, ((width / 2) - (END_GAME.get_width() / 2), 600+60))
             screen.fill ((0, 0, 0), (0, 600, 600, 100))
        elif b>a:
             winner = player2_name
             winner = font.render(winner,1,(0,0,0))
             screen.blit(congrats,((width-congrats.get_width())/2,0))
             text = smallfont.render("for winning more number of games",1,(0,0,0))
             screen.blit(winner,((width-winner.get_width())/2,300+10))
             screen.blit(text,((width-text.get_width())/2,300+40))
             screen.blit(END_GAME, ((width / 2) - (END_GAME.get_width() / 2), 600+60))
             screen.fill ((0, 0, 0), (0, 600, 600, 100))
        elif a==b:
       #     winner = font.render(winner,1,(0,0,0))
            screen.blit(congrats,((width-congrats.get_width())/2,0))
           # text = smallfont.render("for winning more number of games",1,(0,0,0))
            text1 = smallfont.render("Both won equal times",1,(0,0,0))
            screen.blit(text1,((width-text1.get_width())/2,300+10))
         #   screen.blit(text,((width-text.get_width())/2,300+40))
            screen.blit(END_GAME, ((width / 2) - (END_GAME.get_width() / 2), 600+60))
            screen.fill ((0, 0, 0), (0, 600, 600, 100))
        
       
        pg.display.update()
        time.sleep(10)
        pg.quit()
        sys.exit()
        
    def end_game():
        message = smallfont.render("Do you want to end game?",1,(0,0,0))
        yes = smallfont.render("YES",1,(255,0,0))
        no = smallfont.render("NO",1,(0,255,0))
        while True:
            screen.fill((255,255,255))
            screen.blit(message,((width-message.get_width())/2,100))
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()
            submitButton1 = create_button((width / 2) - (yes.get_width() / 2) - 5, 250,yes.get_width() + 10, yes.get_height(), lightgrey, slategrey)
            submitButton2 = create_button((width / 2) - (no.get_width() / 2) - 5, 250+55 ,no.get_width() + 10, no.get_height(), lightgrey, slategrey)

            screen.blit(yes, ((width / 2) - (yes.get_width() / 2), 250))
            screen.blit(no, ((width / 2) - (no.get_width() / 2),250+55))
            global i
            if submitButton1:
                if i:
                    result()
                else:
                    pg.quit()
                    sys.exit()
            if submitButton2:
                break
            
            pg.display.update()
        reset_game()
            
    def draw_status():
        global draw
        SAVE_DATA = shelve.open("Save Data")
        try:
            player1_name = SAVE_DATA['user_name1']
            player2_name = SAVE_DATA['user_name2']
            
        except KeyError:
            player1_name = "No  player1 name Saved"
            player2_name = "No player2 name Saved"
        SAVE_DATA.close()
        SAVE_DATA1 = shelve.open("Save Data1")
        try:
            user1_name = SAVE_DATA1['user_name1']
            user2_name = SAVE_DATA1['user_name2']
            
        except KeyError:
            user1_name = "No  player1 name Saved"
            user2_name = "No player2 name Saved"
        SAVE_DATA1.close()
        
        score = smallfont.render("Score:",1,(255,255,255))
        p1 = minifont.render(user1_name+":"+str(list_1.count(user1_name)),1,(255,255,255))
        p2 = minifont.render(user2_name+":"+str(list_1.count(user2_name)),1,(255,255,255))
        p3 = minifont.render("drawn:"+str(len(list_2)),1,(255,255,255))
        p1_name = smallfont.render(player1_name+": X",1,(255,255,255))
        p2_name = smallfont.render(player2_name+": O",1,(255,255,255))
        
        continues = smallfont.render("END THE GAME!",1,(0,0,255))
        if winner is None:
             if XO.upper() == 'X':
                message = player1_name +"'s Turn"
             else:
                message = player2_name +"'s Turn"
            
        else:
           # message = winner.upper() + " won!"
            if winner.upper() == 'X':
                message = player1_name +"'won"
                list_1.append(player1_name)
                SAVE_DATA = shelve.open("Save Data")
                name1 = SAVE_DATA['user_name1']
                name2 = SAVE_DATA['user_name2']
                SAVE_DATA['user_name1']  =" "
                SAVE_DATA['user_name2'] = " "
                SAVE_DATA['user_name1']  =name2
                SAVE_DATA['user_name2'] = name1
                SAVE_DATA.close()
                
            else:
                 message = player2_name +"'won"
                 list_1.append(player2_name)
                 SAVE_DATA = shelve.open("Save Data")
                 name1 = SAVE_DATA['user_name1']
                 name2 = SAVE_DATA['user_name2']
                 SAVE_DATA['user_name1']  =" "
                 SAVE_DATA['user_name2'] = " "
                 SAVE_DATA['user_name1']  =name2
                 SAVE_DATA['user_name2'] = name1
                 SAVE_DATA.close()
                 
                 
        if draw:
            message = 'Game Draw!'

            SAVE_DATA = shelve.open("Save Data")
            name1 = SAVE_DATA['user_name1']
            name2 = SAVE_DATA['user_name2']
            SAVE_DATA['user_name1']  =" "
            SAVE_DATA['user_name2'] = " "
            SAVE_DATA['user_name1']  =name2
            SAVE_DATA['user_name2'] = name1
            SAVE_DATA.close()
        while True:    
            font = pg.font.Font(None, 30)
            text = font.render(message, 1, (255, 255, 255))
        # copy the rendered message onto the board
            screen.fill ((0, 0, 0), (0, 600, 600, 100))
            text_rect = text.get_rect(center=(width/2, 600+50))
            screen.blit(text, text_rect)
            screen.blit(p1_name,(0,600+20))
            screen.blit(p2_name,(0,600+50))
            screen.blit(score,(400,600+10))
            screen.blit(p1,(450,600+30))
            screen.blit(p2,(450,600+60))
            #screen.blit(p3,(400,600+90))
        
           
            pg.display.update()
            break
                   
        return list_1,player1_name,player2_name      
    #
    def check_win():
        global TTT, winner,draw
        # check for winning rows
        for row in range (0,3):
            if ((TTT [row][0] == TTT[row][1] == TTT[row][2]) and(TTT [row][0] is not None)):
                # this row won
                winner = TTT[row][0]
                pg.draw.line(screen, (250,0,0), (0, (row + 1)*height/3 -height/6),\
                             (width, (row + 1)*height/3 - height/6 ), 4)
                
                break
        # check for winning columns
        for col in range(0, 3):
            if (TTT[0][col] == TTT[1][col] == TTT[2][col]) and (TTT[0][col] is not None):
                # this column won
                winner = TTT[0][col]
                #draw winning line
                pg.draw.line (screen, (250,0,0),((col + 1)* width/3 - width/6, 0),\
                              ((col + 1)* width/3 - width/6, height), 4)
                
                break
        # check for diagonal winners
        if (TTT[0][0] == TTT[1][1] == TTT[2][2]) and (TTT[0][0] is not None):
            # game won diagonally left to right
            winner = TTT[0][0]
            pg.draw.line (screen, (250,70,70), (50, 50), (550, 550), 4)
            
        if (TTT[0][2] == TTT[1][1] == TTT[2][0]) and (TTT[0][2] is not None):
            # game won diagonally right to left
            winner = TTT[0][2]
            pg.draw.line(screen, (250,70,70), (550, 50), (50, 550), 4)
            
        if(all([all(row) for row in TTT]) and winner is None ):
            draw = True
        
        draw_status()
    #
    def drawXO(row,col):
        global TTT,XO
        if row==1:
            posx = 30
        if row==2:
            posx = width/3 + 30
        if row==3:
            posx = width/3*2 + 30
        if col==1:
            posy = 30
        if col==2:
            posy = height/3 + 30
        if col==3:
            posy = height/3*2 + 30
        TTT[row-1][col-1] = XO
        if(XO == 'x'):
            screen.blit(x_img,(posy,posx))
            XO= 'o'
        else:
            screen.blit(o_img,(posy,posx))
            XO= 'x'
        pg.display.update()
        #print(posx,posy)
        #print(TTT)
    #
    def userClick():
        #get coordinates of mouse click
        x,y = pg.mouse.get_pos()
        #get column of mouse click (1-3)
        if(x<width/3):
            col = 1
        elif (x<width/3*2):
            col = 2
        elif(x<width):
            col = 3
        else:
            col = None
        #get row of mouse click (1-3)
        if(y<height/3):
            row = 1
        elif (y<height/3*2):
            row = 2
        elif(y<height):
            row = 3
        else:
            row = None
        #print(row,col)
        if(row and col and TTT[row-1][col-1] is None):
            global XO
            
            #draw the x or o on screen
            drawXO(row,col)
            check_win()
    #
    global i
    i = 0
    def reset_game():
        global TTT, winner,XO, draw
        global i
        time.sleep(3)
        XO = 'x'
        draw = False
        winner=None
        game_opening()
        i=  i+1
        TTT = [[None]*3,[None]*3,[None]*3]
        return i
    #
    screen.blit(opening,(0,0))
    pg.display.update()
    time.sleep(1)
    #mixer.music.play()
    users()
    pg.display.update()
    game_opening()

    # run the game loop forever
    
    while(True):
        for event in pg.event.get():
            if event.type == QUIT:
                end_game()
                pg.quit()
                sys.exit()
            elif event.type == MOUSEBUTTONDOWN:
                # the user clicked; place an X or O
                userClick()
                if(winner or draw):
                    reset_game()
        pg.display.update()
        CLOCK.tick(fps)
tic_tac_toe()

