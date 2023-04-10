import random
import pygame
import globalvars

class Amoeba(pygame.sprite.Sprite):
    def __init__(self, maturing_speed, x, y, hunger):
        super().__init__()
        self.image = pygame.Surface((10, 10)) 
        self.maturing_speed = maturing_speed
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect(center=(x, y))
        self.maturity = 0
        self.age = 0
        self.hunger = hunger

    def update(self):
        if self.rect.left <= 0:
            direction = 1
        elif self.rect.right >= globalvars.screen_width:
            direction = 2
        elif self.rect.top <= 0:
            direction = 3
        elif self.rect.bottom >= globalvars.screen_height:
            direction = 4
        else:
            direction = random.randint(1, 4)

        if direction == 1:
            self.rect.move_ip(globalvars.speed, 0)
        elif direction == 2:
            self.rect.move_ip(-globalvars.speed, 0)
        elif direction == 3:
            self.rect.move_ip(0, globalvars.speed)
        elif direction == 4:
            self.rect.move_ip(0, -globalvars.speed)

        self.age = self.age + 1
        self.hunger = self.hunger - 2

        self.maturity = self.maturity + (self.maturing_speed/125)

        if (len(globalvars.sprites) > globalvars.maxsprites or self.hunger < 0 or self.age > globalvars.amoebadeathage) and (10 < len(globalvars.amoebas) > globalvars.maxsprites/4) :
            self.kill()
            

    @classmethod
    def collide(cls):
        mature_amoebas = pygame.sprite.Group()
        for amoeba in globalvars.amoebas:
            if amoeba.maturity >= 50:
                mature_amoebas.add(amoeba)
        
        collisions = pygame.sprite.groupcollide(mature_amoebas, mature_amoebas, False, False)
        for amoeba_1, collided_amoebas in collisions.items():
            for amoeba_2 in collided_amoebas:
                
                amoeba_1.maturity = 45
                amoeba_2.maturity = 45

                location_x = random.randint(1,globalvars.screen_width)
                location_y = random.randint(1, globalvars.screen_height)

                speed_low = min(
                    amoeba_1.maturing_speed, amoeba_2.maturing_speed) - globalvars.mutation_speed
                speed_high = max(
                    amoeba_1.maturing_speed, amoeba_2.maturing_speed) + globalvars.mutation_speed

                new_maturing_speed = random.randint(speed_low, speed_high)
                
                newamoeba = cls(new_maturing_speed, location_x,location_y, amoeba_1.hunger)
                globalvars.sprites.add(newamoeba)
                globalvars.amoebas.add(newamoeba)
                globalvars.num_collisions += 100
    
    
    def eat(cls):
        for sprite1 in globalvars.amoebas: 
            collided_sprites = pygame.sprite.spritecollide(sprite1, globalvars.plants, False)
            for sprite2 in collided_sprites:
                sprite1.hunger += sprite2.food
                sprite2.kill()
            