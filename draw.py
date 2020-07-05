import pygame
import itertools
from pirple.hangman import animations
from pirple.hangman import load_sprits as sprits
from pirple.hangman.main import mainloop as game

pygame.font.init()

# setting window
win_width = 655
win_height = 619

window = pygame.display.set_mode((win_width, win_height))
pygame.display.set_caption('Hangman!')

info_font = pygame.font.SysFont('inkfree', 25)
word_font = pygame.font.SysFont('inkfree', 25)
guess_font = pygame.font.SysFont('inkfree', 25)


class Button:
    def __init__(self, color, x, y, width, height, text='', text_size=60):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.text_size = text_size

    def draw(self, win, outline=None):
        # Call this method to draw the button on the screen
        if outline:
            pygame.draw.rect(win, outline, (self.x - 2, self.y - 2, self.width + 4, self.height + 4), 0)

        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height), 0)

        if self.text != '':
            font = pygame.font.SysFont('comicsans', self.text_size)
            text = font.render(self.text, 1, (0, 0, 0))
            win.blit(text, (self.x + round(self.width / 2 - text.get_width() / 2),
                            (self.y + round(self.height / 2 - text.get_height() / 2))))

    def isOver(self, pos):
        # Pos is the mouse position or a tuple of (x,y) coordinates
        if self.x < pos[0] < self.x + self.width:
            if self.y < pos[1] < self.y + self.height:
                return True

        return False


start_player_vs_player = Button((0, 96, 205), (win_width // 2) / 2, win_height / 4, 400, 100, 'Player vs player')
start_player_vs_bot = Button((0, 96, 205), (win_width // 2) / 2, win_height / 2, 400, 100, 'Play vs bot')


def draw_true_letters(word, true_letters):

    return_word = ''
    for letter in word:
        if letter in true_letters:
            return_word += letter
        else:
            return_word += '_ '
    return return_word


def draw_options():
    window.blit(sprits.main_page, (0, 0))
    start_player_vs_player.draw(window, (0, 0, 0))
    start_player_vs_bot.draw(window, (0, 0, 0))
    pygame.display.update()


def draw_game_window(word, guess, info_text, state,
                     false_letters, true_letters):  # the state of the game is based on lives or if the game is started

    window.blit(sprits.static_sprits[state], (0, 0))

    draw_false_letters(false_letters)

    window.blit(info_font.render(info_text, 1, (0, 0, 0)), (win_width - 10 - (len(info_text) * 12), 25))

    window.blit(word_font.render(draw_true_letters(word, true_letters), 1, (0, 0, 0)), (win_width / 2 - (len(word) * 4), 65))

    window.blit(guess_font.render(guess, 1, (0, 0, 0)), (win_width / 2 - (len(guess) * 4), 100))

    pygame.display.update()


def draw_false_letters(letter_list):
    positions = [(105, 288), (140, 288), (176, 288), (212, 288), (248, 288), (105, 316), (140, 316), (176, 316),
                 (212, 316), (248, 316), (105, 344), (140, 344), (176, 344), (212, 344), (248, 344), (105, 371),
                 (140, 371), (176, 371), (212, 371), (248, 371), (105, 399), (140, 399), (176, 399), (212, 399),
                 (248, 399), (105, 425), (140, 425), (176, 425), (212, 425)]

    letter_positions = list(zip(letter_list, itertools.count()))

    for letter, position in letter_positions:
        window.blit(sprits.static_letters[letter], positions[position])
