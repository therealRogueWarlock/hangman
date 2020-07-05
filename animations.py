from pirple.hangman import load_sprits as sprits
import pygame
clock = pygame.time.Clock()


def animation_1(win):
    for frame in sprits.animation1:
        clock.tick(60)
        win.blit(frame, (0, 0))
        pygame.display.update()


def animation_2(win):
    for frame in sprits.animation2:
        clock.tick(30)
        win.blit(frame, (0, 0))
        pygame.display.update()


def animation_3(win):
    for frame in sprits.animation3:
        clock.tick(30)
        win.blit(frame, (0, 0))
        pygame.display.update()


def animation_4(win):
    for frame in sprits.animation4:
        clock.tick(30)
        win.blit(frame, (0, 0))
        pygame.display.update()


def animation_5(win):
    for frame in sprits.animation5:
        clock.tick(30)
        win.blit(frame, (0, 0))
        pygame.display.update()


def animation_6(win):
    for frame in sprits.animation6:
        clock.tick(30)
        win.blit(frame, (0, 0))
        pygame.display.update()


def animation_7(win):
    for frame in sprits.animation7:
        clock.tick(30)
        win.blit(frame, (0, 0))
        pygame.display.update()


all_animations = [animation_1, animation_2, animation_3, animation_4, animation_5, animation_6, animation_7]