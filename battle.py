#!/usr/bin/python
# -*- coding:utf-8 -*-

__author__ = 'Ydface'

import pygame, sys, pygame.mixer
from pygame.locals import *
import mypygame
import game_ui.mission_ui
import random
import resource
import label
import util.node
import gamestate
import button
import attribute
import skill

screen = mypygame.screen

LayerButton = gamestate.LayerButton
LayerLabel = gamestate.LayerLabel
LayerUI = gamestate.LayerUI

count = 0


class ExitButton(button.Button):
    def __init__(self, father):
        rect = Rect(345, 500, 100, 50)
        image1 = resource.getImage("start_normal")
        image0 = resource.getImage("start_down")

        button.Button.__init__(self, rect, image1, image0, father)

    def mouse_hover_effect(self):
        if self.mouse_stance:
            x, y = pygame.mouse.get_pos()
            rect = Rect(x + 30, y + 30, 100, 50)
            view = label.LabelViewState(label.ViewForver)
            text1 = label.FontLabel(rect, view, 16, u"点击此处退出")
            self.father.layer_child[LayerLabel]["exit_tips"] = text1
        elif not self.mouse_stance and self.father.layer_child[LayerLabel].has_key("exit_tips"):
            del self.father.layer_child[LayerLabel]["exit_tips"]

    def click_up_effect(self):
        gamestate.current_ui = game_ui.mission_ui.UIGame()


class BattleUnit(button.Button, attribute.Attribute):
    def __init__(self, level, image, rect, father, target, type="monster"):
        button.Button.__init__(self, rect, image, resource.getImage("attribute"), father)
        attribute.Attribute.__init__(self)
        self.hp = 1000 + level * 100
        self.max_hp = self.hp
        self.attack = 100 + level * 20
        self.image = image
        self.rect = rect
        self.dead = False
        self.father = father
        self.speed = random.randint(30, 90)
        self.activeProcess = 0
        self.deadDraw = False
        self.attack_enable = False
        self.target = target
        self.type = type
        if type == "monster":
            self.skills = []
        else:
            self.skills = gamestate.player.skills
        self.skills_index = 0

    def draw_self(self):
        global count
        screen.blit(self.image, (self.rect[0], self.rect[1]))

        #绘制技能释放进度条
        if not self.dead and not self.father.end:
            pygame.draw.rect(screen, (255, 255, 0), (self.rect[0] + 69, self.rect[1] + 54, 100, 4))
            w = float(self.activeProcess) / self.speed * 100
            pygame.draw.rect(screen, (255, 0, 0), (self.rect[0] + 69, self.rect[1] + 54, w, 4))

            count += 1
            rect = Rect(self.rect[0] + 69 + 35, self.rect[1] + 48, 100, 4)
            view = label.LabelViewState(label.ViewTimer, 2)
            text = str(round(float(self.activeProcess) / self.speed, 2))
            text1 = label.FontLabel(rect, view, 12, text)
            self.father.layer_child[LayerLabel][str(count)] = text1

        #绘制血条,血值
        w = int(float(self.hp) / self.max_hp * 100)
        if w:
            pygame.draw.rect(screen, (255, 0, 0), (self.rect[0] + 69, self.rect[1] + 24, w, 8))

            my_font = pygame.font.Font("resource/msyh.ttf", 8)
            tx_hp = str(self.hp) + " / " + str(self.max_hp)
            hp_surface = my_font.render(tx_hp, True, (255, 255, 255))
            screen.blit(hp_surface, (self.rect[0] + 79, self.rect[1] + 23))

        if self.dead and not self.deadDraw:
            rect = Rect(self.rect[0] + 77, self.rect[1] + 3, 100, 50)
            view = label.LabelViewState(label.ViewForver)
            text1 = label.FontLabel(rect, view, 16, "Dead")
            self.father.layer_child[LayerLabel][str(count)] = text1
            self.deadDraw = True

    def click_up_effect(self):
        if self.type == "monster" and not self.dead:
            player = self.father.layer_child[LayerButton]["player"]
            player.target = self

    def update(self):
        self.activeProcess += 1
        if self.activeProcess > self.speed:
            self.activeProcess = 0
            self.attack_enable = True

        for s in self.skills:
            if s.cool_down > 0:
                s.cool_down -= 1

    def attack_target(self):
        if not self.target or self.target.dead:
            for m in self.father.layer_child[LayerButton]:
                monster = self.father.layer_child[LayerButton][m]
                if isinstance(monster, BattleUnit) and monster.type == "monster" and not monster.dead:
                    self.target = monster

        self.attack_enable = False

        global count
        count += 1
        damage = 0
        if not self.skills:
            damage = self.attack - self.target.defense
        else:
            if self.skills_index >= len(self.skills):
                self.skills_index = 0
            cur_skill = self.skills[0]
            if not cur_skill.cool_down:
                skill_effect = skill.SkillEffect(cur_skill.skill_id, cur_skill.level)
                damage = skill_effect.damage_value()
                self.skills_index += 1
                cur_skill.cool_down = random.randint(60, 180)
            else:
                damage = self.attack - self.target.defense

        self.target.hp -= damage
        if self.target.hp <= 0:
            self.target.hp = 0
        rect = Rect(self.target.rect[0] + 200, self.target.rect[1] + 30, 100, 50)
        view = label.LabelViewState(label.ViewTimer, 60, [0, -0.3])
        text = str(-damage)
        text1 = label.FontLabel(rect, view, 16, text)
        self.father.layer_child[LayerLabel][str(count)] = text1

        if self.target.hp <= 0:
            self.target.dead = True


