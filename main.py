import pygame as py
from scripts.sprites import Player, Enemy_1


show_hitbox = False
py.init()
screen = py.display.set_mode((1280, 900))
clock = py.time.Clock()
dt = 0
running = True
score = 0

player_sprites = py.sprite.Group()
player = Player(player_sprites)

enemy_projectiles = py.sprite.Group()
enemy_sprites = py.sprite.Group()
enemy1 = Enemy_1(enemy_sprites, enemy_projectiles, 15, (200, 200))
enemy1 = Enemy_1(enemy_sprites, enemy_projectiles, 15, (400, 200))
while running:
    screen.fill("#7090f0")



    player_sprites.update(dt)
    player_sprites.draw(screen)

    enemy_sprites.update(dt)
    enemy_projectiles.update(dt)
    if show_hitbox:
        for sprite in enemy_sprites:
            py.draw.rect(screen, "white", sprite.hitbox)
        for sprite in enemy_projectiles:
            py.draw.rect(screen, "white", sprite.hitbox)
        for sprite in player_sprites:
            py.draw.rect(screen, "white", sprite.rect)
    enemy_sprites.draw(screen)
    enemy_projectiles.draw(screen)




    if py.key.get_pressed()[py.K_LSHIFT]:
        py.draw.rect(screen, "white", player.hitbox)


    py.draw.rect(screen, "#1f1f1f", (1280-500, 0, 500, 900))
    for event in py.event.get():
        if event.type == py.QUIT:
            running = False

    dt = clock.tick() / 1000
    py.display.update()

py.quit()
