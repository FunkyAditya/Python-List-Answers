n = [3, 5, 2, 8, 7, 10] 

c = 0

for i in range(len(n)-1):
    if n[i] < n[i+1]:
        c += 1

print(c)
   
# solved