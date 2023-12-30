import pygame


class GameCollisions:

    @staticmethod
    def apply(char: pygame.sprite, collision_sprites: pygame.sprite.Group) -> bool:
        # noinspection PyTypeChecker
        if pygame.sprite.spritecollide(char, collision_sprites, False,
                                       pygame.sprite.collide_mask) or char.rect.top <= -60:
            return False
        return True
