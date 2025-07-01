a = int(input("Enter a number: "))
if a % 2 == 0:
    a -= 1
numbers = []
for i in range(a):
    numbers.append(str(2*i + 1))
print(', '.join(numbers))
