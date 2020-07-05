import pygame

# loading sprits
main_page = \
    pygame.image.load("C:/Users/Sander/PycharmProjects/HalloWorld/pirple/hangman/hangman_sprits/hangman_page.png")


#  displaying a static sprit at different stages of the game.
static_sprits = []
for n in range(1, 8):
    static_sprits.append(pygame.image.load(f'C:/Users/Sander/PycharmProjects/HalloWorld/pirple/hangman/hangman_sprits'
                                           f'/static/static{n}.png'))


# animation 1. Animation at start, drawing gallows.
animation1 = []
for n in range(1, 66):
    animation1.append(pygame.image.load(f'C:/Users/Sander/PycharmProjects/HalloWorld/pirple/hangman/hangman_sprits'
                                        f'/animation1/animation1_{n}.png'))


# animation 2-7. Animation hangman
# animation 2.
animation2 = []
for n in range(1, 19):
    animation2.append(pygame.image.load(f'C:/Users/Sander/PycharmProjects/HalloWorld/pirple/hangman/hangman_sprits'
                                        f'/animation2/animation2_{n}.png'))


# animation 3
animation3 = []
for n in range(1, 7):
    animation3.append(pygame.image.load(f'C:/Users/Sander/PycharmProjects/HalloWorld/pirple/hangman/hangman_sprits'
                                        f'/animation3/animation3_{n}.png'))


# animation 4
animation4 = []
for n in range(1, 7):
    animation4.append(pygame.image.load(f'C:/Users/Sander/PycharmProjects/HalloWorld/pirple/hangman/hangman_sprits'
                                        f'/animation4/animation4_{n}.png'))


# animation 5
animation5 = []
for n in range(1, 8):
    animation5.append(pygame.image.load(f'C:/Users/Sander/PycharmProjects/HalloWorld/pirple/hangman/hangman_sprits'
                                        f'/animation5/animation5_{n}.png'))

# animation 6
animation6 = []
for n in range(1, 4):
    animation6.append(pygame.image.load(f'C:/Users/Sander/PycharmProjects/HalloWorld/pirple/hangman/hangman_sprits'
                                        f'/animation6/animation6_{n}.png'))


# animation 7
animation7 = []
for n in range(1, 5):
    animation7.append(pygame.image.load(f'C:/Users/Sander/PycharmProjects/HalloWorld/pirple/hangman/hangman_sprits'
                                        f'/animation7/animation7_{n}.png'))


# alphabet animations.

animation_a = []
for n in range(1, 11):
    animation_a.append(pygame.image.load(f'C:/Users/Sander/PycharmProjects/HalloWorld/pirple/hangman/hangman_sprits'
                                         f'/alpabet/a/a_{n}.png'))

animation_b = []
for n in range(1, 14):
    animation_b.append(pygame.image.load(f'C:/Users/Sander/PycharmProjects/HalloWorld/pirple/hangman/hangman_sprits'
                                         f'/alpabet/b/b_{n}.png'))

animation_c = []
for n in range(1, 11):
    animation_c.append(pygame.image.load(f'C:/Users/Sander/PycharmProjects/HalloWorld/pirple/hangman/hangman_sprits'
                                         f'/alpabet/c/c_{n}.png'))

animation_d = []
for n in range(1, 13):
    animation_d.append(pygame.image.load(f'C:/Users/Sander/PycharmProjects/HalloWorld/pirple/hangman/hangman_sprits'
                                         f'/alpabet/d/d_{n}.png'))


static_letters = {}
for letter in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'æ', 'ø', 'å']:
    static_letters[letter] = (pygame.image.load(f'C:/Users/Sander/PycharmProjects/HalloWorld/pirple/hangman'
                                            f'/hangman_sprits/alpabet/static_letters/{letter}.png'))

print(static_sprits)



