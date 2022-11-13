import pygame

pygame.init()
screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption('Towers')
icon = pygame.image.load('images/tower_icon.png')
pygame.display.set_icon(icon)
clock = pygame.time.Clock()

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
PURPLE = (128, 0, 128)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

MARGIN = 2
FPS = 60

screen.fill(PURPLE)
myfont = pygame.font.Font('Roboto-Regular.ttf', 16)

class Character:
    H = 50
    W = 30
    def __init__(self, power: int, position: tuple[int, int], color: tuple=RED, name: str=None) -> None:
        self.color = color
        if name:
            self.name = myfont.render(name, True, BLACK)
        else:
            self.name = name
        self.power = power
        self.position = position
    
    def collide(self, other) -> bool:
        return False

    def attack(self, other) -> None:
        pass

    def draw(self) -> None:
        x, y = self.position
        pygame.draw.rect(screen, self.color, (x, y, self.W, self.H))
        if self.name:
            w, _ = self.name.get_size()
            screen.blit(self.name, (x + self.W // 2 - w // 2, y + self.H + MARGIN))
        power = myfont.render(str(self.power), True, self.color)
        w, h = power.get_size()
        screen.blit(power, (x + self.W // 2 - w // 2, y - h - MARGIN))


hero = Character(10, (100, 100), color=GREEN, name='УБИЙЦА')
pygame.display.update()

while True:
    x, y = hero.position
    w, h = screen.get_size()
    step = 3
    if x < w - step - hero.W:
        x += step
    else:
        x = 0
    hero.position = (x, y)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    screen.fill(PURPLE)
    hero.draw()
    pygame.display.update()
    clock.tick(FPS)
