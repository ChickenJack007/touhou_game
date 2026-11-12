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
        self.bombs = 3

        self.can_shoot = True
        self.time_shot = 0
        self.shoot_timer = 100

    def update(self, dt):
        keys = py.key.get_pressed()
        if keys[py.K_UP]:
            if self.rect.top > 0:
                if keys[py.K_LSHIFT]:
                    if keys[py.K_RIGHT] or keys[py.K_LEFT]:
                        self.rect.y -= 200 * dt
                        self.hitbox.y -= 200 * dt
                    else:
                        self.rect.y -= 350 * dt
                        self.hitbox.y -= 350 * dt
                else:
                    if keys[py.K_RIGHT] or keys[py.K_LEFT]:
                        self.rect.y -= 400 * dt
                        self.hitbox.y -= 400 * dt
                    else:
                        self.rect.y -= 700 * dt
                        self.hitbox.y -= 700 * dt

        if keys[py.K_DOWN]:
            if self.rect.bottom < 900:
                if keys[py.K_LSHIFT]:
                    if keys[py.K_RIGHT] or keys[py.K_LEFT]:
                        self.rect.y += 200 * dt
                        self.hitbox.y += 200 * dt
                    else:
                        self.rect.y += 350 * dt
                        self.hitbox.y += 350 * dt
                else:
                    if keys[py.K_RIGHT] or keys[py.K_LEFT]:
                        self.rect.y += 400 * dt
                        self.hitbox.y += 400 * dt
                    else:
                        self.rect.y += 700 * dt
                        self.hitbox.y += 700 * dt

        if keys[py.K_LEFT]:
            if self.rect.left > 0:
                if keys[py.K_LSHIFT]:
                    if keys[py.K_UP] or keys[py.K_DOWN]:
                        self.rect.x -= 200 * dt
                        self.hitbox.x -= 200 * dt
                    else:
                        self.rect.x -= 350 * dt
                        self.hitbox.x -= 350 * dt
                else:
                    if keys[py.K_UP] or keys[py.K_DOWN]:
                        self.rect.x -= 400 * dt
                        self.hitbox.x -= 400 * dt
                    else:
                        self.rect.x -= 700 * dt
                        self.hitbox.x -= 700 * dt

        if keys[py.K_RIGHT]:
            if self.rect.right < 1280-500:
                if keys[py.K_LSHIFT]:
                    if keys[py.K_UP] or keys[py.K_DOWN]:
                        self.rect.x += 200 * dt
                        self.hitbox.x += 200 * dt
                    else:
                        self.rect.x += 350 * dt
                        self.hitbox.x += 350 * dt
                else:
                    if keys[py.K_UP] or keys[py.K_DOWN]:
                        self.rect.x += 400 * dt
                        self.hitbox.x += 400 * dt
                    else:
                        self.rect.x += 700 * dt
                        self.hitbox.x += 700 * dt

        if keys[py.K_z] and self.can_shoot:
            self.can_shoot = False
            Player_projectile(self.rect.midtop, self.group)
            self.time_shot = py.time.get_ticks()

        if keys[py.K_x] and self.bombs > 0:
            self.bombs -= 1

        if not self.can_shoot:
            if py.time.get_ticks() - self.time_shot >= self.shoot_timer:
                self.can_shoot = True

    def hit(self):
        self.lives -= 1
        if self.lives <= 0:
            self.kill()



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
    def __init__(self, groups, time_active=10, pos=(60, 60)):
        super().__init__(groups)
        self.image = py.image.load('./images/enemy1.png').convert_alpha()
        self.rect = self.image.get_frect(center = pos)
        self.time_active = time_active * 1000
        self.group = groups

        self.spawn_time = py.time.get_ticks()
        self.can_shoot = False
        self.time_shot = py.time.get_ticks()
        self.shoot_timer = 2000


    def update(self, dt):
        if py.time.get_ticks() - self.spawn_time >= self.time_active:
            self.kill()
        if not self.can_shoot:
            if py.time.get_ticks() - self.time_shot >= self.shoot_timer:
                self.can_shoot = True
        if self.can_shoot:
            self.can_shoot = False
            self.shoot(dt)

    def shoot(self, dt):
        self.time_shot = py.time.get_ticks()
        Enemy_1_projectile(self.group, self.rect.midbottom)


class Enemy_1_projectile(py.sprite.Sprite):
    def __init__(self, groups, pos):
        super().__init__(groups)
        self.image = py.image.load('./images/Enemy_1_projectile.png').convert_alpha()
        self.rect = self.image.get_frect(midtop = pos)

    def update(self, dt):
        if self.rect.top >= 900:
            self.kill()
        self.rect.y += 200 * dt


