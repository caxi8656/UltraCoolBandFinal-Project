'''
/////////// please write UPDATE: (date) to keep track of edits made to the code /////////////////////
UPDATE: 12/1/22 Skeleton
UPDATE: 12/2/22 Slight Progress
UPDATE: 12/9/22 Team Zoom + Dr. Z Sound Help
UPDATE: 12/11/22 Team Zoom - Basic Sound and Image Finished
UPDATE: 12/13/22 Added descriptions, docstrings, and comments, and cleaned up the code 
///////////////////////////////////////////////////////////////////////////////////////////////

The Ultra Cool Stage Band B)

AUTHORS: Catherine Xie, Esther San Diego, Dahn Bi Chong, Leonardo LaPorta
DATE: 12/14/22

Description:
Welcome to the band! B)
This is a very cool band filled with very talented musicians that may or may not know what they're doing.

Left click on a musician to tell them to play their instrument or sing.
Keep clicking on musicians to tell them to play together.
Right click to tell them to stop.
Find out what combinations of musicians sounds best to you!
'''

import pygame
pygame.init()
pygame.mixer.init(44100, -16, 2, 16384)

# ============================== set up window ====================================================
w = 1280
h = 720
win = pygame.display.set_mode((w, h))

# ======================== set up global variables ================================================



# ================== create Musician class =====================
class Musician:
    '''
    When instantiated:
    Creates singers and instrumentalists by loading in png's
    Assign's audio to each musician
    Creates a position for the musician to be placed
    Assign's a channel for the musician's audio to go
    '''

    def __init__(self, xcor, ycor, img, aud, chNum):
        # position
        self.x = xcor
        self.y = ycor

        # image size
        self.iw = 180
        self.ih = 280
        self.size = (self.iw, self.ih)

        # audio
        self.ch = pygame.mixer.Channel(chNum)  # assign channels
        self.sound = pygame.mixer.Sound(aud) # load sound

        # create surface and fill it with an image
        self.image = pygame.image.load(img).convert_alpha() # convert()_alpha makes png transparent
        self.image = pygame.transform.scale(self.image, self.size)


    def draw(self):
        '''
        Draws the musician png images onto the background window
        '''
        win.blit(self.image, (self.x, self.y))
        

    def clicked(self, event, img, imgPly):
        '''
        If the user left clicks where the image is, change the image to the "playing" image, and play audio.
        If the user right clicks the image, change back to original image and stop audio.
        '''
        if event.type == pygame.MOUSEBUTTONDOWN:
            mousePos = pygame.mouse.get_pos() # get mouse position

            # if the mouse position is in the same location as the drawn png
            if win.blit(self.image, (self.x, self.y)).collidepoint(mousePos):
                if event.button == 1: # left click
                    # change image to playing image
                    self.image = pygame.image.load(imgPly).convert_alpha()
                    self.image = pygame.transform.scale(self.image, self.size)
        
                    # insert sound
                    self.ch.play(self.sound, loops = -1)
                    
                if event.button == 3: # right click
                    # change image to playing image
                    self.image = pygame.image.load(img).convert_alpha()
                    self.image = pygame.transform.scale(self.image, self.size)
        
                    # insert sound
                    self.ch.stop()


# ======================= create Manager class =======================
class Manager:
    '''
    Sets up the background window
    Sets up main function with a while animation loop
    Instantiates Musician classes
    Calls necessary object methods
    '''
    def __init__(self):
        self.bgImg = pygame.image.load("Concert_Hall.png").convert()
        self.bgImg = pygame.transform.scale(self.bgImg, (w,h))
        self.caption = pygame.display.set_caption("Ultra Cool Stage Band") 

    
    def drawBackground(self):
        '''
        Draws the background image onto the window
        '''
        win.blit(self.bgImg,(0,0))
    

    def main(self):
        # ============================= instantiate objects here ===============================================
        soprano = Musician(95, 50 , 'Soprano1.png', 'SopranoNew.wav', 0)
        alto = Musician(383, 50, 'Alto1.png', 'AltoNew.wav', 1)
        tenor = Musician(710, 50, 'Tenor1.png', 'TenorNew.wav', 2)
        confusedBass = Musician(1015, 50, 'Bass1.png','CountryMAMa.wav', 3)
        robot = Musician(230, 360, 'Robot1.png', 'Robot.wav', 4)
        trumpet = Musician(535, 360, 'Trumpet1.png', 'Trumpeeet.wav', 5)
        piano = Musician(880, 370, 'Piano2.png', 'PPiano.wav', 6)

        # create a running variable
        running = True

        # ======================== animation while loop ========================================================
        while running:
            win.fill((0, 0, 0))
            self.drawBackground() # background needed to be drawn before everything, so it goes first

            # ========================= add all events here =====================================================
            for event in pygame.event.get():
                soprano.clicked(event, 'Soprano1.png', 'Soprano2.png')
                alto.clicked(event, 'Alto1.png', 'Alto2.png')
                tenor.clicked(event, 'Tenor1.png', 'Tenor2.png')
                confusedBass.clicked(event, 'Bass1.png', 'Bass2.png')
                robot.clicked(event, 'Robot1.png', 'Robot2.png')
                trumpet.clicked(event, 'Trumpet1.png', 'Trumpet2 (1).png')
                piano.clicked(event, 'Piano2.png', 'Piano1.png')

                if event.type == pygame.QUIT:  # if user closes the window, code stops
                    pygame.quit()

            # ========================= add drawing events here ==================================================
            soprano.draw()
            alto.draw()
            tenor.draw()
            confusedBass.draw()
            robot.draw()
            trumpet.draw()
            piano.draw()

            # update the window
            pygame.display.update()


# ================== run the code =================================
Manager().main()
