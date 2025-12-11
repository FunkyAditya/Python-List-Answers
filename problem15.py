n = [0, 0, 1, 0, 0, 0]
c = 0

for i in range(len(n)-1):
    if n[i] == 0 and n[i+1] == 0:
        c += 1
print(c)