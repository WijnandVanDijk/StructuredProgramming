lst = [8, 2, 3, 6, 8]
lst01 = [0, 0, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 0, 0, 1]
een = lst01.count(1)
nul = lst01.count(0)


def count():
    print(lst.count(8))


def diff():
    print(max(lst) - min(lst))


def eisen():
    if nul > een and nul > 12:
        print('Er zijn meer nullen dan eenen! En ook nog eens meer dan 12 nullen, dat is niet goed!')
    elif nul > een and nul < 12:
        print('Er zijn meer nullen dan eenen, dit is niet goed!')
    elif nul < een and nul > 12:
        print('Er zijn teveel nullen!')
    else:
        print('Niks aan de hand!')


