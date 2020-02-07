str1 = input('Van welk woord wilt u weten of het een palindroom is?:')
str1Reverse = str1[::-1]


def palindroom():
    if str1 == str1Reverse:
        print('Dit is een palindroom')
    else:
        print('Dit is geen palindroom')


def palindroom2():
    if str1 == reversed(str1):
        print('Dit is een palindroom')
    else:
        print('Dit is geen palindroom')


palindroom()


# [::-1] Bron: https://stackoverflow.com/questions/931092/reverse-a-string-in-python
