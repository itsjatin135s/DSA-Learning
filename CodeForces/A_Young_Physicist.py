m  =  int(input())
i = 0
j = 0
k = 0
a = []
for _ in range(0,m):
    a = input().split()
    x,y,z = a
    i = i+int(x)
    j = j+int(y)
    k = k+int(z)
if k==0 and i==0 and j==0:
    print("YES")
else:
    print("NO")