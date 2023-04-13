#1406번 에디터, 시간초과이지만 맞는 코드
# 문자열 길이 L 커서가 위치할 수 있는 곳 L+1
# 자료구조 중 하나인 스택으로 풀어보기 => pop, push(append) 써보기
""" ex) a_list = [1,2,3]
        a_list.pop()
        3                """

#  예시 h e l l o

a_list = list(input())
cusor = len(a_list) + 1 # 커서는 문장의 맨 뒤에 위치, 인덱스는 길이보다 -1


number = int(input())

for i in range(number):
    command = list(input())
    if command[0] == 'L' and cusor > 1:
        cusor -= 1
    elif command[0] == 'D' and cusor < len(a_list) + 1:
        cusor += 1

    elif command[0] == 'B' and cusor > 1:
        a_list.pop(cusor - 2) # pop은 원소라서 -2 해주어야 함
        cusor -= 1

    elif command[0] == 'P':
        a_list.insert(cusor-1, command[2]) # insert는 중간중간 인덱싱이여서 -1
        cusor += 1

b = ''.join(i for i in a_list)
print(b)
