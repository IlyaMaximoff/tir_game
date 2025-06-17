import pygame
import random

pygame.init()
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

pygame.display.set_caption("Игра Тир")
icon = pygame.image.load("images/img1.jpg")
pygame.display.set_icon(icon)

target_img = pygame.image.load("images/img2.jpg")
target_width = 116
target_height = 116
target_x = random.randint(0,SCREEN_WIDTH - target_width)
target_y = random.randint(0,SCREEN_HEIGHT - target_height)

color = random.randint(0,255), random.randint(0,255), random.randint(0,255)

running = True #Переменная running позволяет контролировать игровой цикл. В этой переменной сначала хранится значение True, которое позволяет циклу while работать бесконечно. То есть, пока running равно True, игра будет продолжаться и выполнять свои команды. Отдельная переменная running используется чтобы в нужный момент остановить игру. Когда потребуется завершить игровой процесс необходимо изменить значение этой переменной на False. Как только это произойдет, цикл while прекратится, и игра остановится. Таким образом, вся игра управляется этим циклом, и с помощью переменной running и можно контролировать ее завершение.
while running:
    screen.fill(color)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONUP:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if target_x < mouse_x < target_x + target_width and target_y < mouse_y < target_y + target_height:
                target_x = random.randint(0, SCREEN_WIDTH - target_width)
                target_y = random.randint(0, SCREEN_HEIGHT - target_height)

    screen.blit(target_img,(target_x,target_y))
    pygame.display.update()

pygame.quit()