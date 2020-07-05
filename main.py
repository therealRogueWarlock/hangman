# Project 2, Hangman
import pygame
from pirple.hangman import draw
import random

# setting clock
clock = pygame.time.Clock()


class MainLoop:
    def __init__(self):
        self.run_game = True
        self.word = ''
        self.false_letters = ''
        self.true_letters = ''
        self.player = 1
        self.fails = 0

    def start(self):  # main game loop
        print('starting main game loop')
        self.menu_loop()

    def menu_loop(self):
        self.restart()
        print('menu loop')
        run = True
        while run:
            clock.tick(60)

            draw.draw_options()

            for event in pygame.event.get():
                pos = pygame.mouse.get_pos()

                if event.type == pygame.QUIT:
                    self.run_game = False
                    run = False
                    print('shutting down')

                if event.type == pygame.KEYDOWN:

                    if event.key == pygame.K_SPACE:
                        draw.animations.animation_1(draw.window)
                        run = False
                        self.input_word()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if draw.start_player_vs_player.isOver(pos):
                        draw.animations.animation_1(draw.window)
                        run = False
                        self.input_word()

                    if draw.start_player_vs_bot.isOver(pos):
                        draw.animations.animation_1(draw.window)
                        run = False
                        self.choosing_word()
                        self.guess_letter_in_word()

                if event.type == pygame.MOUSEMOTION:
                    if draw.start_player_vs_player.isOver(pos):
                        draw.start_player_vs_player.color = (255, 0, 0)
                    else:
                        draw.start_player_vs_player.color = (0, 96, 205)

                    if draw.start_player_vs_bot.isOver(pos):
                        draw.start_player_vs_bot.color = (255, 0, 0)
                    else:
                        draw.start_player_vs_bot.color = (0, 96, 205)

    def input_word(self):
        print('input word loop')
        print('player 1 input word')
        self.restart()
        run = True
        while run:
            clock.tick(60)

            draw.draw_game_window(self.word, '', "Write a word!", 0, '', '')

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run_game = False
                    run = False
                    print('shutting down')

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        print(self.word)
                        if self.word:
                            run = False
                            self.guess_letter_in_word()
                        else:
                            print('input word')

                    elif event.key == pygame.K_BACKSPACE:
                        self.word = self.word[:-1]
                    else:
                        if event.unicode in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
                                             'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'æ', 'ø', 'å']:
                            if len(self.word) <= 30:
                                self.word += event.unicode

    def guess_letter_in_word(self):
        print('start guess loop')
        self.false_letters = ''
        self.true_letters = ''

        letter = ''
        run = True
        while run:
            clock.tick(60)

            draw.draw_game_window(self.word, letter, 'Guess a letter!', self.fails, self.false_letters, self.true_letters)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    self.run_game = False
                    print('shutting down')

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        print(letter)
                        if letter in self.word:
                            if letter not in self.true_letters:
                                self.true_letters += letter
                                print('true:', self.true_letters)
                            else:
                                print('cant guess same letter')

                        elif letter not in self.false_letters:
                            self.false_letters += letter
                            self.fails += 1
                            print('false:', self.false_letters)
                        else:
                            print('cant guess same letter')

                            # animations in a list, index to  draw correct animation
                            draw.animations.all_animations[self.fails](draw.window)

                        letter = ''  # resetting letter to none

                    elif event.key == pygame.K_BACKSPACE:
                        letter = letter[:-1]
                    else:
                        if event.unicode in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
                                             'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'æ', 'ø', 'å']:
                            if len(letter) < 1:
                                letter += event.unicode

            self.check_for_win()

            if self.fails == 6:
                run = False
                self.if_lose()

    def choosing_word(self):
        list_of_words = []
        with open('words.txt', 'r') as words:
            for word in words.readlines():
                word = word[:-1]  # removing invisible letter, might be a new line thing.
                list_of_words.append(word)

        self.word = random.choice(list_of_words)
        print(self.word)

    def check_for_win(self):
        true_word = ''
        for letter in self.word:
            if letter in self.true_letters:
                true_word += letter
            else:
                true_word += '_ '

        if true_word.count('_ ') == 0:
            self.if_win()
        else:
            return False

    def if_win(self):
        run = True
        while run:
            clock.tick(60)

            draw.draw_game_window(self.word, '', 'YOU WON! go to menu, hit enter', self.fails, self.false_letters, self.true_letters)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    self.run_game = False
                    print('shutting down')

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        run = False
                        self.menu_loop()

    def if_lose(self):
        run = True
        while run:
            clock.tick(60)

            draw.draw_game_window(self.word, self.word, 'You lost..! go to menu, hit enter', 6, self.false_letters,
                                  self.true_letters)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    self.run_game = False
                    print('shutting down')

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        run = False
                        self.menu_loop()

    def restart(self):
        self.word = ''
        self.fails = 0


mainloop = MainLoop()

if __name__ == "__main__":
    pygame.init()
    mainloop.start()
    pygame.quit()
