import pygame
import math


class Bacteria:
    def __init__(self, x, y, color, r):
        self.x = x
        self.y = y
        self.color = color
        self.radius = r

    def attract(self, other_bacteria):
        distance = math.sqrt((self.x - other_bacteria.x)**2 + (self.y - other_bacteria.y)**2)
        force = 100 / distance  # Притяжение 

        force_repuslion =  - 30 / distance 

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

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)
        
