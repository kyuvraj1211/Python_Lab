#sum and avg of 10 intergers
numbers = []
print("Enter 10 integers:")
for i in range(10):
    num = int(input(f"Number {i + 1}: "))
    numbers.append(num)

total_sum = sum(numbers)
average = total_sum / 10

print(f"The sum is: {total_sum}")
print(f"The average is: {average}")   
