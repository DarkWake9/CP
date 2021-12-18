x = int(input())
y = int(input())
z = int(input())
n = int(input())
arr = []
for i in range(0,x+1):
    for j in range(0,y+1):
        for k in range(0,z+1):
            if i+j+k != n and not([i,j,k] in arr):
                arr.append([i,j,k])
print(arr)