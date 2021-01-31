from flask import current_app, g
from random import randint


def get_word_list():
    '''Returns Dict with wordlist and length of wordlist, creates at first run'''
    if 'word_list' not in g:
        with current_app.open_resource(current_app.config['WORD_DICT']) as word_file:
            words = word_file.read().decode('utf8').splitlines()
        g.word_list = {'length': len(words), 'words': words}

    return g.word_list

def get_random_word(minlength=4, maxlength=8):
    '''Generates a random word from wordlist'''
    word_list = get_word_list()
    random_word = ''
    while len(random_word) < minlength or len(random_word) > maxlength:
        random_word = word_list['words'][randint(0, word_list['length'] - 1)]
    
    return random_word

def generate_short_url_name():
    '''Generates a random url name from wordlist'''
    return f'{get_random_word()}-{get_random_word()}-{get_random_word()}'
