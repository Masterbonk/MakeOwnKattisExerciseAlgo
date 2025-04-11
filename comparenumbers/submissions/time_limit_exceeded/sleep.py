import time


a = int(input())
b = int(input())

for _ in range(10**10):
    a = a + b - b

if a == b:
    print("equal")
elif a < b:
    print("smaller")
elif a > b:
    print("bigger")
