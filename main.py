import pygame
import sys
from bacteria import *
from bacteria_2 import * 
import pygame.time
from random import randint




pygame.init()

dis=pygame.display.set_mode((1000, 800))
pygame.display.update()


clock = pygame.time.Clock()

'''
создаем несколько экземпляров класса бактерия в список
'''
bacteria_list = []
bacteria_second_type_list = []



num_bact = 10 #количество молекул
radius = 20 # радиус молекул


num_bact_second_type = 30 #количество молекул 2 типа
radius_second_type = 5 # радиус молекул 2 типа



for i in range(num_bact):

    x = randint(0+radius, 1000-radius) # позиция x 
    y = randint(0+radius, 800-radius) # позиция y
    color = 'green'
    bacteria = Bacteria(x, y, color, radius)
    bacteria_list.append(bacteria)

for i in range(num_bact_second_type):

    x = randint(0+radius_second_type, 1000-radius_second_type) # позиция x 
    y = randint(0+radius_second_type, 800-radius_second_type) # позиция y
    color = 'red'
    bacteria_2 = BacteriaSecondType(x, y, color, radius_second_type)
    bacteria_second_type_list.append(bacteria_2)


while True:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    for i in range(num_bact):
        for j in range(i + 1, num_bact):

            bacteria_list[i].attract(bacteria_list[j])


    for l in range(num_bact_second_type):
        for k in range(num_bact):

            bacteria_second_type_list[l].attract2(bacteria_list[k])


    for m in range(num_bact_second_type):
        for n in range(m + 1, num_bact_second_type):

            bacteria_second_type_list[m].attract2(bacteria_second_type_list[n])

    dis.fill((0, 0, 0))

    for bacteria in bacteria_list:

        bacteria.draw(dis)
    
    for bacteria_2 in bacteria_second_type_list:

        bacteria_2.draw(dis)


    pygame.display.update()
    clock.tick(30)