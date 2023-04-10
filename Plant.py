import random
import pygame
import globalvars


class Plant(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.width = 5
        self.height = 5
        self.image = pygame.Surface((self.width, self.height))
        self.image.fill((0, 255, 0))
        self.rect = self.image.get_rect(center=(x, y))
        self.age = 0
        self.food = 10

    def update(self):
        self.age += 1
        self.food += 1

        self.width += 2
        self.height += 2
        self.rect.move_ip(-1, -1)

        if random.randint(1, 10) == 1:
            location_x = self.rect.left + random.randint(-30, 40)
            location_y = self.rect.top + random.randint(-30, 40)
            newplant = Plant(location_x, location_y)
            globalvars.sprites.add(newplant)
            globalvars.plants.add(newplant)

        self.image = pygame.Surface((self.width, self.height))
        self.image.fill((0, 255, 0))

        if self.age > random.randint(20, 80):
            location_x = self.rect.left + random.randint(-30, 40)
            location_y = self.rect.top + random.randint(-30, 40)
            newplant = Plant(location_x, location_y)
            globalvars.sprites.add(newplant)
            globalvars.plants.add(newplant)
            self.kill()

        if self.rect.left <= 0:
            self.rect.left = random.randint(1, globalvars.screen_width)
        elif self.rect.right >= globalvars.screen_width:
            self.rect.right = random.randint(1, globalvars.screen_width)
        elif self.rect.top <= 0:
            self.rect.top = random.randint(1, globalvars.screen_height)
        elif self.rect.bottom >= globalvars.screen_height:
            self.rect.bottom = random.randint(1, globalvars.screen_height)

        if (len(globalvars.sprites) > globalvars.maxsprites or self.age > globalvars.plantdeathage) and (globalvars.maxsprites/4 < len(globalvars.plants) > 10):
            self.kill()
