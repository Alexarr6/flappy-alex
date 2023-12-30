import pygame


class GameScore:

    @staticmethod
    def display(font: pygame.font.Font, screen: pygame.display.set_mode, start_time: int) -> str:
        current_time = pygame.time.get_ticks() - start_time
        game_score = str(int(current_time / 1000))
        score_surf = font.render('Score: ' + game_score, False, (0, 0, 0))
        score_rect = score_surf.get_rect(center=(600, 70))
        screen.blit(score_surf, score_rect)
        return game_score
