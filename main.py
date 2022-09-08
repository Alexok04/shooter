from pygame import *
from pygame import image as img
import random

cosmos = "back.jpg"
rocket = "rocket1.png"
bullet = 'bullet-36942_1280.png'
enemy = 'alien-6626454_1280.png'


class Picture(sprite.Sprite):
    def __init__(self, x, y, image, width, height):
        super().__init__()
        self.image = img.load(image)
        self.image = transform.scale(self.image, (width, height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def draw(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


class Player(Picture):
    def update(self):
        keys = key.get_pressed()
        if keys[K_RIGHT] and self.rect.x < 600:
            self.rect.x += 5
        if keys[K_LEFT] and self.rect.x > 0:
            self.rect.x -= 5

    def fire(self):
        ballet = Bullet(player.rect.centerx, player.rect.top, bullet, 20, 50)
        bullets.add(ballet)


class Bullet(Picture):
    def update(self):
        self.rect.y -= 15
        colisions = sprite.groupcollide(bullets, enemies, True, True)
        for bullet in bullets.copy():
            if bullet.rect.bottom <= 0:
                bullets.remove(bullet)
                print('1')

        if len(enemies) == 0:
            bullets.empty()
            add_enemies()


class UFO(Picture):
    def update(self):
        self.rect.y += random.randint(2, 3)


def add_enemies():
    for i in range(3):
        ufo = UFO(random.randint(0, 600), -100, enemy, 100, 50)
        enemies.add(ufo)


bullets = sprite.Group()
enemies = sprite.Group()

win_width = 700
win_height = 500
display.set_caption("Космические войны")
window = display.set_mode((win_width, win_height))
background = transform.scale(image.load(cosmos), (win_width, win_height))
clock = time.Clock()
FPS = 60

player = Player(275, 400, rocket, 100, 100)

game = True
while game:
    clock.tick(FPS)
    window.blit(background, (0, 0))
    player.draw()
    player.update()
    bullets.draw(window)
    bullets.update()
    enemies.update()
    enemies.draw(window)
    display.update()

    for i in event.get():
        if i.type == QUIT:
            game = False
        elif i.type == KEYDOWN:
            if i.key == K_SPACE:
                player.fire()