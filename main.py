import math
import time
import pygame
import os
import random
import json
from assets.managers import common, entity
from assets.managers import constants
from assets.managers import ai
from assets.managers import menus
from assets.managers import items
from assets.managers import projectile
from assets.managers import level, cutscene
from util.logging import *


def abs(num):
    if num < 0:
        num *= -1
    return num


def align_to_grid(pos):
    pos[0] = int(pos[0]/constants.BLOCK_SIZE)*constants.BLOCK_SIZE
    pos[1] = int(pos[1]/constants.BLOCK_SIZE)*constants.BLOCK_SIZE
    return pos


def draw():
    constants.WIN.fill((48, 48, 48))
    common.loaded_level.hud.fill((0, 0, 0, 255))
    common.loaded_level.update_camera()

    for i in common.enemies:
        if i != None:
            i.Animation(i)

    for i in common.projectiles:
        if i != None:
            i.draw()

    for i in common.particles:
        if i != None:
            i.draw()

    for box in common.boxes:
        box.Draw()

    constants.WIN.blit(common.loaded_level.display_texture, (0, 0))
    if common.player.overlay_active:
        constants.WIN.blit(common.player.overlay, (common.player.x -
                           (constants.CAM_WIDTH*1.5)-1, common.player.y-(constants.CAM_HEIGHT*1.5)))
    
    for i in common.level_transitions:
        pygame.draw.rect(constants.WIN, (128, 128, 128), i.rect)

    common.player.Draw()

    if common.active_text != None:
        common.active_text.update()

    pygame.transform.scale(common.loaded_level.camera_surface, (constants.WIDTH *
                           constants.screen_scale, constants.HEIGHT*constants.screen_scale), constants.disp_win)

    common.Font("nova", pygame.Rect((constants.screen_scale, 13 *
                constants.screen_scale, 8, 30)), "fps: "+str(common.tick)+" ")

    constants.disp_win.blit(common.loaded_level.hud, (0, 0))

    pygame.display.update()


def main():
    clock = pygame.time.Clock()
    isRunning = True
    tick = 0

    common.loaded_level = level.Level()
    common.player = entity.Entity("player", "player")
    common.player.texture_size = [4, 8]
    common.player.hitbox = pygame.Rect(0, 0, 8, 16)
    common.e = cutscene.TextSequence([cutscene.TextElement("press^kwto jump", common.player, "happy"), 90, cutscene.TextElement(
        "\ngo on, press^kw", common.player, "neutral")], 1, size=2)
    common.ReloadSettings()

    info("Loaded assets, starting render loop")

    while isRunning:
        clock.tick(constants.FPS)
        tick += 1
        if time.time() > common.realclock+1:
            common.tick = tick
            tick = 0
            common.realclock = time.time()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                isRunning = False
                break
        pygame.event.clear()
        if common.menu == None:
            menus.menu_ticks.Trigger()
            common.player.AIpointer(common.player)
            for i in common.enemies:
                if i != None:
                    i.AIpointer(i)
            for i in common.projectiles:
                if i != None:
                    i.update()
            for i in common.level_transitions:
                i.check()
            for i in common.particle_spawners:
                i.spawn_particles()
            draw()
        else:
            menus.menu_ticks.Tick()
            if common.menu == "main":
                menus.title()
            elif common.menu == "pause":
                menus.pause()
            constants.disp_win.blit(constants.menu_surface, (0, 0))
            pygame.display.update()
    json.dump(common.Settings, open("settings", "w"), indent=4)
    info("Game quit without errors")
    pygame.quit()


if __name__ == "__main__":
    main()
