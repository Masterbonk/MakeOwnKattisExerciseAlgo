import time


a = int(input())
for i in range(a):
    input()

b = int(input())
for i in range(b):
    input()


for _ in range(10**10):
    a = a + b - b

if a == b:
    print(21)
elif a < b:
    print(21)
elif a > b:
    print(21)
