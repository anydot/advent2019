#!/usr/bin/python3


def data():
    with open("input_01.txt") as f:
        return [int(x.strip()) for x in f.readlines()[1:]]


def fuel(mass):
    return max(mass//3 - 2, 0)


def recufuel(mass):
    f = 0

    while mass > 0:
        mass = fuel(mass)
        f += mass

    return f


assert recufuel(100756) == 50346

print(sum([fuel(x) for x in data()]))
print(sum([recufuel(x) for x in data()]))

