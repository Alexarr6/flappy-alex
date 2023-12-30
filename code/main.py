import time
from sys import exit
import pygame

from background import Background
from character import Character
from floor import Floor
from pipe import create_full_pipe
from settings import *
from score import GameScore
from collisions import GameCollisions

pygame.init()

screen = pygame.display.set_mode((screen_length, screen_height))
pygame.display.set_caption('Flappy Alex')
clock = pygame.time.Clock()

all_sprites = pygame.sprite.Group()
collision_sprites = pygame.sprite.Group()

Background(all_sprites)
Floor([all_sprites, collision_sprites])
char = Character(all_sprites)

font = pygame.font.Font('font/Pixeltype.ttf', 70)
game_message_surf = font.render('Press key to start...', False, (0, 0, 0))
game_message_rect = game_message_surf.get_rect(center=(400, 100))

# timer
obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer, 1400)

game_active = False
start_time = 0
score = '0'
last_time = time.time()

game_score = GameScore()
game_collisions = GameCollisions()

while True:

    dt = time.time() - last_time
    last_time = time.time()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if event.type == obstacle_timer and game_active:
            create_full_pipe(all_sprites,
                             collision_sprites,
                             first_x_pos_pipe,
                             first_y_pos_pipe_up,
                             first_y_pos_pipe_down)

    if game_active:

        game_active = game_collisions.apply(char, collision_sprites)
        all_sprites.draw(screen)
        all_sprites.update(dt)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            char.jump()

        score = game_score.display(font, screen, start_time)

    else:

        menu_time = pygame.time.get_ticks()
        char.dead(char.rect.topleft[0], char.rect.topleft[1])
        all_sprites.draw(screen)

        game_score_surf = font.render('You get a score of: ' + score, False, (0, 0, 0))
        game_score_rect = game_score_surf.get_rect(center=(400, 300))
        pygame.draw.rect(screen, '#c0e8ec', game_score_rect)
        pygame.draw.rect(screen, '#c0e8ec', game_score_rect, 20)
        screen.blit(game_score_surf, game_score_rect)

        if int(str(menu_time)[-3:]) < 900:
            screen.blit(game_message_surf, game_message_rect)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:

            for sprite in collision_sprites.sprites():
                sprite.kill()
            char.kill()
            char = Character(all_sprites)
            Floor([all_sprites, collision_sprites])
            game_active = True
            start_time = pygame.time.get_ticks()

    pygame.display.update()
    clock.tick(60)
