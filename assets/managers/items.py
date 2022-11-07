import pygame, random, os
from assets.managers import constants, projectile, common

class Item():
    def __init__(self, id, type, texture, on_use, cooldown):
        self.id = id
        self.type = type
        self.cooldown = cooldown
        self.texture = pygame.image.load(
            os.path.join(constants.ITEM_PATH, texture))
        self.texture = pygame.transform.scale(self.texture, (self.texture.get_width(
        )*constants.screen_scale, self.texture.get_height()*constants.screen_scale))
        self.on_use = on_use


def basic(self):
    spread = random.randint(-2, 2)
    if not self.cooldown.active:
        self.cooldown.Trigger()
        projectile.new_projectile(projectile.Bullet(
            common.player.x, common.player.y, common.player.angle+spread, "bullet.png", 10, 1, 0, 3))


def gun2(self):
    spread = random.randint(-7, 7)
    if not self.cooldown.active:
        self.cooldown.Trigger()
        projectile.new_projectile(projectile.Bullet(
            common.player.x, common.player.y, common.player.angle+spread, "bullet.png", 3, 1, 0, 3))


registry = {}
registry.update({"gun": Item(basic, "gun", "gun.png", basic, common.Ticker(30))})
registry.update({"gun2": Item(gun2, "gun", "gun.png", basic, common.Ticker(40))})
