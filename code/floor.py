import pygame
from typing import List


class Floor(pygame.sprite.Sprite):

    def __init__(self, groups: List[pygame.sprite.Group]):

        super().__init__(groups)

        self.image = pygame.image.load('graphics/floor.png').convert_alpha()
        self.rect = self.image.get_rect(topleft=(0, 370))
        self.mask = pygame.mask.from_surface(self.image)
