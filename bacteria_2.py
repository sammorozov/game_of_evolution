import pygame
import math


class BacteriaSecondType:
    def __init__(self, x, y, color, r):
        self.x = x
        self.y = y
        self.color = color
        self.radius = r

    def attract2(self, other_bacteria):
        distance = math.sqrt((self.x - other_bacteria.x)**2 + (self.y - other_bacteria.y)**2)
        force = distance  # Притяжение
        force_repuslion =  - distance 

        alpha = abs(math.atan((other_bacteria.y - self.y)/(other_bacteria.x - self.x))) # угол в радианах между двумя точками
        

        
        if self.x <= other_bacteria.x and self.y <= other_bacteria.y and distance > self.radius + other_bacteria.radius:
            self.x += force * math.cos(alpha)
            self.y += force * math.sin(alpha)

            other_bacteria.x -= force * math.cos(alpha)
            other_bacteria.y -= force * math.sin(alpha)

        elif self.x <= other_bacteria.x and self.y >= other_bacteria.y and distance > self.radius + other_bacteria.radius:
            
            self.x += force * math.cos(alpha)
            self.y -= force * math.sin(alpha)

            other_bacteria.x -= force * math.cos(alpha)
            other_bacteria.y += force * math.sin(alpha)

        elif self.x >= other_bacteria.x and self.y >= other_bacteria.y and distance > self.radius + other_bacteria.radius:
            
            self.x -= force * math.cos(alpha)
            self.y -= force * math.sin(alpha)
        
            other_bacteria.x += force * math.cos(alpha)
            other_bacteria.y += force * math.sin(alpha)

        elif self.x >= other_bacteria.x and self.y <= other_bacteria.y and distance > self.radius + other_bacteria.radius:
            
            self.x -= force * math.cos(alpha)
            self.y += force * math.sin(alpha)

            other_bacteria.x += force * math.cos(alpha)
            other_bacteria.y -= force * math.sin(alpha)


        

        elif distance < self.radius + other_bacteria.radius:
            
            if self.x <= other_bacteria.x and self.y <= other_bacteria.y:
                self.x += force_repuslion * math.cos(alpha)
                self.y += force_repuslion * math.sin(alpha)

                other_bacteria.x -= force_repuslion * math.cos(alpha)
                other_bacteria.y -= force_repuslion * math.sin(alpha)

            elif self.x <= other_bacteria.x and self.y >= other_bacteria.y:
                
                self.x += force_repuslion * math.cos(alpha)
                self.y -= force_repuslion * math.sin(alpha)

                other_bacteria.x -= force_repuslion * math.cos(alpha)
                other_bacteria.y += force_repuslion * math.sin(alpha)

            elif self.x >= other_bacteria.x and self.y >= other_bacteria.y:
                
                self.x -= force_repuslion * math.cos(alpha)
                self.y -= force_repuslion * math.sin(alpha)
            
                other_bacteria.x += force_repuslion * math.cos(alpha)
                other_bacteria.y += force_repuslion * math.sin(alpha)

            elif self.x >= other_bacteria.x and self.y <= other_bacteria.y:
                
                self.x -= force_repuslion * math.cos(alpha)
                self.y += force_repuslion * math.sin(alpha)

                other_bacteria.x += force_repuslion * math.cos(alpha)
                other_bacteria.y -= force_repuslion * math.sin(alpha)

            else:
                pass

        else:
            print('исключение!')
            print('координата x', self.x, other_bacteria.x)
            print('координата y', self.y, other_bacteria.y)
            pass

    def draw2(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)
        
# for l in range(num_bact_second_type):
    #     for k in range(num_bact):

    #         bacteria_second_type_list[l].attract2(bacteria_list[k])


    # for m in range(num_bact_second_type):
    #     for n in range(m + 1, num_bact_second_type):

    #         bacteria_second_type_list[m].attract2(bacteria_second_type_list[n])


# for bacteria_2 in bacteria_second_type_list:

    #     bacteria_2.draw2(dis)