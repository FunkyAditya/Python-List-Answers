# a,b,c = map(int, input().split())
# print(a,b, c)

# n = [int(i) for i in input().split()]
# print(*n)


# age = int(input("Enter Age : "))
# print(f"Your age is {age}.") 

# ph_num = "1234567890"
# for i in ph_num:
#     print(i)

# l = [1,2,3,4,5]
# print(l[3])

# test = [i for i in range(1,21)]
# print(*test)

# python program to create array of 5 integers and display arr items

# list = [i for i in range(1,6)]
# print(*list)
# print(list[int(input("Enter index to access : "))])

n = [int(i) for i in input().split()] #this better
# or
x = list(map(int, input().split()))

print(n, "\t", x)