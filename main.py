import pygame as py

class Player(py.sprite.Sprite):
    def __init__(self, groups):
        super().__init__(groups)
        self.image = py.image.load('./images/player.png').convert_alpha()
        self.rect = self.image.get_frect(center = (1280 / 2, 900 / 2))
        self.group = groups

        self.can_shoot = True
        self.time_shot = 0
        self.shoot_timer = 100

    def update(self, dt):
        keys = py.key.get_pressed()
        if keys[py.K_UP]:
            if self.rect.top > 0:
                if keys[py.K_RIGHT] or keys[py.K_LEFT]:
                    self.rect.y -= 500 * dt
                else:
                    self.rect.y -= 800 * dt
        if keys[py.K_DOWN]:
            if self.rect.bottom < 900:
                if keys[py.K_RIGHT] or keys[py.K_LEFT]:
                    self.rect.y += 500 * dt
                else:
                    self.rect.y += 800 * dt
        if keys[py.K_LEFT]:
            if self.rect.left > 0:
                if keys[py.K_UP] or keys[py.K_DOWN]:
                    self.rect.x -= 500 * dt
                else:
                    self.rect.x -= 800 * dt
        if keys[py.K_RIGHT]:
            if self.rect.right < 1280:
                if keys[py.K_UP] or keys[py.K_DOWN]:
                    self.rect.x += 500 * dt
                else:
                    self.rect.x += 800 * dt

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
    def __init__(self, groups):
        super().__init__(groups)
        self.image = ""
        self.rect = ""

    def update(self, dt):
        pass


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

    for event in py.event.get():
        if event.type == py.QUIT:
            running = False
    dt = clock.tick() / 1000
    py.display.update()

py.quit()
