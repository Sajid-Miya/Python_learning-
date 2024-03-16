numbers = input("Enter the numbers: ").split()

numbers = [int(num) for num in numbers]

largest = numbers[0]
    
for num in numbers:
    if num > largest:
        largest = num
print(f"Largest number: {largest}")

#     while num > largest:
#         largest = num
# print(f"Largest number: {largest}")