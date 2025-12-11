n = [4, 0, 12, 6, 8, 5, 3, 9, 1, 7, 6, 2, 10, 6, 3, 5, 0, 4, 11, 6]
c = 0 
for i in n:
    if i <= 6:
        c += 1
print("Perfect Overs : ", c)