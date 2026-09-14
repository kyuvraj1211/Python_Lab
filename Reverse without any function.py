#reverse without any function
lst = []
n = int(input("Enter the size of list"))
for i in range(n):
    lst.append(int(input(f"Enter the number {i+1}:")))

for i in range(n // 2):
    lst[i], lst[n - 1 - i] = lst[n - 1 - i], lst[i]

print(lst)   
