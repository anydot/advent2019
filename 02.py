#!/usr/bin/python3


def data():
    with open("input_02.txt") as f:
        return [int(x.strip()) for x in f.read().split(',')]


def run(data):
    ip = 0

    while True:
        if data[ip] == 1:
            (op1, op2, dst) = data[ip + 1:ip + 4]
            data[dst] = data[op1] + data[op2]
        elif data[ip] == 2:
            (op1, op2, dst) = data[ip + 1:ip + 4]
            data[dst] = data[op1] * data[op2]
        elif data[ip] == 99:
            return data
        else:
            assert False, "Position {0}, value {1}".format(ip, data[ip])

        ip += 4

assert data()[0:2] == [1, 0]
assert run([1, 0, 0, 0, 99]) == [2, 0, 0, 0, 99]
assert run([2, 3, 0, 3, 99]) == [2, 3, 0, 6, 99]
assert run([2, 4, 4, 5, 99, 0]) == [2, 4, 4, 5, 99, 9801]
assert run([1, 1, 1, 4, 99, 5, 6, 0, 99]) == [30, 1, 1, 4, 2, 5, 6, 0, 99]

d = data()
d[1] = 12
d[2] = 2

print(run(d)[0])

d = data()
for i in range(100):
    for j in range(100):
        nd = d[:]
        nd[1] = i
        nd[2] = j

        if run(nd)[0] == 19690720:
            print((100*i) + j)


