import pygame


class Background(pygame.sprite.Sprite):

    def __init__(self, groups: pygame.sprite.Group):

        super().__init__(groups)

        self.image = pygame.image.load('graphics/sky.png').convert()
        self.rect = self.image.get_rect(bottomleft=(0, 370))
