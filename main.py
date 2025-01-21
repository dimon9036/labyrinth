import pygame
pygame.init() 
from map1 import *

FPS = 60

win_width, win_height = 700, 500

window = pygame.display.set_mode((win_width, win_height))

timer = pygame.time.Clock()

background = pygame.image.load("photo-1700901555562-952f0008a11f.jpeg")

background = pygame.transform.scale(background, (win_width, win_height))

pygame.display.set_caption("Лабіринт")

pygame.mixer.music.load("jungles.ogg")
pygame.mixer.music.set_volume(0.2)
pygame.mixer.music.play(-1)


class Sprite:
    def __init__(self, x, y, w, h, image):
        self.rect = pygame.Rect(x, y, w, h)
        image = pygame.transform.scale(image, (w, h))
        self.image = image

    def draw(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


class Player(Sprite):
    def __init__(self, x, y, w, h, image, speed):
        super().__init__(x, y, w, h, image)
        self.speed = speed
    def move(self, a, d, s, w):
        keys = pygame.key.get_pressed()
        if keys[a]:
            if self.rect.x > 0:
                self.rect.x -= self.speed
        if keys[d]:
            if self.rect.right < win_width:
                self.rect.x += self.speed
        if keys[w]:
            if self.rect.y > 0:
                self.rect.y -= self.speed
        if keys[s]:
            if self.rect.bottom < win_height:
                self.rect.y += self.speed

blocks = []
block_size = 25

block_x = 0
block_y = 0
block_image = pygame.image.load("6407951eb8df3.png")


class Enemy(Sprite):
    def __init__(self, x, y, w, h, image1, image2, speed, x2, direction = "right"):
        super().__init__(x, y, w, h, image1)
        self.image1 = self.image
        self.image2 =pygame.transform.scale(image2, (w, h))
        self.speed = speed
        self.x1 = 375
        self.x2 = x2
        self.direction = direction

    def move(self):
        if self.rect.x >= self.x2:
            self.rect.x == self.x2
            self.direction = "left"
            self.image = self.image2
        elif self.rect.x <= self.x1:
            self.rect.x = self.x1
            self.direction = "right"
            self.image = self.image1
        if self.direction == 'right':
            self.rect.x += self.speed
        else:
            self.rect.x -= self.speed           

    


img_gold = pygame.image.load("buried-pirates-treasure-chest-157583040-5b5630f7c9e77c005b40d079.jpg")

for row in lvl1:
    for tile in row:
        if tile == "1":
            blocks.append(Sprite(block_x, block_y, block_size, block_size, block_image))
        elif tile == "2":
            treasure = Sprite(block_x, block_y, 50, 50, img_gold)
        block_x += block_size  
    block_x = 0
    block_y += block_size


player1 = Player(0, 0, 50, 50, pygame.image.load("sprite1.png"), 2)


enemy_img1 = pygame.image.load("eeace5f9be1598d049e913e0254adda5.gif")
enemy_img2 = pygame.transform.flip(enemy_img1, True, False)

enemy1 = Enemy(375, 375, 50, 50, enemy_img1, enemy_img2, 3, 650)

font = pygame.font.SysFont("Arial", 70, )
lose = font.render("You lose!", True, (255, 0, 0))
win = font.render("You won!", True, (0, 255, 0))

game = True
finish = False

while game:
    if not finish:
        window.blit(background, (0, 0))
        treasure.draw()

        for b in blocks:
            b.draw()

        player1.draw()
        player1.move(pygame.K_a, pygame.K_d, pygame.K_s, pygame.K_w)
        enemy1.draw()
        enemy1.move()

        for b in blocks:
            if player1.rect.colliderect(b.rect):
                window.blit(lose, (50, 100))
                finish = True
                pygame.mixer.music.stop()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and finish:
            player1 = Player(0, 0, 50, 50, pygame.image.load("sprite1.png"), 2)
            finish = False


    pygame.display.update()
    timer.tick(FPS)

pygame.time.delay(50)