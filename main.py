import sys, pygame
from datetime import datetime
pygame.init()

from core.constants import WIDTH, HEIGHT, FPS
from core import assets
assets.load()

from core import ScreenManager
from screens import HomeScreen

SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
CLOCK = pygame.time.Clock()

manager = ScreenManager()
manager.go_to(HomeScreen(manager))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        manager.handle_event(event)

    manager.update()
    manager.draw(SCREEN)

    current_time = datetime.now().strftime("%I:%M %p")
    rendered_time = assets.FONT_R_M.render(current_time, True, "white")
    time_pos_w = WIDTH - rendered_time.get_width() // 2 - 5
    time_pos_h = rendered_time.get_height() // 2
    time_rect = rendered_time.get_rect(center=(time_pos_w, time_pos_h))

    SCREEN.blit(rendered_time, time_rect)

    pygame.display.flip()

    CLOCK.tick(FPS)