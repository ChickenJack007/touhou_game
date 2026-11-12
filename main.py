import pygame as py
class Player(py.sprite.Sprite):
    def __init__(self, groups):
        super().__init__(groups)
        self.image = py.image.load('./images/player.png').convert_alpha()
        self.rect = self.image.get_frect(center = (1280 / 2, 900 / 2))
        self.group = groups

        self.hitbox = self.rect.inflate(-70, -80)
        self.hitbox.x += 7
        self.hitbox.y += 15

        self.lives = 3

        self.can_shoot = True
        self.time_shot = 0
        self.shoot_timer = 100

    def update(self, dt):
        keys = py.key.get_pressed()
        if keys[py.K_UP]:
            if self.rect.top > 0:
                if keys[py.K_LSHIFT]:
                    if keys[py.K_RIGHT] or keys[py.K_LEFT]:
                        self.rect.y -= 250 * dt
                        self.hitbox.y -= 250 * dt
                    else:
                        self.rect.y -= 400 * dt
                        self.hitbox.y -= 400 * dt
                else:
                    if keys[py.K_RIGHT] or keys[py.K_LEFT]:
                        self.rect.y -= 500 * dt
                        self.hitbox.y -= 500 * dt
                    else:
                        self.rect.y -= 800 * dt
                        self.hitbox.y -= 800 * dt

        if keys[py.K_DOWN]:
            if self.rect.bottom < 900:
                if keys[py.K_LSHIFT]:
                    if keys[py.K_RIGHT] or keys[py.K_LEFT]:
                        self.rect.y += 250 * dt
                        self.hitbox.y += 250 * dt
                    else:
                        self.rect.y += 400 * dt
                        self.hitbox.y += 400 * dt
                else:
                    if keys[py.K_RIGHT] or keys[py.K_LEFT]:
                        self.rect.y += 500 * dt
                        self.hitbox.y += 500 * dt
                    else:
                        self.rect.y += 800 * dt
                        self.hitbox.y += 800 * dt

        if keys[py.K_LEFT]:
            if self.rect.left > 0:
                if keys[py.K_LSHIFT]:
                    if keys[py.K_UP] or keys[py.K_DOWN]:
                        self.rect.x -= 250 * dt
                        self.hitbox.x -= 250 * dt
                    else:
                        self.rect.x -= 400 * dt
                        self.hitbox.x -= 400 * dt
                else:
                    if keys[py.K_UP] or keys[py.K_DOWN]:
                        self.rect.x -= 500 * dt
                        self.hitbox.x -= 500 * dt
                    else:
                        self.rect.x -= 800 * dt
                        self.hitbox.x -= 800 * dt

        if keys[py.K_RIGHT]:
            if self.rect.right < 1280:
                if keys[py.K_LSHIFT]:
                    if keys[py.K_UP] or keys[py.K_DOWN]:
                        self.rect.x += 250 * dt
                        self.hitbox.x += 250 * dt
                    else:
                        self.rect.x += 400 * dt
                        self.hitbox.x += 400 * dt
                else:
                    if keys[py.K_UP] or keys[py.K_DOWN]:
                        self.rect.x += 500 * dt
                        self.hitbox.x += 500 * dt
                    else:
                        self.rect.x += 800 * dt
                        self.hitbox.x += 800 * dt

        if keys[py.K_z] and self.can_shoot:
            Player_projectile(self.rect.midtop, self.group)
            self.can_shoot = False
            self.time_shot = py.time.get_ticks()

        if not self.can_shoot:
            if py.time.get_ticks() - self.time_shot >= self.shoot_timer:
                self.can_shoot = True


class Player_projectile(py.sprite.Sprite):
    def __init__(self, pos, groups):
        super().__init__(groups)
        self.image = py.image.load('./images/projectile.png').convert_alpha()
        self.rect = self.image.get_frect(midbottom = pos)

    def update(self, dt):
        self.rect.centery -= 1200 * dt
        if self.rect.bottom < 0:
            self.kill()

class Enemy_1(py.sprite.Sprite):
    def __init__(self, groups, time_active=10000, pos):
        super().__init__(groups)
        self.image = ""
        self.rect = self.image.get_frect(center = pos)
        self.time_active = time_active

        self.spawn_time = py.time.get_ticks()
        self.can_shoot = False
        self.time_shot = py.time.get_ticks()
        self.shoot_timer = 2000


    def update(self, dt):
        if py.time.get_ticks() - self.spawn_time >= self.time_active:
            self.kill()
        if not can_shoot:
            if py.time.get_ticks() - self.time_shot >= self.shoot_timer:
                self.can_shoot = True
        else:
            shoot()

    def shoot(self, dt):
        pass

class Enemy_1_projectile(py.sprite.Sprite):
    def __init__(self, groups):
        super().__init__(groups)
        self.image = ""
        self.rect = ""


py.init()
screen = py.display.set_mode((1280, 900))
clock = py.time.Clock()
dt = 0
running = True

player_sprites = py.sprite.Group()
player = Player(player_sprites)

while running:
    screen.fill("#1f1f1f")

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
