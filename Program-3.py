# Since i wanted comma seperated values as output
a = int(input("Enter a number: "))

numbers = []

for i in range(a):
    num = 2 * i + 1
    numbers.append(str(num))  

output = ', '.join(numbers)

print(output)
