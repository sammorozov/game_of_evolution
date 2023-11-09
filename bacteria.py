import pygame
import math


class Bacteria:
    def __init__(self, x, y, color, r, vx, vy):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.color = color
        self.radius = r


    def attract(self, other_bacteria):
        distance = math.sqrt((self.x - other_bacteria.x)**2 + (self.y - other_bacteria.y)**2)
        force = 10 / distance  # Притяжение 
        force_repuslion =  - 1 / distance 

        alpha = abs(math.atan((other_bacteria.y - self.y)/(other_bacteria.x - self.x))) # угол в радианах между двумя точками
        

        if self.x <= 0 or self.x >= 1000:
            self.vx = - self.vx

        if self.y <= 0 or self.y >= 800:
            self.vy = - self.vy
        
        if other_bacteria.x <= 0 or other_bacteria.x >= 1000:
            other_bacteria.vx = - other_bacteria.vx

        if other_bacteria.y <= 0 or other_bacteria.y >= 800:
            other_bacteria.vy = - other_bacteria.vy
        
        if self.x <= other_bacteria.x and self.y <= other_bacteria.y and distance > self.radius + other_bacteria.radius:
            #было просто self.x += force * math.cos(alpha)
            self.vx = self.vx + force * math.cos(alpha)
            self.vy = self.vy + force * math.sin(alpha)
            self.x += self.vx
            self.y += self.vy

            other_bacteria.vx = other_bacteria.vx - force * math.cos(alpha)
            other_bacteria.vy = other_bacteria.vy - force * math.sin(alpha)
            other_bacteria.x += other_bacteria.vx
            other_bacteria.y += other_bacteria.vy

        elif self.x <= other_bacteria.x and self.y >= other_bacteria.y and distance > self.radius + other_bacteria.radius:
            
            self.vx = self.vx + force * math.cos(alpha)
            self.vy = self.vy - force * math.sin(alpha)
            self.x += self.vx
            self.y += self.vy


            other_bacteria.vx = other_bacteria.vx - force * math.cos(alpha)
            other_bacteria.vy = other_bacteria.vy + force * math.sin(alpha)
            other_bacteria.x += other_bacteria.vx
            other_bacteria.y += other_bacteria.vy



        elif self.x >= other_bacteria.x and self.y >= other_bacteria.y and distance > self.radius + other_bacteria.radius:
            
            self.vx = self.vx - force * math.cos(alpha)
            self.vy = self.vy - force * math.sin(alpha)
            self.x += self.vx
            self.y += self.vy



            other_bacteria.vx = other_bacteria.vx + force * math.cos(alpha)
            other_bacteria.vy = other_bacteria.vy + force * math.sin(alpha)
            other_bacteria.x += other_bacteria.vx
            other_bacteria.y += other_bacteria.vy


        elif self.x >= other_bacteria.x and self.y <= other_bacteria.y and distance > self.radius + other_bacteria.radius:
            
            self.vx = self.vx - force * math.cos(alpha)
            self.vy = self.vy + force * math.sin(alpha)
            self.x += self.vx
            self.y += self.vy

            other_bacteria.vx = other_bacteria.vx + force * math.cos(alpha)
            other_bacteria.vy = other_bacteria.vy - force * math.sin(alpha)
            other_bacteria.x += other_bacteria.vx
            other_bacteria.y += other_bacteria.vy
        

        elif distance < self.radius + other_bacteria.radius:
            
            if self.x <= other_bacteria.x and self.y <= other_bacteria.y:

                
                self.vx = self.vx + force_repuslion * math.cos(alpha)
                self.vy = self.vy + force_repuslion * math.sin(alpha)
                self.x += self.vx
                self.y += self.vy


                other_bacteria.vx = other_bacteria.vx - force_repuslion * math.cos(alpha)
                other_bacteria.vy = other_bacteria.vy - force_repuslion * math.sin(alpha)
                other_bacteria.x += other_bacteria.vx
                other_bacteria.y += other_bacteria.vy

            elif self.x <= other_bacteria.x and self.y >= other_bacteria.y:
                
                self.vx = self.vx + force_repuslion * math.cos(alpha)
                self.vy = self.vy - force_repuslion * math.sin(alpha)
                self.x += self.vx
                self.y += self.vy


                other_bacteria.vx = other_bacteria.vx - force_repuslion * math.cos(alpha)
                other_bacteria.vy = other_bacteria.vy + force_repuslion * math.sin(alpha)
                other_bacteria.x += other_bacteria.vx
                other_bacteria.y += other_bacteria.vy

            elif self.x >= other_bacteria.x and self.y >= other_bacteria.y:
                
                self.vx = self.vx - force_repuslion * math.cos(alpha)
                self.vy = self.vy - force_repuslion * math.sin(alpha)
                self.x += self.vx
                self.y += self.vy
            
                other_bacteria.vx = other_bacteria.vx + force_repuslion * math.cos(alpha)
                other_bacteria.vy = other_bacteria.vy + force_repuslion * math.sin(alpha)
                other_bacteria.x += other_bacteria.vx
                other_bacteria.y += other_bacteria.vy

            elif self.x >= other_bacteria.x and self.y <= other_bacteria.y:
                
                self.vx = self.vx - force_repuslion * math.cos(alpha)
                self.vy = self.vy + force_repuslion * math.sin(alpha)
                self.x += self.vx
                self.y += self.vy

                other_bacteria.vx = other_bacteria.vx + force_repuslion * math.cos(alpha)
                other_bacteria.y = other_bacteria.y - force_repuslion * math.sin(alpha)
                other_bacteria.x += other_bacteria.vx
                other_bacteria.y += other_bacteria.vy

            else:
                pass

        else:
            print('исключение!')
            print('координата x', self.x, other_bacteria.x)
            print('координата y', self.y, other_bacteria.y)
            pass


    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)

