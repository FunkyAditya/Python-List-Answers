n = [1, 2, 3, 7, 5]
c = 0

for i in range(len(n)-1):
    if n[i] > n[i+1]:
        c += 1
if c == 0:
    print("Sorted")
else:
    print("Not Sorted")

# solved