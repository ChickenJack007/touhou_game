import pygame as py
from scripts.sprites import Player, Enemy_1


py.init()
screen = py.display.set_mode((1280, 900))
clock = py.time.Clock()
dt = 0
running = True
score = 0

player_sprites = py.sprite.Group()
player = Player(player_sprites)

enemy_sprites = py.sprite.Group()
enemy1 = Enemy_1(enemy_sprites, 15, (200, 200))
while running:
    screen.fill("#7090f0")

    py.draw.rect(screen, "#1f1f1f", (1280-500, 0, 500, 900))






    enemy_sprites.update(dt)
    enemy_sprites.draw(screen)


    player_sprites.update(dt)
    player_sprites.draw(screen)


    if py.key.get_pressed()[py.K_LSHIFT]:
        py.draw.rect(screen, "white", player.hitbox)
















    for event in py.event.get():
        if event.type == py.QUIT:
            running = False

    dt = clock.tick() / 1000
    py.display.update()

py.quit()
