import sys
sys.setrecursionlimit(10000)


def multi_character_check(data, backslash=False):
    regex, user_input = data.split('|')
    backslash = backslash
    if regex.startswith('\\') and not backslash:
        regex = regex[1:]
        backslash = True
    if '' in [regex, user_input]:
        return regex in ['', '$'] or regex.strip('?').strip('*').strip('+') == '.'

    elif single_character_check(regex[0], user_input[0], backslash=backslash):
        if len(regex) > 1 and regex[1] in ['?', '*', '+'] and not backslash:
            operator = regex[1]
            if len(regex) > 2 and operator in ['?', '*', '+'] and regex[2] == user_input[0]:
                return multi_character_check(f'{regex[2:]}|{user_input}', backslash=backslash)
            if operator == '?':
                operator_index = regex.index('?')
                regex = regex.replace('?', '')
                alt_regex = regex[:operator_index - 1] + regex[operator_index:]
                return multi_character_check(f'{regex}|{user_input}', backslash=backslash) or multi_character_check(f'{alt_regex}|{user_input}', backslash=backslash)
            if regex[1] == '*':
                return multi_character_check(f'{regex}|{user_input[1:]}', backslash=backslash)
            alt_regex = regex.replace('+', '')
            return multi_character_check(f'{regex}|{user_input[1:]}', backslash=backslash) or multi_character_check(f'{alt_regex[1:]}|{user_input[1:]}', backslash=backslash)

        return multi_character_check(f'{regex[1:]}|{user_input[1:]}', backslash=backslash)
    else:
        if len(regex) > 1 and regex[1] in ['?', '*']:
            return multi_character_check(f'{regex[2:]}|{user_input}', backslash=backslash)
        return False


def single_character_check(regex_character, user_character, backslash=False):
    if regex_character == '.' and not backslash:
        return True
    return regex_character == user_character


def reg_engine(data, backslash=False):
    regex, user_input = data.split('|')
    backslash = backslash
    if regex.startswith('\\') and not backslash:
        regex = regex[1:]
        backslash = True
    if regex.startswith('^'):
        if regex.endswith('$') and len(regex) == 2:
            return False
        if any(operator in regex for operator in ['?', '*', '+']):
            return reg_engine(f'{regex[1:]}|{user_input}', backslash=backslash)
        return multi_character_check(f'{regex[1:]}|{user_input}', backslash=backslash)
    if multi_character_check(f'{regex}|{user_input}', backslash=backslash):
        return True
    elif len(regex) > len(user_input):
        return False
    else:
        return reg_engine(f'{regex}|{user_input[1:]}', backslash=backslash)


if __name__ == "__main__":
    print(reg_engine(input()))
