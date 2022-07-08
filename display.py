class View():
    def __init__(self, screen, screen_width, screen_height, img, word):
        self.screen = screen
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.img = img
        self.word = word
    
    def render(self):
        self.screen.fill((0,0,0))

        self.screen.blit(self.img, ((self.screen_width/2) - 100, (self.screen_height/2) - 100))
