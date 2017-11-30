#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 26 11:51:11 2016

@author: Kevin Desousa
"""

import pygame
import random

  
class square:
    def __init__(self, width, height, location, speedx, speedy, color):
        #Initialize the square's variables such as height, width, color,etc.
        self.width = width
        self.height = height
        self.speedx = speedx
        self.speedy = speedy
        self.location = location
        self.color = color
        
        #Call setRect() to create the rectangle with the info
        self.setRect()

    def setRect(self):
        self.rect = pygame.Rect(self.location[0], self.location[1], self.height, self.width)
    
    def moveRect(self, x ,y):
        #Move the rectangle with a certain x and y velocity
        self.rect = self.rect.move(x,y)
        
class text:
    def __init__(self,location,font,words):
        self.location = location
        self.words = words
        self.desiredfont = font
    
        self.setText(words)
        self.location[0] -= self.width / 2
        
    def setText(self,words):
        self.font = pygame.font.Font(self.desiredfont, 60)
        self.width, self.height = self.font.size(words)
        self.object = self.font.render((words), 1, (255, 255, 255))
        self.words = words
        self.rect = self.object.get_rect()
        
def draw():
    #Fill the blank space with the color black. If not used, things will look all weird
    color = 0,0,0
    screen.fill(color)
    
    
    #Loop through the objects that stand off the background and add them to the display
    for x in nonBackground_Squares:
        pygame.draw.rect(screen, x.color, x.rect, 0)
        
    for x in nonBackground_Text:
        screen.blit(x.object, x.location)
    pygame.display.flip()
   
def detectKeys():
    #This gets an array of all the key presses
    pressed = pygame.key.get_pressed()
  
    #Check what key is pressed, then do something based on that key.
    if pressed[pygame.K_w]:
        move_up = True
        movePaddle(move_up, nonBackground_Squares[0])
    if pressed[pygame.K_s]:
        move_up = False
        movePaddle(move_up, nonBackground_Squares[0])
    if pressed[pygame.K_i]:
        move_up = True
        movePaddle(move_up, nonBackground_Squares[1])
    if pressed[pygame.K_k]:
        move_up = False
        movePaddle(move_up, nonBackground_Squares[1])
    if pressed[pygame.K_x]:
        nonBackground_Squares[len(nonBackground_Squares) -1].speedx \
        = random.randrange(-9,9)
        nonBackground_Squares[len(nonBackground_Squares) -1].speedy \
        = random.randrange(-9,9)
    if pressed[pygame.K_z]:
        nonBackground_Squares[len(nonBackground_Squares) -1].location[0] \
        = dimensions[0]/2
        nonBackground_Squares[len(nonBackground_Squares) -1].location[1] \
        = dimensions[1]/2
        nonBackground_Squares[len(nonBackground_Squares) -1].setRect()
     
    
    #Exit game if user hits the escape key   
    if pressed[pygame.K_ESCAPE]:
        pygame.quit()
        
    #Call the draw function to draw the change in position            
    for event in pygame.event.get():
        draw()
   
   

         
def movePaddle(upordown, sqr_object):
    #If wanting to move up, check if the paddle location isnt at the top
    if(upordown == True and not sqr_object.rect.top <= 0):
        sqr_object.moveRect(0, -(sqr_object.speedy))
           
    #If wanting to move down, check if paddle location isnt at the bottom      
    elif(upordown == False and not sqr_object.rect.bottom >= dimensions[1]):
        sqr_object.moveRect(0, (sqr_object.speedy))
    
def moveBall():    
    #Change the balls loation based on its speed
    nonBackground_Squares[len(nonBackground_Squares) - 1].moveRect\
    ((nonBackground_Squares[len(nonBackground_Squares) - 1].speedx),\
    (nonBackground_Squares[len(nonBackground_Squares) - 1].speedy))
         
    #Check if the ball hits an object:

    if(nonBackground_Squares[len(nonBackground_Squares) - 1].rect.y <= 0):
        nonBackground_Squares[len(nonBackground_Squares) - 1].speedy = \
        -1 * nonBackground_Squares[len(nonBackground_Squares) - 1].speedy
    elif(nonBackground_Squares[len(nonBackground_Squares) - 1].rect.y >= dimensions[1]):
        nonBackground_Squares[len(nonBackground_Squares) - 1].speedy = \
        -1 * nonBackground_Squares[len(nonBackground_Squares) - 1].speedy

    if(nonBackground_Squares[len(nonBackground_Squares) - 1].rect.colliderect\
        (nonBackground_Squares[0].rect)):
        nonBackground_Squares[len(nonBackground_Squares) - 1].speedx = \
        -1 * nonBackground_Squares[len(nonBackground_Squares) - 1].speedx
    elif(nonBackground_Squares[len(nonBackground_Squares) - 1].rect.x <= 0):
        nonBackground_Squares[len(nonBackground_Squares) - 1].speedx = \
        -1 * nonBackground_Squares[len(nonBackground_Squares) - 1].speedx
        #Return a value to indicate that a wall was hit
        return 1
         
    if(nonBackground_Squares[len(nonBackground_Squares) - 1].rect.colliderect\
        (nonBackground_Squares[1].rect)):
        nonBackground_Squares[len(nonBackground_Squares) - 1].speedx = \
        -1 * nonBackground_Squares[len(nonBackground_Squares) - 1].speedx
    elif(nonBackground_Squares[len(nonBackground_Squares) - 1].rect.x >= dimensions[0]):
        nonBackground_Squares[len(nonBackground_Squares) - 1].speedx = -1 * nonBackground_Squares[len(nonBackground_Squares) - 1].speedx
        #Return a value to indicate that a wall was hit
        return 2
         
         
def initlize():
    pygame.init()
    #Initilize the screen size variables
    global dimensions
    dimensions = [800, 400]
    size = width, height = dimensions
    
    #Create a global variable for the screen and initilize it
    global screen 
    screen = pygame.display.set_mode(size)

    #Set window caption
    pygame.display.set_caption("PONG")
    #Set window icon
    pygame.display.set_icon(pygame.image.load("icon.jpg"))    

    global scoreP1
    global scoreP2
    scoreP1 = 0
    scoreP2 = 0
    
    #Create the paddle1, paddle2 ,ball, and text
    paddle = square(50,10,[0, 0], 5, 5, (255,255,255))
    
    paddle2 = square(50,10,[dimensions[0] - 10,0], 5, 5, (255,255,255))
        
    ball_square = square(10,10,[dimensions[0]/2, dimensions[1]/2], random.randrange(-5,5), random.randrange(-5,5),(255,255,255))
    
    score_display = text([dimensions[0]/2, 0], None, (str(scoreP1) + " - " + str(scoreP2)))
    
    #The non-Background objects to be displayed
    global nonBackground_Squares 
    nonBackground_Squares = [paddle,paddle2,ball_square]

    #The text objects to be displayed
    global nonBackground_Text 
    nonBackground_Text = [score_display]
    
    #A while loop to run the game, detect the inputs, and to call the draw function.
    while 1:
        detectKeys()
        temp = moveBall()
        if(temp == 1):
            scoreP2 += 1
        elif(temp == 2):
            scoreP1 += 1
        nonBackground_Text[0].setText(str(scoreP1) + " - " + str(scoreP2))
        
        for x in range(10):
            draw() 
    
     
            
initlize()