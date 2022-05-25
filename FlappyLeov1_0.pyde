'''Name: Amiteash Paul, Aditya Balakrishnan, Event Sharku
NetId: ap6444, ab9348, es5531
Course Name: CS-UH 1001 Introduction to Computer Science
Assignment Name: Final Assignment - Flappy Leo
Description: A Flappy Bird clone inspired by the movie Inception
Date: 05/16/2022
'''
# Add Minim library - for sound
add_library('minim')

# Import modules
import random
import os
from math import *
import copy

#To get absolute path
path = os.getcwd()

#Audio Player
player = Minim(this)

#Game Window Dimensions
WIDTH = 1280
HEIGHT = 800

#Declare variables
start_image = None
font = None
music = None
game = None
scoresound = None
warningsound = None
deathvoices = []
open_sans = None

mute_music = False

class Game:
    def __init__(self, w, h, g, font, music):
        self.w = w #Width
        self.h = h #Height
        self.g = g #Ground
        self.leo = Leo(150, 100, 35, 0, self.g, "leo.png") #Leo Object
        self.building_image = loadImage(path + "/assets/images/building.png") #Image for upright buildings
        self.buildings = [] #List of buildings - updated every time a building leaves the screen
        self.get5buildings() #Get first 5 buildings
        self.ground = Ground(self.w, h - g, self.h) #Ground object
        self.font = font #Inception font
        self.score = 0
        self.oldframe = 0
        self.flipped = 0
        self.bg_music = music
        self.death_voice = random.choice(deathvoices)
        self.started = False
        self.scorecheck = 1
        self.background_images = []
        for images in [1, 1, 2, 2, 3, 3]:
            self.background_images.append(loadImage(path + "/assets/images/bg_" + str(images) + ".png"))
        self.bg_x = []
        for images in range(3):
            self.bg_x.append(0)
            self.bg_x.append(self.w)
            
        #Mute Icons
        self.bg_music_mute = False
        self.music_playing = loadImage(path + "/assets/images/music.png")
        self.music_mute = loadImage(path + "/assets/images/no_music.png")
        
        #Menu
        self.display_menu = False
        self.menu = loadImage(path + "/assets/images/info.png")
    
    # Display Method
    def display(self):        
        if self.leo.alive == False:
            #Game Over Screen
            self.bg_music.pause()
            background(51)
            fill(255, 204, 0)
            textFont(self.font)
            text("GAME OVER", 240, 380)
            textSize(46)
            text("Score: " + str(self.score), 510, 450)
            return
        
        if self.started == False:
            image(start_image, 0, 0, self.w, self.h)
        else:
            #Background Images - 2 for each background to keep up the continuous scroll
            imageMode(CORNER)
            image(self.background_images[0], self.bg_x[0],0, self.w, self.h)
            image(self.background_images[1], self.bg_x[1],0, self.w, self.h)
            image(self.background_images[2], self.bg_x[2],0, self.w, self.h//4)
            image(self.background_images[3], self.bg_x[3],0, self.w, self.h//4)
            image(self.background_images[4], self.bg_x[4],self.g - self.h//3, self.w, self.h//3)
            image(self.background_images[5], self.bg_x[5],self.g - self.h//3, self.w, self.h//3)
            
            #Parallax Background - Images move at different speeds and move to right once they completely leave the screen
            if self.started:
                self.bg_x[0] -= 3
                self.bg_x[1] -= 3
                self.bg_x[2] -= 5
                self.bg_x[3] -= 5
                self.bg_x[4] -= 7
                self.bg_x[5] -= 7
                
            for i in range(len(self.bg_x)):
                if self.bg_x[i] <= -self.w:
                    self.bg_x[i] = self.w
            
            #Leo Display and Update
            self.leo.display()
            if self.started:
                self.leo.update()
            
            #Add score and restore flipped condition
            if (self.leo.x > self.buildings[0].x) and (self.scorecheck==1):
                self.score+=1
                scoresound.rewind()
                warningsound.rewind()
                scoresound.play()
                self.scorecheck = 0
                self.oldframe = frameCount
                self.flipped = 0
            
            # Flip gravity every 5 points
            if (self.score > 0) and (self.score % 5 == 0):
                if (frameCount - self.oldframe) <= 25:
                    warningsound.play()
                    textFont(open_sans)
                    textSize(36)
                    fill(255,204,0)
                    text("WARNING: GRAVITY FLIPPING", 400, 300)
                if (frameCount - self.oldframe) >= 25 and (self.flipped == 0):
                    self.leo.gravacc = - self.leo.gravacc
                    self.leo.rise = - self.leo.rise
                    self.flipped = 1
                        
            #Ground Display
            self.ground.display()
            
            #Delete buildings that move all the way left
            if (self.buildings[0].x + self.buildings[0].w < 0):
                self.buildings = self.buildings[1:]
                self.getBuildings()
                self.scorecheck = 1
            
            #Building Display
            for index in range(len(self.buildings)):
                self.buildings[index].display()
                if self.started:
                    self.buildings[index].update()
            
            #Score Display
            #self.updatescore()
            textFont(open_sans)
            textSize(40)
            fill(255,255,255)
            text("Score: " + str(self.score), 30, 40)
            
            #Mute Sound, Image display
            if self.bg_music_mute == False:
                imageMode(CORNER)
                music_playing = image(self.music_playing, 1200, 40, 40, 40)
            else:
                imageMode(CORNER)  
                music_mute = image(self.music_mute, 1200, 40, 40, 40)
            
            global mute_music
            if self.bg_music_mute == True  and mute_music == False:
                self.bg_music.pause()
                mute_music = True
            elif self.bg_music_mute == False and mute_music == True:
                self.bg_music.play()
                self.bg_music.loop()
                mute_music = False
            

    #Initial Get buildings
    def get5buildings(self):
        for i in range(5):
            self.buildings.append(Building(WIDTH + i * 500, 70, self.g, 250, 10, None, self.building_image)) 
    
    #Get buildings
    def getBuildings(self):
        self.buildings.append(Building(self.buildings[-1].x + 500, 70, self.g, 200, 10, None, self.building_image))
        

#Leo - Our Protagonist
class Leo:
    def __init__(self, x, y, r, vy, g, img):
        self.x = x
        self.y = y
        self.r = r
        self.vy = vy
        self.g = g
        self.img = loadImage(path + "/assets/images/" + img)
        self.gravacc = 7.81 #Acceleration due to gravity in pixels/frame^2 (9.81 is too fast :( )
        self.rise = -40 #Rise in pixels with each flap
        self.alive = True
        #self.jump = player.loadFile(path + "/sounds/jump.mp3")
        self.vmult = 0.9 #speed multiplier (for better control in debugging)

    def update(self):
        self.gravity()
        self.vy *= self.vmult
        self.y += self.vy

        # Boundary conditions
        if (self.y > height):
            self.y = height
            self.vy = 0
    
        if (self.y < 0):
            self.y = 0
            self.vy = 0
        
        # Check for collision with ground or no collision with building empty space (easier than individually checking for collision with the two buildings)
        if game.ground.collisionY() or ((game.buildings[0].collisionX()) and not(game.buildings[0].collisionY())):
                game.death_voice.play()
                self.alive = False
    
    # Accelerates fall (or rise in gravity flip mode) by set amount
    def gravity(self):
        self.vy += self.gravacc
    
    # Rises (or falls in gravity flip mode) by set amount
    def flap(self):
        self.vy = self.rise
    
    # Leonardo DiCaprio's face
    def display(self):
        imageMode(CENTER)
        image(self.img, self.x, self.y, self.r * 4, self.r * 2)
    
    #Returns distance to an object (planned feature for coins)
    def distance(self, targetX, targetY):
        return sqrt((self.x - targetX)**2 + (self.y - targetY) ** 2)

#Obstacles - Buildings and Ground
class Obstacle():
    def __init__(self, x, y, w, h, g, vx, img):
        self.collx = x
        self.colly = y
        self.w = w
        self.h = h
        self.g = g
        self.vx = vx
        self.img = img

    #Horizontal collision range
    def collisionX(self):
        #Horizontally in range
        if game.leo.x <= (self.collx + self.w) and game.leo.x >= (self.collx):
            return True
        else:
            return False

    #Vertical collision range
    def collisionY(self):
        #Vertically in range
        if game.leo.y <= (self.colly + self.h) and game.leo.y >= (self.colly):
            return True
        else:
            return False


#Ground - Just an obstacle that has a display method
class Ground(Obstacle, object):
    def __init__(self, w, h, g):
        self.groundimg = loadImage(path + "/assets/images/ground.png")
        super(Ground, self).__init__(0, g-h, w, h, g, 0, None)

    def display(self):
        strokeWeight(0)
        fill(0, 125, 0)
        imageMode(CORNER)
        image(self.groundimg, 0, self.colly, self.w, self.h)


#Building Class - An obstacle with both display and update
class Building(Obstacle, object):
  def __init__(self, x, w, g, space, vx, img, building_image):
    self.x = x
    self.y = random.randint(100,300)
    self.space = space
    self.w = w
    super(Building, self).__init__(self.x, self.y, self.w, self.space, g, vx, img)
    self.building_image = building_image
    self.building_image2 = loadImage(path + "/assets/images/inverted_building.png")

  def display(self):
    strokeWeight(0)
    fill(125, 0, 0)
    imageMode(CORNER)
    #Upside down building
    rect(self.x, 0, self.w, self.y) # In case image doesn't load
    image(self.building_image2, self.x, 0, self.w, self.y)
    #Right side up building
    rect(self.x, self.y + self.space, self.w, self.g-self.y-self.space) # In case image doesn't load
    image(self.building_image, self.x, self.y + self.space, self.w, self.g-self.y-self.space)

  def update(self):
    # Building Movement
    self.x = self.x - self.vx
    self.collx = self.x

# ----- #

#Client Class

#Setup
def setup():
  size(WIDTH, HEIGHT)
  #Load Starting Image
  global start_image
  start_image = loadImage(path + "/assets/images/inception.jpeg")
  #Load BG Music
  global music
  music = player.loadFile(path + "/assets/audio/bgmusic.mp3")
  #Load Score SFX
  global scoresound
  scoresound = player.loadFile(path + "/assets/audio/score.mp3")
  #Load Warning Klaxon SFX
  global warningsound
  warningsound = player.loadFile(path + "/assets/audio/warning.mp3")
  #Load Character Death Voice Lines
  deathvoice1 = player.loadFile(path + "/assets/audio/death1.mp3")
  deathvoice2 = player.loadFile(path + "/assets/audio/death2.mp3")
  global deathvoices
  deathvoices.append(deathvoice1)
  deathvoices.append(deathvoice2)
  #Load Inception Font
  global font
  font = createFont(path + "/assets/fonts/Inception_free.ttf", 128)
  #Load Open Sans Font (much more readable)
  global open_sans
  open_sans = createFont(path + "/assets/fonts/OpenSans-SemiBold.ttf", 128)
  #Generate Game
  global game
  game = Game(WIDTH, HEIGHT, 720, font, music)
  game.bg_music = player.loadFile(path + "/assets/audio/bgmusic.mp3")
  game.font = createFont(path + "/assets/fonts/Inception_free.ttf", 128)

#Draw
def draw():
  background(62, 61, 152)
  game.display()


#if key pressed
def keyPressed():
    global game
    if key == " ":        
        # Starts Playing
        if not game.started:
            #global game
            game.started = True
            game.death_voice.rewind()
            game.bg_music.loop()
        # Flap
        if game.started:
            game.leo.flap()
            
    # Mute audio with m key
    if key == "m":
        if game.bg_music_mute:
           game.bg_music_mute = False
        else:
           game.bg_music_mute = True

#if mouse clicked
def mouseClicked():
    # Restarts Game
    global game
    if not game.leo.alive:
        game = Game(WIDTH, HEIGHT, 720, font, music)
    
    # Mutesif you click on icon
    elif(mouseX >= 1200) and (mouseX <= 1240) and (mouseY >= 40) and (mouseY <= 80) and game.bg_music_mute == False:
        game.bg_music_mute = True
    elif(mouseX >= 1200) and (mouseX <= 1240) and (mouseY >= 40) and (mouseY <= 80) and game.bg_music_mute == True:
        game.bg_music_mute = False
    
