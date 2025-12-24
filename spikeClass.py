class spike():
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = 50
        self.height = 50
        self.image = pygame.image.load("SPIKE.png").convert_alpha()
        self.hitbox = pygame.Rect(self.x, self.y, self.width, self.height)

    def collisions(self, player):
        if self.hitbox.colliderect(player.hitbox):
            player.health = player.health - 1 
            player.x = 100
            player.y = 500  
