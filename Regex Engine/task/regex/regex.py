import sys
sys.setrecursionlimit(10000)


def multi_character_check(data):
    regex, user_input = data.split('|')
    if '' in [regex, user_input]:
        return regex in ['', '$'] or regex.strip('?').strip('*').strip('+') == '.'

    elif single_character_check(regex[0], user_input[0]):
        if len(regex) > 1 and regex[1] in ['*', '+']:
            if len(regex) > 2 and regex[2] == user_input[0]:
                return multi_character_check(f'{regex[2:]}|{user_input}')
            if regex[1] == '*':
                return multi_character_check(f'{regex}|{user_input[1:]}')
            alt_regex = regex.replace('+', '')
            return multi_character_check(f'{regex}|{user_input[1:]}') or multi_character_check(f'{alt_regex[1:]}|{user_input[1:]}')

        return multi_character_check(f'{regex[1:]}|{user_input[1:]}')
    else:
        if len(regex) > 1 and regex[1] == '*':
            return multi_character_check(f'{regex[2:]}|{user_input}')
        return False


def single_character_check(regex_character, user_character):
    if regex_character == '.':
        return True
    return regex_character == user_character


def reg_engine(data):
    regex, user_input = data.split('|')
    if regex.startswith('^'):
        if regex.endswith('$') and len(regex) == 2:
            return False
        if any(operator in regex for operator in ['?', '*', '+']):
            return reg_engine(f'{regex[1:]}|{user_input}')
        return multi_character_check(f'{regex[1:]}|{user_input}')

    if '?' in regex:
        operator_index = regex.index('?')
        regex = regex.replace('?', '')
        alt_regex = regex[:operator_index - 1] + regex[operator_index:]
        return reg_engine(f'{regex}|{user_input}') or reg_engine(f'{alt_regex}|{user_input}')

    if multi_character_check(f'{regex}|{user_input}'):
        return True
    elif len(regex) > len(user_input):
        return False
    else:
        return reg_engine(f'{regex}|{user_input[1:]}')


if __name__ == "__main__":
    print(reg_engine(input()))
