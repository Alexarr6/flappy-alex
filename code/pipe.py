import pygame
import random
from settings import *
from typing import List


class BodyPipeUp(pygame.sprite.Sprite):

    def __init__(self, groups: List[pygame.sprite.Group], x_pos: int, y_pos: int):
        super().__init__(groups)

        self.image = pygame.image.load('graphics/body_pipe_up.png').convert_alpha()
        self.rect = self.image.get_rect(midtop=(x_pos, y_pos))
        self.mask = pygame.mask.from_surface(self.image)

    def move(self):
        self.rect.x -= 4

    def update(self, dt):
        self.move()
        if self.rect.right <= -100:
            self.kill()


class BodyPipeDown(pygame.sprite.Sprite):

    def __init__(self, groups: List[pygame.sprite.Group], x_pos: int, y_pos: int):
        super().__init__(groups)

        self.image = pygame.image.load('graphics/body_pipe_down.png').convert_alpha()
        self.rect = self.image.get_rect(midbottom=(x_pos, y_pos))
        self.mask = pygame.mask.from_surface(self.image)

    def move(self):
        self.rect.x -= 4

    def update(self, dt):
        self.move()
        if self.rect.right <= -100:
            self.kill()


class HeadPipeUp(pygame.sprite.Sprite):

    def __init__(self, groups: List[pygame.sprite.Group], x_pos: int, y_pos: int):
        super().__init__(groups)

        self.image = pygame.image.load('graphics/head_pipe_up.png').convert_alpha()
        self.rect = self.image.get_rect(midtop=(x_pos, y_pos))
        self.mask = pygame.mask.from_surface(self.image)

    def move(self):
        self.rect.x -= 4

    def update(self, dt):
        self.move()
        if self.rect.right <= -100:
            self.kill()


class HeadPipeDown(pygame.sprite.Sprite):

    def __init__(self, groups: List[pygame.sprite.Group], x_pos: int, y_pos: int):
        super().__init__(groups)

        self.image = pygame.image.load('graphics/head_pipe_down.png').convert_alpha()
        self.rect = self.image.get_rect(midbottom=(x_pos, y_pos))
        self.mask = pygame.mask.from_surface(self.image)

    def move(self):
        self.rect.x -= 4

    def update(self, dt):
        self.move()
        if self.rect.right <= -100:
            self.kill()


def create_full_pipe(all_sprites: pygame.sprite.Group,
                     collision_sprites: pygame.sprite.Group,
                     x_pos_pipe: int,
                     y_pos_pipe_up: int,
                     y_pos_pipe_down: int):

    random_number = random.randint(1, 3)
    upper_pipe_size = 1 + random_number
    bottom_pipe_size = 1 + (3 - random_number)

    for _ in range(bottom_pipe_size):
        BodyPipeDown([all_sprites, collision_sprites], x_pos_pipe, y_pos_pipe_down)
        y_pos_pipe_down -= 30

    HeadPipeDown([all_sprites, collision_sprites], x_pos_pipe, y_pos_pipe_down)

    for _ in range(upper_pipe_size):
        BodyPipeUp([all_sprites, collision_sprites], first_x_pos_pipe, y_pos_pipe_up)
        y_pos_pipe_up += 30

    HeadPipeUp([all_sprites, collision_sprites], first_x_pos_pipe, y_pos_pipe_up)
