n = int(input())
a_lst = list(map(int, input().split()))
b_lst = list(map(int, input().split()))

num = 0

a_lst.sort()
b_lst.sort(reverse=True)

for (a, b) in zip(a_lst, b_lst):
    num += a*b

print(num)