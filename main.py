import pygame
import random
from pygame.examples.scrap_clipboard import screen
from pygame.examples.sprite_texture import running

pygame.init()
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

pygame.display.set_caption("Игра Тир")
icon = pygame.image.load("images/img1.jpg")
pygame.display.set_icon(icon)

target_img = pygame.image.load("images/img2.jpg")
target_width = 80
target_height = 80
target_x = random.randint(0,SCREEN_WIDTH - target_width)
target_y = random.randint(0,SCREEN_HEIGHT - target_height)

color = ((random.randint(0,255), (random.randint(0,255),(random.randint(0,255))

running = True #Переменная running позволяет контролировать игровой цикл. В этой переменной сначала хранится значение True, которое позволяет циклу while работать бесконечно. То есть, пока running равно True, игра будет продолжаться и выполнять свои команды. Отдельная переменная running используется чтобы в нужный момент остановить игру. Когда потребуется завершить игровой процесс необходимо изменить значение этой переменной на False. Как только это произойдет, цикл while прекратится, и игра остановится. Таким образом, вся игра управляется этим циклом, и с помощью переменной running и можно контролировать ее завершение.
while running:
    pass


pygame.quit()