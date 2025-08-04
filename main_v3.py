import pygame
import random

pygame.init()

display_width = 800
display_height = 600

black = (0, 0, 0)
white = (255, 255, 255)

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("Penguin Game")

backgroundImg = pygame.image.load('background.png')  
backgroundImg = pygame.transform.scale(backgroundImg, (display_width, display_height))

playerImg = pygame.image.load('penguin.png')
playerImg = pygame.transform.scale(playerImg, (60, 75))
player_width = playerImg.get_width()
player_height = playerImg.get_height()

coinImg = pygame.image.load('coin.jfif')
coinImg = pygame.transform.scale(coinImg, (75, 75))
coin_width = coinImg.get_width()
coin_height = coinImg.get_height()

fireImg = pygame.image.load('fire.jfif')
fireImg = pygame.transform.scale(fireImg, (75, 75))
fire_width = fireImg.get_width()
fire_height = fireImg.get_height()

#Ammendment - Sound
coin_sound = pygame.mixer.Sound("collectcoin.mp3")

paused_font = pygame.font.SysFont(None, 75)
paused_text = paused_font.render("PAUSED", True, (255, 0, 0))

x = (display_width * 0.45)
y = (display_height * 0.8)

falling_x = random.randrange(0, display_width)
falling_y = 0 - coin_height
falling_speed = 5

falling_x2 = random.randrange(0, display_width)
falling_y2 = 0 - fire_height
falling_speed2 = 5

x_change = 0
score = 0

def player(x, y):
    gameDisplay.blit(playerImg, (x, y))

def coin(x, y):
    gameDisplay.blit(coinImg, (falling_x, falling_y))

def fire(x, y):
    gameDisplay.blit(fireImg, (falling_x2, falling_y2))    

def display_score():
    font = pygame.font.SysFont(None, 30)
    text = font.render("Score: " + str(score), True, white)
    gameDisplay.blit(text, [0, 0])

clock = pygame.time.Clock()
crashed = False
fps = 60

player_Name = ""
startscreen = True
maingame = False
gameoverscreen = False

scoreslist = []
count = 1 

scores_file = "scores.txt"

def highscoretable():
    global scoreslist, count
    try:
        with open(scores_file, "r") as file:
            scores = [line.split() for line in file]

        for i in range(len(scores)):
            scores[i][1] = int(scores[i][1])

        scores.sort(key=lambda score: score[1], reverse=True)

        scoreslist = []
        length = min(len(scores), 5) 
        if length > 0:
            for i in range(length):
                scoreslist.append(str(scores[i][0]) + " " + str(scores[i][1]))

    except FileNotFoundError:
        scoreslist = []

def display_high_scores():
    gameDisplay.fill(white)
    font = pygame.font.SysFont(None, 35)
    text = font.render("High Scores", True, black)
    gameDisplay.blit(text, (50, 100))

    if len(scoreslist) == 5:
        for i in range(5):
            score_text = font.render(str(scoreslist[i]), True, black)
            gameDisplay.blit(score_text, (50, 150 + i * 50))
    else:
        not_enough = font.render("There are not enough scores to display", True, black)
        gameDisplay.blit(not_enough, (50, 150))

    pygame.display.update()


def reset_game():
    global x, y, falling_x,falling_y,falling_x2, falling_y2,score
    x = (display_width * 0.45)
    y = (display_height * 0.8)
    falling_x = random.randrange(0, display_width - coin_width * 2)
    falling_y = 0 - coin_height
    falling_x2 = random.randrange(0, display_width - coin_width * 2)
    falling_y2 = 0 - fire_height
    score = 0


def start_game():
    global startscreen, maingame, gameoverscreen
    startscreen = False
    maingame = True
    gameoverscreen = False
    reset_game()

while not crashed:
    while startscreen:
        if player_Name == "":
            player_Name = input("Enter a player name: ")
        gameDisplay.fill(white)
        font = pygame.font.SysFont(None, 75)
        text = font.render("Press Enter to Start", True, black)
        gameDisplay.blit(text, (50, 100))
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    start_game()
                    count = 1  
        pygame.display.update()

    while maingame:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                crashed = True
                maingame = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    x_change = -5
                elif event.key == pygame.K_d:
                    x_change = 5
                elif event.key == pygame.K_SPACE:
                    y_change = 5
                elif event.key == pygame.K_ESCAPE:
                    crashed = True
                    maingame = False
                #Amendment:
                #Pause function - Client asked for this amandment to add more functionality and so players can stop playing then pick it back up.
                #This improves the game as it makes it more accessible and allows people to get high scores without being affected by outside features.
                elif event.key == pygame.K_p:
                    fps = 0.5
                    gameDisplay.blit(paused_text, (display_width // 2 - paused_text.get_width() // 2, display_height // 2 - paused_text.get_height() // 2))
                    pygame.display.update()
                elif event.key == pygame.K_u:
                    fps = 60
                    gameDisplay.fill(white)
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_a or event.key == pygame.K_d:
                    x_change = 0

        x += x_change
        
        gameDisplay.blit(backgroundImg, (0, 0))
        player(x, y)
        coin(falling_x, falling_y)
        fire(falling_x2, falling_y2)

        falling_y2 += falling_speed2
        if falling_y2 > display_height:
            falling_y2 = 0 - fire_height
            falling_x2 = random.randrange(0, display_width)
        falling_y += falling_speed
        if falling_y > display_height:
            falling_y = 0 - coin_height
            falling_x = random.randrange(0, display_width)
            with open(scores_file, "a") as file:
                file.write(player_Name + " " + str(score) + "\n")
            scoreslist = []  
            highscoretable()  
            display_high_scores()
            pygame.display.update()
            pygame.time.delay(2000)  
            reset_game()

        if y < falling_y + coin_height:
            if x > falling_x and x < falling_x + coin_width or x + player_width > falling_x and x + player_width < falling_x + coin_width:
                pygame.mixer.Sound.play(coin_sound)
                pygame.mixer.music.stop()
                falling_y = 0 - coin_height
                falling_x = random.randrange(0, display_width)
                score += 1

        if y < falling_y2 + fire_height:
            if x > falling_x2 and x < falling_x2 + fire_width or x + player_width > falling_x2 and x + player_width < falling_x2 + fire_width:
                falling_y2 = 0 - fire_height
                falling_x2 = random.randrange(0, display_width)
                score -= 1        

        x += x_change
        if x > display_width - player_width or x < 0:
            x_change = 0
        display_score()
        pygame.display.update()
        clock.tick(fps)


    while gameoverscreen:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    start_game()
                    count = 1 
                if event.key == pygame.K_ESCAPE:
                    crashed = True
        gameDisplay.fill(white)
        font = pygame.font.SysFont(None, 35)
        text = font.render("High Scores", True, black)
        gameDisplay.blit(text, (50, 100))

        if len(scoreslist) == 5:
            score1 = font.render(str(scoreslist[0]), True, black)
            score2 = font.render(str(scoreslist[1]), True, black)
            score3 = font.render(str(scoreslist[2]), True, black)
            score4 = font.render(str(scoreslist[3]), True, black)
            score5 = font.render(str(scoreslist[4]), True, black)
            gameDisplay.blit(score1, (50, 150))
            gameDisplay.blit(score2, (50, 200))
            gameDisplay.blit(score3, (50, 250))
            gameDisplay.blit(score4, (50, 300))
            gameDisplay.blit(score5, (50, 350))
        else:
            notenough = font.render("There are not enough scores to display", True, black)
            gameDisplay.blit(notenough, (50, 150))
        pygame.display.update()

pygame.quit()
quit() 