import pygame
from core.constants import WIDTH, HEIGHT, MENU_GAP
from core import assets

LABELS = ["Alarm", "Pomodoro", "Music"]

class HomeScreen:
    def __init__(self, manager):
        self.manager = manager
        self.bg = pygame.image.load("assets/background.png")
        self.bg_pos = self.bg.get_rect(center=(WIDTH/2, HEIGHT/2))
        self.rendered = [assets.FONT_S_L.render(text, True, "white") for text in LABELS]
        self.total_height = sum(t.get_height() for t in self.rendered) + (MENU_GAP * (len(LABELS) - 1))

        # build a rect for each label so we can hit-test taps
        self.rects = []
        current_y = (HEIGHT - self.total_height) // 2
        for label in self.rendered:
            x = (WIDTH - label.get_width()) // 2
            rect = pygame.Rect(x, current_y, label.get_width(), label.get_height())
            self.rects.append(rect)
            current_y += label.get_height() + MENU_GAP
    
    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = event.pos  # works for both mouse and touch
            for i, rect in enumerate(self.rects):
                if rect.collidepoint(pos):
                    print(i)
    
    def update(self): pass

    def draw(self, surface):
        surface.blit(self.bg, self.bg_pos)        
        current_y = (HEIGHT - self.total_height) // 2

        for label in self.rendered:
            x_pos = (WIDTH - label.get_width()) // 2
            surface.blit(label, (x_pos, current_y))
            current_y += label.get_height() + MENU_GAP
