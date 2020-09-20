import pygame
import sys
import  random
import time
pygame.init()
size = [width, height] = [900, 700]
snakehead = [125,125]
snakebody = [[100,125],[75,125],[50,125],[25,125]]
BLACK = 0,0,0
RED = 255,0,0
GREEN = 0,255,0
BLUE = 0,0,255
screen = pygame.display.set_mode(size)
pygame.display.set_caption('V3.0')
#限定帧速率
fpsclock = pygame.time.Clock()
def food():
    food_x = random.randint(0,35)
    food_y = random.randint(0,27)
    pd = 0
    an = [food_x,food_y]
    if an == headrect:
        pd = 1
    for i in range(len(snakebody)):
        if snakebody[i] == an:
            pd = 1
    if pd == 1:
        return food()
    return [food_x,food_y]

# ----------start(这里插入需要加载的图片)----------
img_up = pygame.image.load(r"Snake\up.png")
img_down = pygame.image.load(r"Snake\down.png")
img_left = pygame.image.load(r"Snake\left.png")
img_right = pygame.image.load(r"CSnake\right.png")
img_food = pygame.image.load(r"Snake\food.png")
img_body = pygame.image.load(r"Snake\body.png")
# ---------end-----------
direction = 'right'
hh = img_right
headrect = hh.get_rect()
headrect[0] = snakehead[0]
headrect[1] = snakehead[1]
#---------------死亡提示-----------------
deathfont = pygame.font.SysFont('georgia',48)
img_death = deathfont.render('Game Over! Press ESC to escape',True,BLUE)
scorefont = pygame.font.SysFont('timesnewroman',32)
scorequals1 = pygame.font.SysFont('timesnewroman',32)
# death_rect = img_death.get_rect()
score = 0
count = 0


ff=input('Please input the speed of the snake:')
ff=int(ff)
# new_food = food()
# new_food = [25 * i for i in new_food]
# screen.blit(img_food, new_food)



while 1:
    fpsclock.tick(ff)
    for event in pygame.event.get():
        # print(event)
        # fpsclock.tick(1)
        # screen.fill(BLACK)
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                if direction != 'right':
                    direction = 'left'
                    # headrect = headrect.move(-25,0)
                    print('1')
            elif event.key == pygame.K_RIGHT:
                if direction != 'left':
                    direction = 'right'
                    # headrect = headrect.move(25, 0)
                    print('2')
            elif event.key == pygame.K_UP:
                if direction != 'down':
                    direction = 'up'
                    # headrect = headrect.move(0, -25)
                    print('3')
            elif event.key == pygame.K_DOWN:
                if direction != 'up':
                    direction = 'down'
                    # headrect = headrect.move(0, 25)
                    print('4')
            elif event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
            # pygame.display.update()
    temp = headrect  # 暂存蛇头的位置
    if direction == 'left':
        headrect = headrect.move(-25, 0)
        hh = img_left
    if direction == 'right':
        headrect = headrect.move(25, 0)
        hh = img_right
    if direction == 'up':
        headrect = headrect.move(0, -25)
        hh = img_up
    if direction == 'down':
        headrect = headrect.move(0, 25)
        hh = img_down
    # screen.fill(BLACK)
    ll = len(snakebody)
    for i in range(1,ll):
        snakebody[ll-i] = snakebody[ll-i-1]
        screen.blit(hh, headrect)
        screen.blit(img_body, snakebody[i])
    screen.blit(img_body, snakebody[1])
    snakebody[0] = temp
    screen.blit(img_body,snakebody[0])
    # print(headrect,snakebody)
    pygame.display.update()#使用暂时存储的位置
    # ---------------吃食物提示-------------------
    if score == 0:
        if count == 0:
            new_food = food()
            new_food = [25 * i for i in new_food]
            screen.blit(img_food, new_food)
            true_food = new_food
            img_score = scorefont.render('Score:0', True, GREEN)
            pygame.display.update()
            count += 1
    if (headrect[0] == true_food[0] and headrect[1] == true_food[1]):
        print('222222')
        new_food = food()
        #将随机数对应到全屏
        new_food = [25 * i for i in new_food]
        screen.blit(img_food, new_food)
        true_food = new_food
        score += 1
        img_score = scorefont.render('Score:%d'% score,True,GREEN)
        screen.blit(img_score, [25,25])
        pygame.display.update()
        apx = 2*snakebody[ll-1][0] - snakebody[ll-2][0]
        apy = 2*snakebody[ll-1][1] - snakebody[ll-2][1]
        snakebody.append([apx,apy])
        pygame.display.update()
    # ---------------吃食物提示end-------------------
    #---------------死亡提示-------------------
    detec = 0
    for i in range(len(snakebody)):
        if snakebody[i] == headrect:
            detec = 1
    if (headrect[0] < 0 or headrect[0] > 900 or headrect[1] < 0 or headrect[1] > 700) or(detec == 1):
        while 1:
            img_death = deathfont.render('Game Over! Press ESC to escape Score:%d'%score, True, BLUE)
            screen.blit(img_death,[5,320])
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        sys.exit()
    screen.blit(img_food,true_food)
    screen.blit(img_score, [25, 25])
    pygame.display.update()
    screen.fill(BLACK)
    if (headrect[0] == true_food[0] and headrect[1] == true_food[1]):
        print("Ohhhhhhhhhhhhhhhh")

    #---------------结束死亡提示-------------------
    # time.sleep(10) #现在不用了，可以通过改变fps值来完成
    # print(snakebody[1])
    #画蛇
    # for i in range(len(snakebody)):
    #     screen.blit(img_right,headrect)
    #     screen.blit(img_body,snakebody[i])
    #     pygame.display.update()
    # headrect = headrect.move(25,0)
    # time.sleep(0.5)
#屏幕的刷新频率（就是蛇的整个身子的位置的更新频率）
# time.sleep(1)