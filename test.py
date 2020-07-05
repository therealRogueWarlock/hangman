def draw_true_letters(word, true_letters):
    return_word = ''
    for letter in word:
        if letter in true_letters:
            return_word += letter
        else:
            return_word += '_ '
    return return_word



print(draw_true_letters('saaader', 'anseder'))