import sys, pygame

pygame.init()

WIDTH, HEIGHT = 240, 320
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
CLOCK = pygame.time.Clock()

BG = pygame.image.load("assets/background.png")
BG_POS = BG.get_rect(center=(WIDTH/2, HEIGHT/2))

FONT = pygame.font.Font("assets/IS-Reg.ttf", 30)

labels = ["ALARM", "POMODORO", "MUSIC"]
rendered_texts = [FONT.render(text, True, "white") for text in labels]

total_height = sum(t.get_height() for t in rendered_texts) + (15 * (len(labels) - 1))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    SCREEN.blit(BG, BG_POS)
    current_y = (HEIGHT - total_height) // 2

    for surface in rendered_texts:
        x_pos = (WIDTH - surface.get_width()) // 2
        SCREEN.blit(surface, (x_pos, current_y))
        current_y += surface.get_height() + 15

    pygame.display.flip()

    CLOCK.tick(60)