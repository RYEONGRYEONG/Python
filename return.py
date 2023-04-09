# 재귀 구조
# 공차가 3이고 첫 항이 1일 때
"""def seq(n):
    if n == 1:
        return 1
    else:
        return seq(n-1) + 3

a = seq(int(input())) # input은 문자열 취급이기 때문에 앞에 int() 해줘야 함
print(a)"""

# 피보나치 수열
# 첫 항과 두 번째 항이 1이고 나머지는 앞의 두 항을 더한 것
# 피보나치 수열은 등차수열처럼 차곡차곡 쌓이는 게 아니라 직전 두 항을 더한 값만 출력됨
"""def fib(n):
    if n ==1 or n ==2:
        return 1
    else:
        return fib(n-1) + fib(n-2)

a = fib(int(input()))
print(a)"""

# 선택 정렬 - 재귀
# 크기 순으로 정렬

"""def sel_sort_rec(n):
    if n != []:
        x= max(n)
        a.remove(x)
        return sel_sort_rec(n) + [x]
    else:
        return []

a = [4, 3, 5, 1, 2, 6, 8, 9, 3, 5, 2, 6, 7]
c = sel_sort_rec(a)
print(c)"""

# 선택 정렬
"""def sel_sort_rec(a):
    n = len(a)
    b = []
    while n > 1:
        x = max(a)
        a.remove(x)
        b = [x] + b # b = b + [x] 하면 작은 순대로 정렬됨
        n = n - 1
    return b # 들여쓰기 중요

a = [1,2,3,4,5]
c = sel_sort_rec(a)
print(c)"""

# print("안녕", "하세요", sep = "")

""" for elements in 'east':
    print(elements, end="") """ # 결과가 e-a-s-t-인 이유는?
