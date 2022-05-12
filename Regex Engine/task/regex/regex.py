data = input()
regex, user_input = data.split('|')

if regex == '':
    print(True)
elif user_input == '':
    print(False)
elif regex == '.':
    print(True)
else:
    print(regex == user_input)
