import pygame
import sys
from bacteria import *
# from bacteria_2 import * 
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
# bacteria_second_type_list = []



num_bact = 10 #количество молекул
radius = 10 # радиус молекул

'''
num_bact_second_type = 10 #количество молекул 2 типа
radius_second_type = 20 # радиус молекул 2 типа
'''


for i in range(num_bact):

    x = randint(0+radius, 1000-radius) # позиция x 
    y = randint(0+radius, 800-radius) # позиция y
    color = 'green'
    bacteria = Bacteria(x, y, color, radius, 0, 0)
    bacteria_list.append(bacteria)


'''

for i in range(num_bact_second_type):

    x = randint(0+radius_second_type, 1000-radius_second_type) # позиция x 
    y = randint(0+radius_second_type, 800-radius_second_type) # позиция y
    color = 'red'
    bacteria_2 = BacteriaSecondType(x, y, color, radius_second_type)
    bacteria_second_type_list.append(bacteria_2)
'''

while True:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    for i in range(num_bact):
        for j in range(i + 1, num_bact):

            bacteria_list[i].attract(bacteria_list[j])




    dis.fill((0, 0, 0))

    for bacteria in bacteria_list:

        bacteria.draw(dis)



    pygame.display.update()
    clock.tick(20)