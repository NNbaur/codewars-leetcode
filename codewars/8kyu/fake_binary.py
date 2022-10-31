# Given a string of digits, you should replace any digit below 5 with '0' and any digit 5 and above with '1'. Return the resulting string.
#
# Note: input will never be an empty string


def fake_bin(x):
    string = ''
    for number in x:
        if number < '5':
            string += '0'
        else:
            string += '1'
    return string


def fake_bin1(x):
    return ''.join(['0' if i < '5' else '1' for i in x])
