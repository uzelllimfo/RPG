import random

def set_settings():
    print('[#] <<::SETTINGS::>>')
    try:
        max_length = int(input('[~] Enter password max length (default length equally 12 chars) >> '))
    except:
        max_length = 11
    allow_chars = input('[~] Enter allow chars (or just skip it by pressing the enter button) >> ')
    return (max_length, allow_chars)

def get_random_password(max_length, allow_chars):
    chars = ''
    pswd  = ''

    if allow_chars == '':
        chars = [
        'A',
        'B',
        'C',
        'D',
        'E',
        'F',
        'G',
        'H',
        'I',
        'J',
        'K',
        'L',
        'M',
        'N',
        'O',
        'P',
        'Q',
        'R',
        'S',
        'T',
        'U',
        'V',
        'W',
        'X',
        'Y',
        'Z',
        'a',
        'b',
        'c',
        'd',
        'e',
        'f',
        'g',
        'h',
        'i',
        'j',
        'k',
        'l',
        'm',
        'n',
        'o',
        'p',
        'q',
        'r',
        's',
        't',
        'u',
        'v',
        'w',
        'x',
        'y',
        'z',
        '1',
        '2',
        '3',
        '4',
        '5',
        '6',
        '7',
        '8',
        '9',
        '0',
        '!',
        '@',
        '#',
        '$',
        '%',
        '^',
        '&',
        '*',
        '(',
        ')',
        '-',
        '_',
        '+',
        ';',
        '\\'
    ]
    else:
        chars = allow_chars

    random.seed(version=2)
    i = 0
    while i <= max_length:
        pswd+=chars[random.randrange(0, len(chars), 1)]
        i+=1

    return pswd

if __name__ == '__main__':
    max_length, allow_chars = set_settings()
    password                = get_random_password(max_length, allow_chars)
    print(f'[+] Your password: {password}')