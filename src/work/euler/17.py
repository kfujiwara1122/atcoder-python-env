ln = [
    0,  # zero: no
    3,  # one
    3,  # two
    5,  # three
    4,  # four
    4,  # five
    3,  # six
    5,  # seven
    5,  # eight
    4,  # nine
]
lty = [
    0,  # zero: no
    0,  # ten: no
    6,  # twenty
    6,  # thirty
    5,  # forty
    5,  # fifty
    5,  # sixty
    7,  # seventy
    6,  # eighty
    6,  # ninety
]
lteen = [
    3,  # ten
    6,  # eleven
    6,  # tewlve
    8,  # thirteen
    8,  # fourteen
    7,  # fifteen
    7,  # sixteen
    9,  # seventeen
    8,  # eighteen
    8,  # nineteen
]

print(
    sum(ln) * 100
    + sum(lty) * 100
    + sum(lteen) * 10
    + sum(ln) * 100
    + 7 * 900  # hundred
    + 3 * 890  # and
    + 11  # one thousand
)
