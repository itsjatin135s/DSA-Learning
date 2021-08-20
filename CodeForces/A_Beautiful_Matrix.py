m,n  = 5,5
y = 0
x = 0
arr = []
for i in range(0,n):
    arr=input().split()
    try:
        x = arr.index('1')
        y = i
    except:
        continue
a = x-2
b = y-2
if a <0:
    a = -a
if b<0:
    b = -b
print(a+b)