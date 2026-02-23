class ScreenManager:
    def __init__(self):
        self._current = None
    
    def go_to(self, screen):
        self._current = screen
    
    def handle_event(self, event):
        if self._current:
            self._current.handle_event(event)
    
    def update(self):
        if self._current:
            self._current.update()
        
    def draw(self, surface):
        if self._current:
            self._current.draw(surface)