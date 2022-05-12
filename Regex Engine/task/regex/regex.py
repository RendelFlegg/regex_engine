import sys
sys.setrecursionlimit(10000)


def multi_character_check(data):
    regex, user_input = data.split('|')
    if '' in [regex, user_input]:
        return regex == ''
    elif single_character_check(regex[0], user_input[0]):
        return multi_character_check(f'{regex[1:]}|{user_input[1:]}')
    else:
        return False


def single_character_check(regex_character, user_character):
    if regex_character == '.':
        return True
    return regex_character == user_character


def reg_engine(data):
    regex, user_input = data.split('|')
    if multi_character_check(f'{regex}|{user_input}'):
        return True
    elif len(regex) > len(user_input):
        return False
    else:
        return reg_engine(f'{regex}|{user_input[1:]}')


print(reg_engine(input()))
