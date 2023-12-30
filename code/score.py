import pygame


def display_score(font: pygame.font.Font, screen: pygame.display.set_mode, start_time: int):
    current_time = pygame.time.get_ticks() - start_time
    score = str(int(current_time/1000))
    score_surf = font.render('Score: ' + score, False, (64, 64, 64))
    score_rect = score_surf.get_rect(center=(600, 70))
    pygame.draw.rect(screen, '#c0e8ec', score_rect)
    pygame.draw.rect(screen, '#c0e8ec', score_rect, 20)
    screen.blit(score_surf, score_rect)

    return score
