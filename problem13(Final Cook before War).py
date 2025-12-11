'''This is raw version'''

# n = [4, 0, 6, 0, 12, 8, 5, 0, 10, 3, 1, 0, 5, 6, 7, 8, 0, 4, 2, 1,]
# c = 0

# for i in n:
#     if i == 0:
#         c +=1 
# print(c)

# solved

'''This is full version'''
n = list(map(int, input("Enter 20 overs (0 to 36 runs each): ").split()))

if len(n) != 20:
    print("Error: You must enter exactly 20 numbers.")
    exit()

for x in n:
    if x < 0 or x > 36:
        print("Error: Each value must be between 0 and 36.")
        exit()

c = 0
for i in n:
    if i == 0:
        c += 1

print(c)