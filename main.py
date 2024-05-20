import pygame

win = pygame.display.set_mode((700,700))

pygame.display.set_caption("First Game")

run = True

x = 350
y = 350
radius = 15
val_x = 10
val_y = 10
jump = False

while run:

    win.fill((0,0,0))
    pygame.draw.circle(win, (255,255,255), (int(x),int(y)), radius)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False


    userInput = pygame.key.get_pressed()

    if userInput[pygame.K_LEFT] and x > 0:
        x -= val_x
    if userInput[pygame.K_RIGHT] and x < 700:
        x += val_x
    # if userInput[pygame.K_UP] and y > 0:
    #     y -= val
    # if userInput[pygame.K_DOWN] and y < 700:
    #     y += val
    if jump == False and userInput[pygame.K_SPACE]:
        jump = True

    if jump == True:
        y -= val_y*3
        val_y -= 1
        if val_y < -10:
            jump = False
            val_y = 10


    pygame.time.delay(50)

    pygame.display.update()
    