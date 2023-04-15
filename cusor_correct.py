import sys

a_list = list(sys.stdin.readline().rstrip()) # rstrip() 함수는 공백을 제거해줌
b_list = [] # stack 두개 만들어 놓기
number = int(sys.stdin.readline())

for i in range(number):
    command = list(sys.stdin.readline())
    if command[0] == 'L' and a_list: # 'L'커서를 왼쪽으로 한 칸 옮김
        b_list.append(a_list.pop())

    elif command[0] == 'D'and b_list:  # 'D' 커서를 오른쪽으로 한 칸 옮김
        a_list.append(b_list.pop())

    elif command[0] == 'B':  # 커서 왼쪽에 있는 문자를 삭제함
        a_list.pop()

    elif command[0] == 'P':  # 문자를 커서 왼쪽에 추가함
        a_list.append(command[2])  # b_list += a_list.pop()을 해주지 않는 이유는 '커서 기준' 으로 스택에 넣기 때문!

b_list.reverse()
c_list = ''.join(a_list + b_list)
print(c_list)