class Battle(util.node.Node):
    def __init__(self, level):
        util.node.Node.__init__(self)
        num = random.randint(1, 2)

        self.end = False
        self.playerWin = False

        self.layer_child[LayerButton]["player"] = BattleUnit(gamestate.player.level, resource.getImage("header_line"), Rect(100, 360, 100, 50), self, None, "player")
        player = self.layer_child[LayerButton]["player"]
        for i in range(0, num):
            self.layer_child[LayerButton][str(i)] = BattleUnit(1, resource.getImage("header_line"), Rect(400, 20 + 80 * i, 100, 50), self, player)

        self.next_delay = 0


        self.layer_child[LayerButton]["exit"] = ExitButton(self)

    def update(self):
        player = self.layer_child[LayerButton]["player"]
        player.update()
        if not player.dead and player.attack_enable:
            player.attack_target()

        if not self.check_end():
            for unit in self.layer_child[LayerButton]:
                monster = self.layer_child[LayerButton][unit]
                if not isinstance(monster, BattleUnit) or monster.type != "monster" or monster.dead:
                    continue
                monster.update()
                if not monster.attack_enable:
                    continue
                monster.update()
                monster.attack_target()
                if self.check_end():
                    break
        else:
            self.next_delay += 1

            rect = Rect(200, 30, 100, 50)
            view = label.LabelViewState(label.ViewForver)
            text = str(60 - self.next_delay) + u"帧后返回"
            text1 = label.FontLabel(rect, view, 16, text)
            self.layer_child[LayerLabel]["return"] = text1

        if self.next_delay > 60:
            if self.playerWin:
                gamestate.current_ui = Battle(3)
            else:
                gamestate.current_ui = Battle(3) #game_ui.mission_ui.UIGame()

        #移除过期label显示
        for key in self.layer_child[LayerLabel].keys():
            view_state = self.layer_child[LayerLabel][key]
            if view_state.viewState.view == label.ViewTimer and not view_state.viewState.isView:
                del self.layer_child[LayerLabel][key]


    def check_end(self):
        if self.end:
            return self.end

        player_unit = self.layer_child[LayerButton]["player"]
        if player_unit.hp <= 0:
            self.end = True

            rect = Rect(40, 30, 100, 50)
            view = label.LabelViewState(label.ViewForver)
            text1 = label.FontLabel(rect, view, 16, "You Dead")
            self.layer_child[LayerLabel]["result"] = text1

        else:
            for unit in self.layer_child[LayerButton]:
                monster = self.layer_child[LayerButton][unit]
                if isinstance(monster, BattleUnit) and not monster.dead and unit != "player":
                    return False
            self.end = True
            self.playerWin = True

            gamestate.player.add_exp(1)

            rect = Rect(40, 30, 100, 50)
            view = label.LabelViewState(label.ViewForver)
            text1 = label.FontLabel(rect, view, 16, "You Win")
            self.layer_child[LayerLabel]["result"] = text1

        return self.end

