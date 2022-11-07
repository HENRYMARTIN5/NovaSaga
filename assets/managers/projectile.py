from assets.managers import constants, common
import math, pygame, os


def new_projectile(projectile):
    if len(common.projectiles) == 0:
        common.projectiles.append(projectile)
    else:
        for i in range(len(common.projectiles)):
            if common.projectiles[i] == None:
                projectile.index = i
                common.projectiles[i] = projectile
                break
            elif i == len(common.projectiles)-1:
                projectile.index = i+1
                common.projectiles.append(projectile)


class Bullet():
    def __init__(self, x, y, angle, texture, speed, damage, pierce=0, bounce=0, gravity=constants.DEF_GRAVITY/3):
        self.x = x
        self.y = y
        self.x_vel = math.cos(math.radians(angle))*speed
        self.y_vel = math.sin(math.radians(angle))*speed
        self.speed = speed
        self.texture = pygame.image.load(
            os.path.join(constants.PROJ_PATH, texture))
        #self.texture = pygame.transform.scale(self.texture,(self.texture.get_width()*constants.screen_scale,self.texture.get_height()*constants.screen_scale))
        self.index = 0
        self.damage = damage
        self.pierce = pierce
        self.bounce = bounce
        self.gravity = gravity
        self.damage_ticks = 0

    def kill(self):
        common.projectiles[self.index] = None

    def update(self):
        if self.y_vel > 10:
            self.y_vel = 10
        else:
            self.y_vel += self.gravity
        if self.x+self.x_vel < constants.WIN.get_width()-1 and self.y+self.y_vel < constants.WIN.get_height()-1 and self.x+self.x_vel > 1 and self.y+self.y_vel > 1:
            x_step = self.x_vel/self.speed
            y_step = self.y_vel/self.speed
            total_x = 0
            total_y = 0
            for i in range(self.speed):
                x = x_step*i+self.x
                y = y_step*i+self.y
                if common.loaded_level.collision.get_at((x, y)) == 1:
                    if common.loaded_level.collision.get_at((x, y+1)) == 1 and common.loaded_level.collision.get_at((x, y-1)) == 1:
                        x_step *= -1
                        self.x_vel = self.x_vel/2*-1
                    if common.loaded_level.collision.get_at((x+1, y)) == 1 and common.loaded_level.collision.get_at((x-1, y)) == 1:
                        y_step *= -1
                        self.y_vel *= -1
                        if self.y_vel < 0:
                            self.y_vel /= 2
                            y_step /= 2
                    if self.bounce <= 0:
                        self.kill()
                    self.bounce -= 1
                total_x += x_step
                total_y += y_step
            self.x += total_x
            self.y += total_y
        else:
            self.kill()
        for i in common.enemies:
            if i != None:
                if i.hitbox.collidepoint((self.x, self.y)):
                    i.damage(self.damage)
                    self.pierce -= 1
                    if self.pierce < 0:
                        self.kill()

    def draw(self):
        constants.WIN.blit(self.texture, (self.x-1, self.y-1))
