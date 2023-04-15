number = int(input())
print(2**number-1)


def hanoi(number, start, goal, assist):
    if number == 1:
        print(start, goal, sep = " ")
    else:
        hanoi(number-1, start, assist, goal)
        print(start, goal, sep = " ")
        hanoi(number-1, assist, goal, start)


hanoi(number, 1,3,2)
