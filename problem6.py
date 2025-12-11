n = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 55, 35, 25, 75, 65]
sum = 0
for i in n:
    sum = sum + i

length = len(n)

avg = sum/length


c = 0

for i in range(len(n)):
    if n[i] < avg:
        c += 1
print("Students who scored less than average", avg,"are", c)

#solved