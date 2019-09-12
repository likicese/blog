#coding=utf-8

n = input("N 为：")
m = input("M 为：")

if m > n:
    x = n
    n = m
    m = x

r = m % n

while r != 0:
    print("r:", r)
    m = n
    n =r
    r = m % n


print("N 和 M 的最大公约数是：", n)