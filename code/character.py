import pygame


class Character(pygame.sprite.Sprite):

    def __init__(self, groups: pygame.sprite.Group):

        super().__init__(groups)

        self.image = pygame.transform.rotate(
            pygame.image.load('graphics/char.png').convert_alpha(), 290)
        self.rect = self.image.get_rect(center=(150, 200))

        self.pos = pygame.math.Vector2(self.rect.topleft)
        self.player_gravity = 800
        self.direction = 0
        self.mask = pygame.mask.from_surface(self.image)

    def apply_gravity(self, dt):
        self.direction += self.player_gravity * dt
        self.pos.y += self.direction * dt
        self.rect.y = round(self.pos.y)

    def jump(self):
        self.direction = -350

    def animate(self):

        self.image = pygame.transform.rotate(
            pygame.image.load('graphics/char.png').convert_alpha(), 290)

    def dead(self, x: int, y: int):
        image = pygame.transform.rotate(
            pygame.image.load('graphics/dead_char.png').convert_alpha(), 290)
        self.image = pygame.transform.rotozoom(image, -self.direction * 0.1, 1)
        self.rect = self.image.get_rect(topleft=(x, y))

    def rotate(self):
        rotated_char = pygame.transform.rotozoom(self.image, -self.direction * 0.1, 1)
        self.image = rotated_char
        self.mask = pygame.mask.from_surface(self.image)

    def update(self, dt):
        self.apply_gravity(dt)
        self.animate()
        self.rotate()
