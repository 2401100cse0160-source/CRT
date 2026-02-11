n = int(input())
count = 0
while n > 0:
    count += 1
    n = n // 10
print(count)

print(len(str(n)))

#input=1565
#output=17
n = int(input())
temp = n
s = 0
while n>0:
    s += (n%10)
    n //= 10
print(s)


#method 3
print(sum(map(int,str(temp))))

#input = 456
#output = 6
n = int(input())

while n > 9:
    n = sum(map(int,str(n)))
print(n)


