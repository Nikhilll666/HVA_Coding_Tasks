# Write a program that calculates the sum of all the digits in a given number n.

n = int(input())
sum = 0
while n>0:
    x = n%10
    sum += x
    n = n//10
print(sum)
