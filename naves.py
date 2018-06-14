import pygame, sys, time, random

pygame.init()

display_width = 400
display_height = 600

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
yellow = (255,255,0)
green = (0,255,0)

gameDisplay = pygame.display.set_mode((400, 600))

pygame.display.set_caption("Naves")

clock = pygame.time.Clock()

naveImg = pygame.image.load("/naves/nave2.png")
nave_width = 66
nave_height = 82

def obs(obs_x, obs_y, obs_width, obs_height, color):
    pygame.draw.rect(gameDisplay, color, [obs_x, obs_y, obs_width, obs_height])

def obs_avoid(count, diff):
    font = pygame.font.SysFont(None, 25)
    scoretext = font.render("Score: " + str(count), True, yellow)
    leveltext = font.render("Difficulty: " + str(diff), True, green)
    gameDisplay.blit(scoretext, (10, 10))
    gameDisplay.blit(leveltext, (10, 30))

def nave(x, y):
    gameDisplay.blit(naveImg, (x, y))

def message(message):
    fontObj = pygame.font.Font("freesansbold.ttf" , 30)
    textSurfaceObj = fontObj.render(message, True, red)
    textRectObj = textSurfaceObj.get_rect()
    textRectObj.center = ((display_width/2), (display_height/2))

    gameDisplay.blit(textSurfaceObj, textRectObj)
    pygame.display.update()
    time.sleep(1)

def game_loop():
    nave_x = (display_width * 0.4)
    nave_y = (display_height * 0.85)
    nave_x_change = 0

    obs_x = random.randrange(150, display_width-150)
    obs_y = -300
    obs_speed = 5
    obs_width = 30
    obs_height = 30
    avoid_count = 0
    difficulty = 1

    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:                
                    nave_x_change += -3
                elif event.key == pygame.K_RIGHT:
                    nave_x_change += 3

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    nave_x_change += 3
                elif  event.key == pygame.K_RIGHT:
                    nave_x_change += -3

        nave_x += nave_x_change

        gameDisplay.fill(black) 
        obs_avoid(avoid_count, difficulty)
        #nave set pos
        nave(nave_x, nave_y)

        #windows boundaries
        if (nave_x > display_width - nave_width):
            nave_x = display_width - nave_width
            message("Right border reached")
        elif nave_x < 0:
            nave_x = 0
            message("Left border reached")

        obs(obs_x, obs_y, obs_width, obs_height, white)
        obs_y += obs_speed

        #obstacle rectangle
        if obs_y > display_height:
            obs_x = random.randrange(150, display_width-150)
            obs_y = -50
            avoid_count += 1
            if avoid_count % 5 == 0:
                obs_speed += 2.5
                difficulty += 1
            

        #nave-obstacle collision
        if nave_y < obs_y + obs_height:
            print("obs x + width = ", obs_x + obs_width, ", nave x = ", nave_x)
            if (nave_x + nave_width > obs_x and nave_x < obs_x + obs_width or
                nave_x + nave_width < obs_x + obs_width and nave_x + nave_width > obs_x):
                message("Collision")
                obs_x = random.randrange(150, display_width-150)
                obs_y = -50
                obs_speed = 5
                avoid_count = 0  
                difficulty = 1              

        pygame.display.update()
        clock.tick(60)

game_loop()
pygame.quit()
quit()
